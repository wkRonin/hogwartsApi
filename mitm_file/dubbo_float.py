# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 19:36
# @Author  : wkRonin
# @File    :dubbo_float.py
import json

import mitmproxy.http
from mitmproxy import http, ctx


class Rewrite:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 给定监听的url匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?" in flow.request.pretty_url \
                and "x=" in flow.request.pretty_url:
            ctx.log.info(f"{flow.response.text}")
            # 使用json的loads方法转为字典格式
            data = json.loads(flow.response.text)
            # 调用递归实现浮点的翻倍
            new_data = self.my_recursion(data, 3)
            # 修改响应后返回
            flow.response.text = json.dumps(new_data)

    def my_recursion(self, data, times=1):
        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = self.my_recursion(v, times)
        elif isinstance(data, list):
            data = [self.my_recursion(i, times) for i in data]
        elif isinstance(data, float):
            data = data * times
        else:
            data = data
        return data


addons = [
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8889', '-s', __file__])
