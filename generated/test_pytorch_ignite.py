import sys
_module = sys.modules[__name__]
del sys
conf = _module
main = _module
utils = _module
benchmark_fp32 = _module
benchmark_nvidia_apex = _module
benchmark_torch_cuda_amp = _module
mnist_with_neptune_logger = _module
mnist_with_tensorboard_logger = _module
mnist_with_tqdm_logger = _module
mnist_with_trains_logger = _module
mnist_with_visdom_logger = _module
mnist_with_wandb_logger = _module
handlers = _module
neural_style = _module
transformer_net = _module
vgg = _module
dcgan = _module
mnist = _module
mnist_save_resume_engine = _module
mnist_with_tensorboard = _module
mnist_with_tensorboard_on_tpu = _module
mnist_with_visdom = _module
dataflow = _module
dataloaders = _module
transforms = _module
vis = _module
common_training = _module
mlflow_training = _module
plx_training = _module
baseline_resnet50 = _module
check_baseline_resnet50 = _module
code = _module
datasets = _module
scripts = _module
download_dataset = _module
trains_training = _module
baseline_resnet101 = _module
baseline_resnet101_sbd = _module
actor_critic = _module
reinforce = _module
ignite = _module
_utils = _module
base = _module
mixins = _module
contrib = _module
engines = _module
common = _module
tbptt = _module
base_logger = _module
custom_events = _module
lr_finder = _module
mlflow_logger = _module
neptune_logger = _module
param_scheduler = _module
polyaxon_logger = _module
tensorboard_logger = _module
time_profilers = _module
tqdm_logger = _module
trains_logger = _module
visdom_logger = _module
wandb_logger = _module
metrics = _module
average_precision = _module
gpu_info = _module
precision_recall_curve = _module
regression = _module
_base = _module
canberra_metric = _module
fractional_absolute_error = _module
fractional_bias = _module
geometric_mean_absolute_error = _module
geometric_mean_relative_absolute_error = _module
manhattan_distance = _module
maximum_absolute_error = _module
mean_absolute_relative_error = _module
mean_error = _module
mean_normalized_bias = _module
median_absolute_error = _module
median_absolute_percentage_error = _module
median_relative_absolute_error = _module
r2_score = _module
wave_hedges_distance = _module
roc_auc = _module
distributed = _module
auto = _module
comp_models = _module
native = _module
xla = _module
launcher = _module
engine = _module
deterministic = _module
events = _module
exceptions = _module
checkpoint = _module
early_stopping = _module
terminate_on_nan = _module
timing = _module
accumulation = _module
accuracy = _module
confusion_matrix = _module
epoch_metric = _module
fbeta = _module
frequency = _module
loss = _module
mean_absolute_error = _module
mean_pairwise_distance = _module
mean_squared_error = _module
metric = _module
metrics_lambda = _module
precision = _module
recall = _module
root_mean_squared_error = _module
running_average = _module
top_k_categorical_accuracy = _module
setup = _module
tests = _module
test_mixins = _module
conftest = _module
test_common = _module
test_tbptt = _module
conftest = _module
test_base_logger = _module
test_custom_events = _module
test_lr_finder = _module
test_mlflow_logger = _module
test_neptune_logger = _module
test_param_scheduler = _module
test_polyaxon_logger = _module
test_tensorboard_logger = _module
test_time_profilers = _module
test_tqdm_logger = _module
test_trains_logger = _module
test_visdom_logger = _module
test_wandb_logger = _module
test__base = _module
test_canberra_metric = _module
test_fractional_absolute_error = _module
test_fractional_bias = _module
test_geometric_mean_absolute_error = _module
test_geometric_mean_relative_absolute_error = _module
test_manhattan_distance = _module
test_maximum_absolute_error = _module
test_mean_absolute_relative_error = _module
test_mean_error = _module
test_mean_normalized_bias = _module
test_median_absolute_error = _module
test_median_absolute_percentage_error = _module
test_median_relative_absolute_error = _module
test_r2_score = _module
test_wave_hedges_distance = _module
test_average_precision = _module
test_gpu_info = _module
test_precision_recall_curve = _module
test_roc_auc = _module
test_roc_curve = _module
check_idist_parallel = _module
test_base = _module
test_native = _module
test_xla = _module
test_auto = _module
test_launcher = _module
test_utils = _module
test_create_supervised = _module
test_deterministic = _module
test_engine = _module
test_engine_state_dict = _module
test_event_handlers = _module
test_checkpoint = _module
test_early_stopping = _module
test_handlers = _module
test_terminate_on_nan = _module
test_timing = _module
test_accumulation = _module
test_accuracy = _module
test_confusion_matrix = _module
test_dill = _module
test_epoch_metric = _module
test_fbeta = _module
test_frequency = _module
test_loss = _module
test_mean_absolute_error = _module
test_mean_pairwise_distance = _module
test_mean_squared_error = _module
test_metric = _module
test_metrics_lambda = _module
test_precision = _module
test_recall = _module
test_root_mean_squared_error = _module
test_running_average = _module
test_top_k_categorical_accuracy = _module

