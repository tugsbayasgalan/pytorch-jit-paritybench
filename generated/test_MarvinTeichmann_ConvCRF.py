import sys
_module = sys.modules[__name__]
del sys
benchmark = _module
convcrf = _module
convcrf = _module
demo = _module
fullcrf = _module
fullcrf = _module
utils = _module
pascal_visualizer = _module
synthetic = _module
test_utils = _module
visualization = _module

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


import numpy as np


import logging


import torch


from torch.autograd import Variable


import time


import scipy as scp


import math


import warnings


import torch.nn as nn


from torch.nn import functional as nnfun


from torch.nn.parameter import Parameter


import torch.nn.functional as F


def _get_ind(dz):
    if dz == 0:
        return 0, 0
    if dz < 0:
        return 0, -dz
    if dz > 0:
        return dz, 0


def _negative(dz):
    """
    Computes -dz for numpy indexing. Goal is to use as in array[i:-dz].

    However, if dz=0 this indexing does not work.
    None needs to be used instead.
    """
    if dz == 0:
        return None
    else:
        return -dz


def show_memusage(device=0, name=''):
    gc.collect()
    gpu_stats = gpustat.GPUStatCollection.new_query()
    item = gpu_stats.jsonify()['gpus'][device]
    logging.info('{:>5}/{:>5} MB Usage at {}'.format(item['memory.used'], item['memory.total'], name))


class MessagePassingCol:
    """ Perform the Message passing of ConvCRFs.

    The main magic happens here.
    """

    def __init__(self, feat_list, compat_list, merge, npixels, nclasses, norm='sym', filter_size=5, clip_edges=0, use_gpu=False, blur=1, matmul=False, verbose=False, pyinn=False):
        assert use_gpu
        if not norm == 'sym' and not norm == 'none':
            raise NotImplementedError
        span = filter_size // 2
        assert filter_size % 2 == 1
        self.span = span
        self.filter_size = filter_size
        self.use_gpu = use_gpu
        self.verbose = verbose
        self.blur = blur
        self.pyinn = pyinn
        self.merge = merge
        self.npixels = npixels
        if not self.blur == 1 and self.blur % 2:
            raise NotImplementedError
        self.matmul = matmul
        self._gaus_list = []
        self._norm_list = []
        for feats, compat in zip(feat_list, compat_list):
            gaussian = self._create_convolutional_filters(feats)
            if not norm == 'none':
                mynorm = self._get_norm(gaussian)
                self._norm_list.append(mynorm)
            else:
                self._norm_list.append(None)
            gaussian = compat * gaussian
            self._gaus_list.append(gaussian)
        if merge:
            self.gaussian = sum(self._gaus_list)
            if not norm == 'none':
                raise NotImplementedError

    def _get_norm(self, gaus):
        norm_tensor = torch.ones([1, 1, self.npixels[0], self.npixels[1]])
        normalization_feats = torch.autograd.Variable(norm_tensor)
        if self.use_gpu:
            normalization_feats = normalization_feats
        norm_out = self._compute_gaussian(normalization_feats, gaussian=gaus)
        return 1 / torch.sqrt(norm_out + 1e-20)

    def _create_convolutional_filters(self, features):
        span = self.span
        bs = features.shape[0]
        if self.blur > 1:
            off_0 = (self.blur - self.npixels[0] % self.blur) % self.blur
            off_1 = (self.blur - self.npixels[1] % self.blur) % self.blur
            pad_0 = math.ceil(off_0 / 2)
            pad_1 = math.ceil(off_1 / 2)
            if self.blur == 2:
                assert pad_0 == self.npixels[0] % 2
                assert pad_1 == self.npixels[1] % 2
            features = torch.nn.functional.avg_pool2d(features, kernel_size=self.blur, padding=(pad_0, pad_1), count_include_pad=False)
            npixels = [math.ceil(self.npixels[0] / self.blur), math.ceil(self.npixels[1] / self.blur)]
            assert npixels[0] == features.shape[2]
            assert npixels[1] == features.shape[3]
        else:
            npixels = self.npixels
        gaussian_tensor = features.data.new(bs, self.filter_size, self.filter_size, npixels[0], npixels[1]).fill_(0)
        gaussian = Variable(gaussian_tensor)
        for dx in range(-span, span + 1):
            for dy in range(-span, span + 1):
                dx1, dx2 = _get_ind(dx)
                dy1, dy2 = _get_ind(dy)
                feat_t = features[:, :, dx1:_negative(dx2), dy1:_negative(dy2)]
                feat_t2 = features[:, :, dx2:_negative(dx1), dy2:_negative(dy1)]
                diff = feat_t - feat_t2
                diff_sq = diff * diff
                exp_diff = torch.exp(torch.sum(-0.5 * diff_sq, dim=1))
                gaussian[:, (dx + span), (dy + span), dx2:_negative(dx1), dy2:_negative(dy1)] = exp_diff
        return gaussian.view(bs, 1, self.filter_size, self.filter_size, npixels[0], npixels[1])

    def compute(self, input):
        if self.merge:
            pred = self._compute_gaussian(input, self.gaussian)
        else:
            assert len(self._gaus_list) == len(self._norm_list)
            pred = 0
            for gaus, norm in zip(self._gaus_list, self._norm_list):
                pred += self._compute_gaussian(input, gaus, norm)
        return pred

    def _compute_gaussian(self, input, gaussian, norm=None):
        if norm is not None:
            input = input * norm
        shape = input.shape
        num_channels = shape[1]
        bs = shape[0]
        if self.blur > 1:
            off_0 = (self.blur - self.npixels[0] % self.blur) % self.blur
            off_1 = (self.blur - self.npixels[1] % self.blur) % self.blur
            pad_0 = int(math.ceil(off_0 / 2))
            pad_1 = int(math.ceil(off_1 / 2))
            input = torch.nn.functional.avg_pool2d(input, kernel_size=self.blur, padding=(pad_0, pad_1), count_include_pad=False)
            npixels = [math.ceil(self.npixels[0] / self.blur), math.ceil(self.npixels[1] / self.blur)]
            assert npixels[0] == input.shape[2]
            assert npixels[1] == input.shape[3]
        else:
            npixels = self.npixels
        if self.verbose:
            show_memusage(name='Init')
        if self.pyinn:
            input_col = P.im2col(input, self.filter_size, 1, self.span)
        else:
            input_unfold = F.unfold(input, self.filter_size, 1, self.span)
            input_unfold = input_unfold.view(bs, num_channels, self.filter_size, self.filter_size, npixels[0], npixels[1])
            input_col = input_unfold
        k_sqr = self.filter_size * self.filter_size
        if self.verbose:
            show_memusage(name='Im2Col')
        product = gaussian * input_col
        if self.verbose:
            show_memusage(name='Product')
        product = product.view([bs, num_channels, k_sqr, npixels[0], npixels[1]])
        message = product.sum(2)
        if self.verbose:
            show_memusage(name='FinalNorm')
        if self.blur > 1:
            in_0 = self.npixels[0]
            in_1 = self.npixels[1]
            message = message.view(bs, num_channels, npixels[0], npixels[1])
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                message = torch.nn.functional.upsample(message, scale_factor=self.blur, mode='bilinear')
            message = message[:, :, pad_0:pad_0 + in_0, pad_1:in_1 + pad_1]
            message = message.contiguous()
            message = message.view(shape)
            assert message.shape == shape
        if norm is not None:
            message = norm * message
        return message


