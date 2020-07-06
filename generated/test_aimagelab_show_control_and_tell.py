import sys
_module = sys.modules[__name__]
del sys
config = _module
data = _module
dataset = _module
field = _module
CaptioningModel = _module
models = _module
controllable_captioning = _module
controllable_captioning_no_visual_sentinel = _module
controllable_captioning_single_sentinel = _module
test_region_sequence = _module
test_region_set = _module
train = _module
utils = _module
noun_iou = _module
nw_noun_aligner = _module
sinkhorn_network = _module

from _paritybench_helpers import _mock_config, patch_functional
from unittest.mock import mock_open, MagicMock
from torch.autograd import Function
from torch.nn import Module
import abc, collections, copy, enum, functools, inspect, itertools, logging, math, numbers, numpy, queue, random, re, scipy, sklearn, string, tensorflow, time, torch, torchaudio, torchtext, torchvision, types, typing, uuid, warnings
import numpy as np
from torch import Tensor
patch_functional()
open = mock_open()
yaml = logging = sys = argparse = MagicMock()
ArgumentParser = argparse.ArgumentParser
_global_config = args = argv = cfg = config = params = _mock_config()
argparse.ArgumentParser.return_value.parse_args.return_value = _global_config
yaml.load.return_value = _global_config
sys.argv = _global_config
__version__ = '1.0.0'


import torch


import numpy as np


import warnings


from itertools import groupby


from torch import nn


from torch import distributions


import functools


import torch.nn.functional as F


import random


import itertools


from torch.optim import Adam


from torch.optim.lr_scheduler import StepLR


from torch.nn import NLLLoss


