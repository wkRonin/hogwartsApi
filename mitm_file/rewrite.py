# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 16:48
# @Author  : wkRonin
# @File    :rewrite.py
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
            # 打印请求发出去后的响应体内容
            ctx.log.info(f"{flow.response.text}")
            ctx.log.info(str(type(flow.response.text)))
            # 使用json的loads方法转为字典格式
            data = json.loads(flow.response.text)
            # 修改字典中的指定位置的数据，实现rewrite
            data["data"]["items"][0]["quote"]["name"] = "hogwarts1"
            data["data"]["items"][1]["quote"]["current"] = "99.99"
            # 替换响应体中的正文
            flow.response.text = json.dumps(data)


addons = [
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['--ssl-insecure', '-p', '8889', '-s', __file__])
