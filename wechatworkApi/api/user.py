# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 18:29
# @Author  : wkRonin
# @File    :user.py
from wechatworkApi.api.base_api import BaseApi


class User(BaseApi):

    def add(self, userid, name, mobile, department, **kwargs):
        data = {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
        }
        data.update(kwargs)
        r = self.send("POST", f"user/create?access_token={self.token}", json=data)
        return r

    def get(self, userid):
        r = self.send("GET", f"user/get?access_token={self.token}&userid={userid}")
        return r

    def update(self, userid, name):
        data = {
                "userid": userid,
                "name": name
        }
        r = self.send("POST", f"user/update?access_token={self.token}", json=data)
        return r

    def delete(self, userid):
        r = self.send("GET", f"user/delete?access_token={self.token}&userid={userid}")
        return r

    def userid_is_not_exist(self, userid):
        errcode = self.get(userid).json().get("errcode")
        if errcode == 60111:
            return True
        else:
            return False