from _paritybench_helpers import _mock_config
from unittest.mock import mock_open, MagicMock
from torch.autograd import Function
from torch.nn import Module
open = mock_open()
logging = sys = argparse = MagicMock()
ArgumentParser = argparse.ArgumentParser
_global_config = args = argv = cfg = config = params = _mock_config()
argparse.ArgumentParser.return_value.parse_args.return_value = _global_config
sys.argv = _global_config
__version__ = '1.0.0'


import torch


import torch.nn as nn


import torch.optim as optim


from torch.nn import CrossEntropyLoss


from torch.optim import SGD


from torch.cuda.amp import GradScaler


from torch.cuda.amp import autocast


import torch.nn.functional as F


from torch import nn


from torch.utils.data import DataLoader


import numpy as np


import random


from torch.optim import Adam


from collections import OrderedDict


from collections import namedtuple


import warnings


import torch.utils.data as data


from torch.optim.lr_scheduler import StepLR


from torch.utils.tensorboard import SummaryWriter


from functools import partial


import torch.optim.lr_scheduler as lrs


import torch.distributed as dist


from torch.distributions import Categorical


from collections.abc import Mapping


from collections.abc import Sequence


from torch.utils.data.distributed import DistributedSampler


from abc import ABCMeta


from abc import abstractmethod


from typing import Any


from typing import Mapping


from typing import Optional


from torch.optim.optimizer import Optimizer


from torch.utils.data import Dataset


from torch.utils.data.sampler import Sampler


from typing import Callable


from typing import Dict


from typing import Sequence


from typing import Tuple


from typing import Union


import collections.abc as collections


from torch.nn.functional import pairwise_distance


import copy


import math


from torch.utils.data.sampler import RandomSampler


from torch.utils.data.sampler import WeightedRandomSampler


from torch.nn import Linear


from torch.nn.functional import mse_loss


from numpy.testing import assert_almost_equal


from torch.nn.functional import nll_loss


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class TransformerNet(torch.nn.Module):

    def __init__(self):
        super(TransformerNet, self).__init__()
        self.conv1 = ConvLayer(3, 32, kernel_size=9, stride=1)
        self.in1 = torch.nn.InstanceNorm2d(32, affine=True)
        self.conv2 = ConvLayer(32, 64, kernel_size=3, stride=2)
        self.in2 = torch.nn.InstanceNorm2d(64, affine=True)
        self.conv3 = ConvLayer(64, 128, kernel_size=3, stride=2)
        self.in3 = torch.nn.InstanceNorm2d(128, affine=True)
        self.res1 = ResidualBlock(128)
        self.res2 = ResidualBlock(128)
        self.res3 = ResidualBlock(128)
        self.res4 = ResidualBlock(128)
        self.res5 = ResidualBlock(128)
        self.deconv1 = UpsampleConvLayer(128, 64, kernel_size=3, stride=1,
            upsample=2)
        self.in4 = torch.nn.InstanceNorm2d(64, affine=True)
        self.deconv2 = UpsampleConvLayer(64, 32, kernel_size=3, stride=1,
            upsample=2)
        self.in5 = torch.nn.InstanceNorm2d(32, affine=True)
        self.deconv3 = ConvLayer(32, 3, kernel_size=9, stride=1)
        self.relu = torch.nn.ReLU()

    def forward(self, X):
        y = self.relu(self.in1(self.conv1(X)))
        y = self.relu(self.in2(self.conv2(y)))
        y = self.relu(self.in3(self.conv3(y)))
        y = self.res1(y)
        y = self.res2(y)
        y = self.res3(y)
        y = self.res4(y)
        y = self.res5(y)
        y = self.relu(self.in4(self.deconv1(y)))
        y = self.relu(self.in5(self.deconv2(y)))
        y = self.deconv3(y)
        return y


