import sys
_module = sys.modules[__name__]
del sys
folder = _module
main = _module
network = _module
utils = _module

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


import torch.utils.data as data


import numpy as np


import random


import torch


import torch.nn as nn


import torch.nn.parallel


import torch.backends.cudnn as cudnn


import torch.optim as optim


import torch.utils.data


import torchvision.datasets as dset


import torchvision.transforms as transforms


import torchvision.utils as vutils


from torch.autograd import Variable


class _netG(nn.Module):

    def __init__(self, ngpu, nz):
        super(_netG, self).__init__()
        self.ngpu = ngpu
        self.nz = nz
        self.fc1 = nn.Linear(110, 768)
        self.tconv2 = nn.Sequential(nn.ConvTranspose2d(768, 384, 5, 2, 0, bias=False), nn.BatchNorm2d(384), nn.ReLU(True))
        self.tconv3 = nn.Sequential(nn.ConvTranspose2d(384, 256, 5, 2, 0, bias=False), nn.BatchNorm2d(256), nn.ReLU(True))
        self.tconv4 = nn.Sequential(nn.ConvTranspose2d(256, 192, 5, 2, 0, bias=False), nn.BatchNorm2d(192), nn.ReLU(True))
        self.tconv5 = nn.Sequential(nn.ConvTranspose2d(192, 64, 5, 2, 0, bias=False), nn.BatchNorm2d(64), nn.ReLU(True))
        self.tconv6 = nn.Sequential(nn.ConvTranspose2d(64, 3, 8, 2, 0, bias=False), nn.Tanh())

    def forward(self, input):
        if isinstance(input.data, torch.FloatTensor) and self.ngpu > 1:
            input = input.view(-1, self.nz)
            fc1 = nn.parallel.data_parallel(self.fc1, input, range(self.ngpu))
            fc1 = fc1.view(-1, 768, 1, 1)
            tconv2 = nn.parallel.data_parallel(self.tconv2, fc1, range(self.ngpu))
            tconv3 = nn.parallel.data_parallel(self.tconv3, tconv2, range(self.ngpu))
            tconv4 = nn.parallel.data_parallel(self.tconv4, tconv3, range(self.ngpu))
            tconv5 = nn.parallel.data_parallel(self.tconv5, tconv4, range(self.ngpu))
            tconv5 = nn.parallel.data_parallel(self.tconv6, tconv5, range(self.ngpu))
            output = tconv5
        else:
            input = input.view(-1, self.nz)
            fc1 = self.fc1(input)
            fc1 = fc1.view(-1, 768, 1, 1)
            tconv2 = self.tconv2(fc1)
            tconv3 = self.tconv3(tconv2)
            tconv4 = self.tconv4(tconv3)
            tconv5 = self.tconv5(tconv4)
            tconv5 = self.tconv6(tconv5)
            output = tconv5
        return output


