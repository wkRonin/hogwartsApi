# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 15:24
# @Author  : wkRonin
# @File    :tag.py
import requests

from wechatworkApi.api.base_api import BaseApi

"""
必填参数放到函数的参数中，非必填放到
"""


class Tag(BaseApi):

    def add(self, tagname, **kwargs):
        """
        添加标签
        :param tagname: 标签名
        :param kwargs: tagid，默认会自动生成
        :return:
        """
        # 添加的标签json体
        data = {
            "tagname": tagname
        }
        data.update(kwargs)
        # 添加标签
        r = self.send("POST", f"tag/create?access_token={self.token}", json=data)
        return r

    def delete(self, tagid):
        """
        删除tag
        :param tagid: 标签id
        :return:
        """
        r = self.send("GET", f"tag/delete?access_token={self.token}&tagid={tagid}")
        return r

    def update(self, tagid, tagname):
        """
        tag 更新
        :param tagid: 标签iid
        :param tagname: 标签名字
        :return:
        """
        data = {
                "tagid": tagid,
                "tagname": tagname
                }
        r = self.send("POST", f"tag/update?access_token={self.token}", json=data)
        return r

    def get(self):
        """
        获取所有tag
        :return:
        """
        r = self.send("GET", f"tag/list?access_token={self.token}")
        return r

    def is_in_taglist(self, tag_id):
        """
        获取标签列表判断新增的标签id是否在列表中
        :param tag_id: 新增的tagid
        :return:
        """
        tag_list = self.get().json().get("taglist")
        for tag in tag_list:
            if tag_id == tag.get("tagid"):
                return True
        return False