class ConvLayer(torch.nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride):
        super(ConvLayer, self).__init__()
        reflection_padding = kernel_size // 2
        self.reflection_pad = torch.nn.ReflectionPad2d(reflection_padding)
        self.conv2d = torch.nn.Conv2d(in_channels, out_channels,
            kernel_size, stride)

    def forward(self, x):
        out = self.reflection_pad(x)
        out = self.conv2d(out)
        return out


class ResidualBlock(torch.nn.Module):
    """ResidualBlock
    introduced in: https://arxiv.org/abs/1512.03385
    recommended architecture: http://torch.ch/blog/2016/02/04/resnets.html
    """

    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = ConvLayer(channels, channels, kernel_size=3, stride=1)
        self.in1 = torch.nn.InstanceNorm2d(channels, affine=True)
        self.conv2 = ConvLayer(channels, channels, kernel_size=3, stride=1)
        self.in2 = torch.nn.InstanceNorm2d(channels, affine=True)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        residual = x
        out = self.relu(self.in1(self.conv1(x)))
        out = self.in2(self.conv2(out))
        out = out + residual
        return out


class UpsampleConvLayer(torch.nn.Module):
    """UpsampleConvLayer
    Upsamples the input and then does a convolution. This method gives better results
    compared to ConvTranspose2d.
    ref: http://distill.pub/2016/deconv-checkerboard/
    """

    def __init__(self, in_channels, out_channels, kernel_size, stride,
        upsample=None):
        super(UpsampleConvLayer, self).__init__()
        self.upsample = upsample
        reflection_padding = kernel_size // 2
        self.reflection_pad = torch.nn.ReflectionPad2d(reflection_padding)
        self.conv2d = torch.nn.Conv2d(in_channels, out_channels,
            kernel_size, stride)

    def forward(self, x):
        x_in = x
        if self.upsample:
            x_in = torch.nn.functional.interpolate(x_in, mode='nearest',
                scale_factor=self.upsample)
        out = self.reflection_pad(x_in)
        out = self.conv2d(out)
        return out


class Vgg16(torch.nn.Module):

    def __init__(self, requires_grad=False):
        super(Vgg16, self).__init__()
        vgg_pretrained_features = models.vgg16(pretrained=True).features
        self.slice1 = torch.nn.Sequential()
        self.slice2 = torch.nn.Sequential()
        self.slice3 = torch.nn.Sequential()
        self.slice4 = torch.nn.Sequential()
        for x in range(4):
            self.slice1.add_module(str(x), vgg_pretrained_features[x])
        for x in range(4, 9):
            self.slice2.add_module(str(x), vgg_pretrained_features[x])
        for x in range(9, 16):
            self.slice3.add_module(str(x), vgg_pretrained_features[x])
        for x in range(16, 23):
            self.slice4.add_module(str(x), vgg_pretrained_features[x])
        if not requires_grad:
            for param in self.parameters():
                param.requires_grad = False

    def forward(self, X):
        h = self.slice1(X)
        h_relu1_2 = h
        h = self.slice2(h)
        h_relu2_2 = h
        h = self.slice3(h)
        h_relu3_3 = h
        h = self.slice4(h)
        h_relu4_3 = h
        vgg_outputs = namedtuple('VggOutputs', ['relu1_2', 'relu2_2',
            'relu3_3', 'relu4_3'])
        out = vgg_outputs(h_relu1_2, h_relu2_2, h_relu3_3, h_relu4_3)
        return out