class CaptioningModel(nn.Module):

    def __init__(self, seq_len):
        self.seq_len = seq_len
        super(CaptioningModel, self).__init__()

    def init_weights(self):
        raise NotImplementedError

    def init_state(self, b_s, device):
        raise NotImplementedError

    def step(self, t, state, prev_outputs, images, seqs, *args, mode='teacher_forcing'):
        raise NotImplementedError

    def forward(self, statics, seqs, *args):
        device = statics[0].device
        b_s = statics[0].size(0)
        seq_len = seqs[0].size(1)
        state = self.init_state(b_s, device)
        outs = None
        outputs = []
        for t in range(seq_len):
            outs, state = self.step(t, state, outs, statics, seqs, *args, mode='teacher_forcing')
            outputs.append(outs)
        outputs = list(zip(*outputs))
        outputs = tuple(torch.cat([oo.unsqueeze(1) for oo in o], 1) for o in outputs)
        return outputs

    def test(self, statics, *args):
        device = statics[0].device
        b_s = statics[0].size(0)
        state = self.init_state(b_s, device)
        outs = None
        outputs = []
        for t in range(self.seq_len):
            outs, state = self.step(t, state, outs, statics, None, *args, mode='feedback')
            outs = tuple(torch.max(o, -1)[1] for o in outs)
            outputs.append(outs)
        outputs = list(zip(*outputs))
        outputs = tuple(torch.cat([oo.unsqueeze(1) for oo in o], 1) for o in outputs)
        return outputs

    def sample_rl(self, statics, *args):
        device = statics[0].device
        b_s = statics[0].size(0)
        state = self.init_state(b_s, device)
        outputs = []
        log_probs = []
        for t in range(self.seq_len):
            prev_outputs = outputs[-1] if t > 0 else None
            outs, state = self.step(t, state, prev_outputs, statics, None, *args, mode='feedback')
            outputs.append([])
            log_probs.append([])
            for out in outs:
                distr = distributions.Categorical(logits=out)
                sample = distr.sample()
                outputs[-1].append(sample)
                log_probs[-1].append(distr.log_prob(sample))
        outputs = list(zip(*outputs))
        outputs = tuple(torch.cat([oo.unsqueeze(1) for oo in o], 1) for o in outputs)
        log_probs = list(zip(*log_probs))
        log_probs = tuple(torch.cat([oo.unsqueeze(1) for oo in o], 1) for o in log_probs)
        return outputs, log_probs

    def _select_beam(self, input, selected_beam, cur_beam_size, beam_size, b_s, reduced=True):
        if not isinstance(input, list) and not isinstance(input, tuple):
            return self._select_beam_i(input, selected_beam, cur_beam_size, beam_size, b_s, reduced=reduced)
        new_input = []
        for i, s in enumerate(input):
            if isinstance(s, tuple) or isinstance(s, list):
                new_state_i = []
                for ii, ss in enumerate(s):
                    new_state_ii = self._select_beam_i(ss, selected_beam, cur_beam_size, beam_size, b_s, reduced=reduced)
                    new_state_i.append(new_state_ii)
                new_input.append(tuple(new_state_i))
            else:
                new_state_i = self._select_beam_i(s, selected_beam, cur_beam_size, beam_size, b_s, reduced=reduced)
                new_input.append(new_state_i)
        return list(new_input)

    def _select_beam_i(self, input, selected_beam, cur_beam_size, beam_size, b_s, reduced=True):
        input_shape = input.shape
        if reduced:
            input_shape = input_shape[1:]
        else:
            input_shape = input_shape[2:]
        input_exp_shape = (b_s, cur_beam_size) + input_shape
        output_exp_shape = (b_s, beam_size) + input_shape
        input_red_shape = (b_s * beam_size,) + input_shape
        selected_beam_red_size = (b_s, beam_size) + tuple(1 for _ in range(len(input_exp_shape) - 2))
        selected_beam_exp_size = (b_s, beam_size) + input_exp_shape[2:]
        input_exp = input.view(input_exp_shape)
        selected_beam_exp = selected_beam.view(selected_beam_red_size).expand(selected_beam_exp_size)
        out = torch.gather(input_exp, 1, selected_beam_exp)
        if reduced:
            out = out.view(input_red_shape)
        else:
            out = out.view(output_exp_shape)
        return out

    def beam_search(self, statics, eos_idxs, beam_size, out_size=1, *args):
        device = statics[0].device
        b_s = statics[0].size(0)
        state = self.init_state(b_s, device)
        outputs = []
        log_probs = []
        selected_outs = None
        for t in range(self.seq_len):
            outs_logprob, state = self.step(t, state, selected_outs, statics, None, *args, mode='feedback')
            if t == 0:
                n_outs = len(outs_logprob)
                cur_beam_size = 1
                seq_logprob = statics[0].data.new_zeros([b_s, 1] + [1] * n_outs)
                seq_masks = [statics[0].data.new_ones((b_s, beam_size))] * n_outs
            else:
                cur_beam_size = beam_size
            old_seq_logprob = seq_logprob
            outs_logprob = [ol.view([b_s, cur_beam_size] + [1] * i + [-1] + [1] * (n_outs - i - 1)) for i, ol in enumerate(outs_logprob)]
            seq_logprob = seq_logprob + functools.reduce(operator.add, outs_logprob)
            if t > 0:
                masks = [(so.view(b_s, cur_beam_size) != idx).float() for idx, so in zip(eos_idxs, selected_outs)]
                seq_masks = [(sm * m) for sm, m in zip(seq_masks, masks)]
                outs_logprob = [(ol.squeeze() * sm.unsqueeze(-1)) for ol, sm in zip(outs_logprob, seq_masks)]
                old_seq_logprob = old_seq_logprob.expand_as(seq_logprob).contiguous()
                old_seq_logprob[:, :, 1:] = -999
                seq_mask_full = torch.clamp(torch.sum(torch.cat([sm.unsqueeze(0) for sm in seq_masks]), 0), 0, 1)
                seq_mask_full = seq_mask_full.view(list(seq_mask_full.shape) + [1] * n_outs)
                seq_logprob = seq_mask_full * seq_logprob + old_seq_logprob * (1 - seq_mask_full)
            selected_logprob, selected_idx = torch.sort(seq_logprob.view(b_s, -1), -1, descending=True)
            selected_logprob, selected_idx = selected_logprob[:, :beam_size], selected_idx[:, :beam_size]
            _div = functools.reduce(operator.mul, seq_logprob.shape[2:], 1)
            selected_beam = selected_idx / _div
            selected_outs = []
            for i in range(n_outs):
                if i == 0:
                    selected_idx = selected_idx - selected_beam * _div
                else:
                    selected_idx = selected_idx - selected_outs[-1] * _div
                _div = functools.reduce(operator.mul, seq_logprob.shape[3 + i:], 1)
                selected_outs.append(selected_idx / _div)
            state = self._select_beam(state, selected_beam, cur_beam_size, beam_size, b_s)
            statics = self._select_beam(statics, selected_beam, cur_beam_size, beam_size, b_s)
            seq_masks = self._select_beam(seq_masks, selected_beam, beam_size, beam_size, b_s, reduced=False)
            outputs = self._select_beam(outputs, selected_beam, cur_beam_size, beam_size, b_s, reduced=False)
            outputs.append([so.unsqueeze(-1) for so in selected_outs])
            seq_logprob = selected_logprob.view([b_s, beam_size] + [1] * n_outs)
            outs_logprob = [ol.view(b_s, cur_beam_size, -1) for ol in outs_logprob]
            this_word_logprob = self._select_beam(outs_logprob, selected_beam, cur_beam_size, beam_size, b_s, reduced=False)
            this_word_logprob = [torch.gather(o, 2, selected_outs[i].unsqueeze(-1)) for i, o in enumerate(this_word_logprob)]
            log_probs.append(this_word_logprob)
            selected_outs = [so.view(-1) for so in selected_outs]
        seq_logprob, sort_idxs = torch.sort(seq_logprob.view(b_s, beam_size, 1), 1, descending=True)
        outputs = list(zip(*outputs))
        outputs = [torch.cat(o, -1) for o in outputs]
        outputs = [torch.gather(o, 1, sort_idxs.expand(b_s, beam_size, self.seq_len)) for o in outputs]
        log_probs = list(zip(*log_probs))
        log_probs = [torch.cat(lp, -1) for lp in log_probs]
        log_probs = [torch.gather(lp, 1, sort_idxs.expand(b_s, beam_size, self.seq_len)) for lp in log_probs]
        outputs = [o.contiguous()[:, :out_size] for o in outputs]
        log_probs = [lp.contiguous()[:, :out_size] for lp in log_probs]
        if out_size == 1:
            outputs = [o.squeeze(1) for o in outputs]
            log_probs = [lp.squeeze(1) for lp in log_probs]
        return outputs, log_probs


