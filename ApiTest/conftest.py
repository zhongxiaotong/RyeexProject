#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/27 17:01
# @Author : Greey
# @FileName: conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption("--mcu", default='default mcu', help=u"固件路径")
    parser.addoption("--resoure", default='default resoure', help=u"资源路径")
    parser.addoption("--diff", default='default diff', help=u"差分资源路径")

@pytest.fixture()
def mcu(request):
    return request.config.getoption("--mcu")

@pytest.fixture()
def resoure(request):
    return request.config.getoption("--resoure")

@pytest.fixture()
def diff(request):
    return request.config.getoption("--diff")