class Net(nn.Module):
    """ A base class for both generator and the discriminator.
    Provides a common weight initialization scheme.

    """

    def weights_init(self):
        for m in self.modules():
            classname = m.__class__.__name__
            if 'Conv' in classname:
                m.weight.data.normal_(0.0, 0.02)
            elif 'BatchNorm' in classname:
                m.weight.data.normal_(1.0, 0.02)
                m.bias.data.fill_(0)

    def forward(self, x):
        return x


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=-1)


class Policy(nn.Module):

    def __init__(self):
        super(Policy, self).__init__()
        self.affine1 = nn.Linear(4, 128)
        self.action_head = nn.Linear(128, 2)
        self.value_head = nn.Linear(128, 1)
        self.saved_actions = []
        self.rewards = []

    def forward(self, x):
        x = F.relu(self.affine1(x))
        action_scores = self.action_head(x)
        state_values = self.value_head(x)
        return F.softmax(action_scores, dim=-1), state_values


class Policy(nn.Module):

    def __init__(self):
        super(Policy, self).__init__()
        self.affine1 = nn.Linear(4, 128)
        self.affine2 = nn.Linear(128, 2)
        self.saved_log_probs = []
        self.rewards = []

    def forward(self, x):
        x = F.relu(self.affine1(x))
        action_scores = self.affine2(x)
        return F.softmax(action_scores, dim=1)


class DummyModel(nn.Module):

    def __init__(self):
        super(DummyModel, self).__init__()
        self.net = nn.Linear(1, 1)

    def forward(self, x):
        return self.net(x)


class DummyModel(nn.Module):

    def __init__(self):
        super(DummyModel, self).__init__()
        self.net = nn.Linear(1, 1)

    def forward(self, x):
        return self.net(x)


class DummyModel(torch.nn.Module):

    def __init__(self):
        super(DummyModel, self).__init__()
        self.net = torch.nn.Linear(2, 2)

    def forward(self, x):
        return self.net(x)


class DummyModel(nn.Module):

    def __init__(self):
        super(DummyModel, self).__init__()
        self.net = nn.Linear(1, 1)

    def forward(self, x):
        return self.net(x)


class DummyPretrainedModel(nn.Module):

    def __init__(self):
        super(DummyPretrainedModel, self).__init__()
        self.features = nn.Linear(4, 2, bias=False)
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
        x = self.features(x)
        x = self.fc(x)
        return x


import torch
from _paritybench_helpers import _mock_config, _mock_layer, _paritybench_base, _fails_compile

class Test_pytorch_ignite(_paritybench_base):
    pass
    def test_000(self):
        self._check(ConvLayer(*[], **{'in_channels': 4, 'out_channels': 4, 'kernel_size': 4, 'stride': 1}), [torch.rand([4, 4, 4, 4])], {})

    def test_001(self):
        self._check(DummyModel(*[], **{}), [torch.rand([1, 1])], {})

    def test_002(self):
        self._check(DummyPretrainedModel(*[], **{}), [torch.rand([4, 4, 4, 4])], {})

    def test_003(self):
        self._check(Policy(*[], **{}), [torch.rand([4, 4, 4, 4])], {})

    def test_004(self):
        self._check(ResidualBlock(*[], **{'channels': 4}), [torch.rand([4, 4, 4, 4])], {})

    @_fails_compile()
    def test_005(self):
        self._check(UpsampleConvLayer(*[], **{'in_channels': 4, 'out_channels': 4, 'kernel_size': 4, 'stride': 1}), [torch.rand([4, 4, 4, 4])], {})