def exp_and_normalize(features, dim=0):
    """
    Aka "softmax" in deep learning literature
    """
    normalized = torch.nn.functional.softmax(features, dim=dim)
    return normalized


class ConvCRF(nn.Module):
    """
        Implements a generic CRF class.

    This class provides tools to build
    your own ConvCRF based model.
    """

    def __init__(self, npixels, nclasses, conf, mode='conv', filter_size=5, clip_edges=0, blur=1, use_gpu=False, norm='sym', merge=False, verbose=False, trainable=False, convcomp=False, weight=None, final_softmax=True, unary_weight=10, pyinn=False):
        super(ConvCRF, self).__init__()
        self.nclasses = nclasses
        self.filter_size = filter_size
        self.clip_edges = clip_edges
        self.use_gpu = use_gpu
        self.mode = mode
        self.norm = norm
        self.merge = merge
        self.kernel = None
        self.verbose = verbose
        self.blur = blur
        self.final_softmax = final_softmax
        self.pyinn = pyinn
        self.conf = conf
        self.unary_weight = unary_weight
        if self.use_gpu:
            if not torch.cuda.is_available():
                logging.error('GPU mode requested but not avaible.')
                logging.error('Please run using use_gpu=False.')
                raise ValueError
        self.npixels = npixels
        if type(npixels) is tuple or type(npixels) is list:
            self.height = npixels[0]
            self.width = npixels[1]
        else:
            self.npixels = npixels
        if trainable:

            def register(name, tensor):
                self.register_parameter(name, Parameter(tensor))
        else:

            def register(name, tensor):
                self.register_buffer(name, Variable(tensor))
        if weight is None:
            self.weight = None
        else:
            register('weight', weight)
        if convcomp:
            self.comp = nn.Conv2d(nclasses, nclasses, kernel_size=1, stride=1, padding=0, bias=False)
            self.comp.weight.data.fill_(0.1 * math.sqrt(2.0 / nclasses))
        else:
            self.comp = None

    def clean_filters(self):
        self.kernel = None

    def add_pairwise_energies(self, feat_list, compat_list, merge):
        assert len(feat_list) == len(compat_list)
        assert self.use_gpu
        self.kernel = MessagePassingCol(feat_list=feat_list, compat_list=compat_list, merge=merge, npixels=self.npixels, filter_size=self.filter_size, nclasses=self.nclasses, use_gpu=True, norm=self.norm, verbose=self.verbose, blur=self.blur, pyinn=self.pyinn)

    def inference(self, unary, num_iter=5):
        if not self.conf['logsoftmax']:
            lg_unary = torch.log(unary)
            prediction = exp_and_normalize(lg_unary, dim=1)
        else:
            lg_unary = nnfun.log_softmax(unary, dim=1, _stacklevel=5)
            if self.conf['softmax'] and False:
                prediction = exp_and_normalize(lg_unary, dim=1)
            else:
                prediction = lg_unary
        for i in range(num_iter):
            message = self.kernel.compute(prediction)
            if self.comp is not None:
                comp = self.comp(message)
                message = message + comp
            if self.weight is None:
                prediction = lg_unary + message
            else:
                prediction = (self.unary_weight - self.weight) * lg_unary + self.weight * message
            if not i == num_iter - 1 or self.final_softmax:
                if self.conf['softmax']:
                    prediction = exp_and_normalize(prediction, dim=1)
        return prediction

    def start_inference(self):
        pass

    def step_inference(self):
        pass


