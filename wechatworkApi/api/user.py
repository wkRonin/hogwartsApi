# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 18:29
# @Author  : wkRonin
# @File    :user.py
from wechatworkApi.api.base_api import BaseApi


class User(BaseApi):

    def add(self, userid, name, mobile, department, **kwargs):
        """
        添加通讯录成员
        :param userid: 成员id
        :param name: 成员姓名
        :param mobile: 成员手机号
        :param department: 成员部门id列表
        :param kwargs: 其他参数
        :return:
        """
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
        """
        根据成员id获取对应的成员信息
        :param userid: 成员id
        :return:
        """
        r = self.send("GET", f"user/get?access_token={self.token}&userid={userid}")
        return r

    def update(self, userid, name):
        """
        根据成员id更新成员信息
        :param userid: 成员id
        :param name: 成员姓名
        :return:
        """
        data = {
                "userid": userid,
                "name": name
        }
        r = self.send("POST", f"user/update?access_token={self.token}", json=data)
        return r

    def delete(self, userid):
        """
        根据成员id删除成员
        :param userid: 成员id
        :return:
        """
        r = self.send("GET", f"user/delete?access_token={self.token}&userid={userid}")
        return r

    def userid_is_not_exist(self, userid):
        """
        根据查询接口的错误码 60111 判断成员id不在企业中
        :param userid: 成员id
        :return:
        """
        errcode = self.get(userid).json().get("errcode")
        if errcode == 60111:
            return True
        else:
            return False

