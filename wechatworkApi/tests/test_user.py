# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 20:35
# @Author  : wkRonin
# @File    :test_user.py
from faker import Faker

from wechatworkApi.api.user import User


class TestUser:

    def setup_class(self):
        self.user = User()
        self.fake = Faker('zh_CN')

    def test_add(self, get_unique_name):
        """
        测试添加成员接口
        :param get_unique_name: 自定义名称
        :return: 断言添加成员是否成功以及添加后是否能查询得到
        """
        name = self.fake.name()
        mobile = self.fake.phone_number()
        new_userid = self.user.add(get_unique_name, name, mobile, 1).json()
        assert new_userid.get("errcode") == 0
        assert self.user.get(get_unique_name).json().get("errcode") == 0

    def test_get(self, get_unique_name):
        """
        测试查询成员接口
        :param get_unique_name: 自定义名称
        :return: 断言是否能查询到新增的成员
        """
        name = self.fake.name()
        mobile = self.fake.phone_number()
        self.user.add(get_unique_name, name, mobile, 1)
        assert self.user.get(get_unique_name).json().get("errcode") == 0

    def test_delete(self, get_unique_name):
        """
        测试删除成员接口
        :param get_unique_name: 自定义名称
        :return: 断言删除成员是否成功以及查询此成员返回的错误码是否为成员不在企业中的错误码
        """
        name = self.fake.name()
        mobile = self.fake.phone_number()
        self.user.add(get_unique_name, name, mobile, 1)
        assert self.user.delete(get_unique_name).json().get("errcode") == 0
        assert self.user.userid_is_not_exist(get_unique_name)

    def test_update(self, get_unique_name):
        """
        测试更新成员接口
        :param get_unique_name: 自定义名称
        :return: 断言成员姓名是否更新成功
        """
        name = self.fake.name()
        mobile = self.fake.phone_number()
        new_name = self.fake.name()
        self.user.add(get_unique_name, name, mobile, 1)
        assert self.user.update(get_unique_name, new_name).json().get("errcode") == 0
