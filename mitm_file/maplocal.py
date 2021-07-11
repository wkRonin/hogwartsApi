# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 18:27
# @Author  : wkRonin
# @File    :maplocal.py
import json

import mitmproxy.http
from mitmproxy import http, ctx


class MapLocal1:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 给定监听的url匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.pretty_url\
                and "x=" in flow.request.pretty_url:
            # 打开本地文件
            with open("quote.json", encoding="utf-8") as f:
                # 制造响应体
                flow.response = http.HTTPResponse.make(
                    # 状态码响应
                    200,
                    # 数据体
                    f.read(),
                )
            ctx.log.info(f"{flow.response.text}")


addons = [
    MapLocal1()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8889', '-s', __file__, '--ssl-insecure'])