class GaussCRF(nn.Module):
    """ Implements ConvCRF with hand-crafted features.

        It uses the more generic ConvCRF class as basis and utilizes a config
        dict to easily set hyperparameters and follows the design choices of:
        Philipp Kraehenbuehl and Vladlen Koltun, "Efficient Inference in Fully
        "Connected CRFs with Gaussian Edge Pots" (arxiv.org/abs/1210.5644)
    """

    def __init__(self, conf, shape, nclasses=None):
        super(GaussCRF, self).__init__()
        self.conf = conf
        self.shape = shape
        self.nclasses = nclasses
        self.trainable = conf['trainable']
        if not conf['trainable_bias']:
            self.register_buffer('mesh', self._create_mesh())
        else:
            self.register_parameter('mesh', Parameter(self._create_mesh()))
        if self.trainable:

            def register(name, tensor):
                self.register_parameter(name, Parameter(tensor))
        else:

            def register(name, tensor):
                self.register_buffer(name, Variable(tensor))
        register('pos_sdims', torch.Tensor([1 / conf['pos_feats']['sdims']]))
        if conf['col_feats']['use_bias']:
            register('col_sdims', torch.Tensor([1 / conf['col_feats']['sdims']]))
        else:
            self.col_sdims = None
        register('col_schan', torch.Tensor([1 / conf['col_feats']['schan']]))
        register('col_compat', torch.Tensor([conf['col_feats']['compat']]))
        register('pos_compat', torch.Tensor([conf['pos_feats']['compat']]))
        if conf['weight'] is None:
            weight = None
        elif conf['weight'] == 'scalar':
            val = conf['weight_init']
            weight = torch.Tensor([val])
        elif conf['weight'] == 'vector':
            val = conf['weight_init']
            weight = val * torch.ones(1, nclasses, 1, 1)
        self.CRF = ConvCRF(shape, nclasses, mode='col', conf=conf, use_gpu=True, filter_size=conf['filter_size'], norm=conf['norm'], blur=conf['blur'], trainable=conf['trainable'], convcomp=conf['convcomp'], weight=weight, final_softmax=conf['final_softmax'], unary_weight=conf['unary_weight'], pyinn=conf['pyinn'])
        return

    def forward(self, unary, img, num_iter=5):
        """ Run a forward pass through ConvCRF.

        Arguments:
            unary: torch.Tensor with shape [bs, num_classes, height, width].
                The unary predictions. Logsoftmax is applied to the unaries
                during inference. When using CNNs don't apply softmax,
                use unnormalized output (logits) instead.

            img: torch.Tensor with shape [bs, 3, height, width]
                The input image. Default config assumes image
                data in [0, 255]. For normalized images adapt
                `schan`. Try schan = 0.1 for images in [-0.5, 0.5]
        """
        conf = self.conf
        bs, c, x, y = img.shape
        pos_feats = self.create_position_feats(sdims=self.pos_sdims, bs=bs)
        col_feats = self.create_colour_feats(img, sdims=self.col_sdims, schan=self.col_schan, bias=conf['col_feats']['use_bias'], bs=bs)
        compats = [self.pos_compat, self.col_compat]
        self.CRF.add_pairwise_energies([pos_feats, col_feats], compats, conf['merge'])
        prediction = self.CRF.inference(unary, num_iter=num_iter)
        self.CRF.clean_filters()
        return prediction

    def _create_mesh(self, requires_grad=False):
        hcord_range = [range(s) for s in self.shape]
        mesh = np.array(np.meshgrid(*hcord_range, indexing='ij'), dtype=np.float32)
        return torch.from_numpy(mesh)

    def create_colour_feats(self, img, schan, sdims=0.0, bias=True, bs=1):
        norm_img = img * schan
        if bias:
            norm_mesh = self.create_position_feats(sdims=sdims, bs=bs)
            feats = torch.cat([norm_mesh, norm_img], dim=1)
        else:
            feats = norm_img
        return feats

    def create_position_feats(self, sdims, bs=1):
        if type(self.mesh) is Parameter:
            return torch.stack(bs * [self.mesh * sdims])
        else:
            return torch.stack(bs * [Variable(self.mesh) * sdims])

