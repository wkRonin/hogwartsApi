# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 16:58
# @Author  : wkRonin
# @File    :conftest.py
import threading
import time

import pytest


@pytest.fixture()
def get_unique_name():
    """
    自定义名称= 时间戳+线程名 ：防止并行时同名失败
    :return:
    """
    tag_name = str(time.time()) + threading.currentThread().name
    return tag_name