class _netD(nn.Module):

    def __init__(self, ngpu, num_classes=10):
        super(_netD, self).__init__()
        self.ngpu = ngpu
        self.conv1 = nn.Sequential(nn.Conv2d(3, 16, 3, 2, 1, bias=False), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv2 = nn.Sequential(nn.Conv2d(16, 32, 3, 1, 0, bias=False), nn.BatchNorm2d(32), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv3 = nn.Sequential(nn.Conv2d(32, 64, 3, 2, 1, bias=False), nn.BatchNorm2d(64), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv4 = nn.Sequential(nn.Conv2d(64, 128, 3, 1, 0, bias=False), nn.BatchNorm2d(128), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv5 = nn.Sequential(nn.Conv2d(128, 256, 3, 2, 1, bias=False), nn.BatchNorm2d(256), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv6 = nn.Sequential(nn.Conv2d(256, 512, 3, 1, 0, bias=False), nn.BatchNorm2d(512), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.fc_dis = nn.Linear(13 * 13 * 512, 1)
        self.fc_aux = nn.Linear(13 * 13 * 512, num_classes)
        self.softmax = nn.Softmax()
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        if isinstance(input.data, torch.FloatTensor) and self.ngpu > 1:
            conv1 = nn.parallel.data_parallel(self.conv1, input, range(self.ngpu))
            conv2 = nn.parallel.data_parallel(self.conv2, conv1, range(self.ngpu))
            conv3 = nn.parallel.data_parallel(self.conv3, conv2, range(self.ngpu))
            conv4 = nn.parallel.data_parallel(self.conv4, conv3, range(self.ngpu))
            conv5 = nn.parallel.data_parallel(self.conv5, conv4, range(self.ngpu))
            conv6 = nn.parallel.data_parallel(self.conv6, conv5, range(self.ngpu))
            flat6 = conv6.view(-1, 13 * 13 * 512)
            fc_dis = nn.parallel.data_parallel(self.fc_dis, flat6, range(self.ngpu))
            fc_aux = nn.parallel.data_parallel(self.fc_aux, flat6, range(self.ngpu))
        else:
            conv1 = self.conv1(input)
            conv2 = self.conv2(conv1)
            conv3 = self.conv3(conv2)
            conv4 = self.conv4(conv3)
            conv5 = self.conv5(conv4)
            conv6 = self.conv6(conv5)
            flat6 = conv6.view(-1, 13 * 13 * 512)
            fc_dis = self.fc_dis(flat6)
            fc_aux = self.fc_aux(flat6)
        classes = self.softmax(fc_aux)
        realfake = self.sigmoid(fc_dis).view(-1, 1).squeeze(1)
        return realfake, classes


class _netG_CIFAR10(nn.Module):

    def __init__(self, ngpu, nz):
        super(_netG_CIFAR10, self).__init__()
        self.ngpu = ngpu
        self.nz = nz
        self.fc1 = nn.Linear(110, 384)
        self.tconv2 = nn.Sequential(nn.ConvTranspose2d(384, 192, 4, 1, 0, bias=False), nn.BatchNorm2d(192), nn.ReLU(True))
        self.tconv3 = nn.Sequential(nn.ConvTranspose2d(192, 96, 4, 2, 1, bias=False), nn.BatchNorm2d(96), nn.ReLU(True))
        self.tconv4 = nn.Sequential(nn.ConvTranspose2d(96, 48, 4, 2, 1, bias=False), nn.BatchNorm2d(48), nn.ReLU(True))
        self.tconv5 = nn.Sequential(nn.ConvTranspose2d(48, 3, 4, 2, 1, bias=False), nn.Tanh())

    def forward(self, input):
        if isinstance(input.data, torch.FloatTensor) and self.ngpu > 1:
            input = input.view(-1, self.nz)
            fc1 = nn.parallel.data_parallel(self.fc1, input, range(self.ngpu))
            fc1 = fc1.view(-1, 384, 1, 1)
            tconv2 = nn.parallel.data_parallel(self.tconv2, fc1, range(self.ngpu))
            tconv3 = nn.parallel.data_parallel(self.tconv3, tconv2, range(self.ngpu))
            tconv4 = nn.parallel.data_parallel(self.tconv4, tconv3, range(self.ngpu))
            tconv5 = nn.parallel.data_parallel(self.tconv5, tconv4, range(self.ngpu))
            output = tconv5
        else:
            input = input.view(-1, self.nz)
            fc1 = self.fc1(input)
            fc1 = fc1.view(-1, 384, 1, 1)
            tconv2 = self.tconv2(fc1)
            tconv3 = self.tconv3(tconv2)
            tconv4 = self.tconv4(tconv3)
            tconv5 = self.tconv5(tconv4)
            output = tconv5
        return output


class _netD_CIFAR10(nn.Module):

    def __init__(self, ngpu, num_classes=10):
        super(_netD_CIFAR10, self).__init__()
        self.ngpu = ngpu
        self.conv1 = nn.Sequential(nn.Conv2d(3, 16, 3, 2, 1, bias=False), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv2 = nn.Sequential(nn.Conv2d(16, 32, 3, 1, 1, bias=False), nn.BatchNorm2d(32), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv3 = nn.Sequential(nn.Conv2d(32, 64, 3, 2, 1, bias=False), nn.BatchNorm2d(64), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv4 = nn.Sequential(nn.Conv2d(64, 128, 3, 1, 1, bias=False), nn.BatchNorm2d(128), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv5 = nn.Sequential(nn.Conv2d(128, 256, 3, 2, 1, bias=False), nn.BatchNorm2d(256), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.conv6 = nn.Sequential(nn.Conv2d(256, 512, 3, 1, 1, bias=False), nn.BatchNorm2d(512), nn.LeakyReLU(0.2, inplace=True), nn.Dropout(0.5, inplace=False))
        self.fc_dis = nn.Linear(4 * 4 * 512, 1)
        self.fc_aux = nn.Linear(4 * 4 * 512, num_classes)
        self.softmax = nn.Softmax()
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        if isinstance(input.data, torch.FloatTensor) and self.ngpu > 1:
            conv1 = nn.parallel.data_parallel(self.conv1, input, range(self.ngpu))
            conv2 = nn.parallel.data_parallel(self.conv2, conv1, range(self.ngpu))
            conv3 = nn.parallel.data_parallel(self.conv3, conv2, range(self.ngpu))
            conv4 = nn.parallel.data_parallel(self.conv4, conv3, range(self.ngpu))
            conv5 = nn.parallel.data_parallel(self.conv5, conv4, range(self.ngpu))
            conv6 = nn.parallel.data_parallel(self.conv6, conv5, range(self.ngpu))
            flat6 = conv6.view(-1, 4 * 4 * 512)
            fc_dis = nn.parallel.data_parallel(self.fc_dis, flat6, range(self.ngpu))
            fc_aux = nn.parallel.data_parallel(self.fc_aux, flat6, range(self.ngpu))
        else:
            conv1 = self.conv1(input)
            conv2 = self.conv2(conv1)
            conv3 = self.conv3(conv2)
            conv4 = self.conv4(conv3)
            conv5 = self.conv5(conv4)
            conv6 = self.conv6(conv5)
            flat6 = conv6.view(-1, 4 * 4 * 512)
            fc_dis = self.fc_dis(flat6)
            fc_aux = self.fc_aux(flat6)
        classes = self.softmax(fc_aux)
        realfake = self.sigmoid(fc_dis).view(-1, 1).squeeze(1)
        return realfake, classes


import torch
from torch.nn import MSELoss, ReLU
from _paritybench_helpers import _mock_config, _mock_layer, _paritybench_base, _fails_compile


TESTCASES = [
    # (nn.Module, init_args, forward_args, jit_compiles)
    (_netD,
     lambda: ([], {'ngpu': False}),
     lambda: ([torch.rand([4, 3, 128, 128])], {}),
     False),
    (_netD_CIFAR10,
     lambda: ([], {'ngpu': False}),
     lambda: ([torch.rand([4, 3, 64, 64])], {}),
     False),
]

class Test_clvrai_ACGAN_PyTorch(_paritybench_base):
    def test_000(self):
        self._check(*TESTCASES[0])

    def test_001(self):
        self._check(*TESTCASES[1])

