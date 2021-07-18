# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 17:16
# @Author  : wkRonin
# @File    :base_api.py
import requests


class BaseApi:

    CORPID = "wwc71c43dfb2ba3f16"
    CORPSECRET = "nuTI08otYivePm7enI9RkBFzEkwQIdwdieu-i39Qvt4"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """
        获取token
        :return:
        """
        url = self.BASE_URL + f"/gettoken?corpid={self.CORPID}&corpsecret={self.CORPSECRET}"
        r = requests.get(url)
        return r.json().get("access_token")

    def send(self, method, url, **kwargs):
        """
        封装发送请求
        :param method: 请求方式
        :param url: 路由地址
        :param kwargs: 其它参数
        :return:
        """
        # post 和 get底层实现，requests.get == requests.request("GET")
        url = self.BASE_URL + url
        return requests.request(method, url, **kwargs)