class SinkhornNet(nn.Module):

    def __init__(self, N, n_iters, tau):
        super(SinkhornNet, self).__init__()
        self.n_iters = n_iters
        self.tau = tau
        self.W1_txt = nn.Linear(300, 128)
        self.W1_vis = nn.Linear(2048, 512)
        self.W2_vis = nn.Linear(512, 128)
        self.W_fc_pos = nn.Linear(260, 256)
        self.W_fc = nn.Linear(256, N)
        self.init_weights()

    def init_weights(self):
        nn.init.xavier_normal_(self.W1_txt.weight)
        nn.init.constant_(self.W1_txt.bias, 0)
        nn.init.xavier_normal_(self.W1_vis.weight)
        nn.init.constant_(self.W1_vis.bias, 0)
        nn.init.xavier_normal_(self.W2_vis.weight)
        nn.init.constant_(self.W2_vis.bias, 0)
        nn.init.xavier_normal_(self.W_fc_pos.weight)
        nn.init.constant_(self.W_fc_pos.bias, 0)
        nn.init.xavier_normal_(self.W_fc.weight)
        nn.init.constant_(self.W_fc.bias, 0)

    def sinkhorn(self, x):
        x = torch.exp(x / self.tau)
        for _ in range(self.n_iters):
            x = x / (1e-07 + torch.sum(x, -2, keepdim=True))
            x = x / (1e-07 + torch.sum(x, -1, keepdim=True))
        return x

    def forward(self, seq):
        x_txt = seq[:, :, :300]
        x_vis = seq[:, :, 300:2348]
        x_pos = seq[:, :, 2348:]
        x_txt = F.relu(self.W1_txt(x_txt))
        x_vis = F.relu(self.W1_vis(x_vis))
        x_vis = F.relu(self.W2_vis(x_vis))
        x = torch.cat((x_txt, x_vis, x_pos), dim=-1)
        x = F.relu(self.W_fc_pos(x))
        x = torch.tanh(self.W_fc(x))
        return self.sinkhorn(x)

