# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 16:30
# @Author  : wkRonin
# @File    :mitm_study_first.py
"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]