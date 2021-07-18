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
        name = self.fake.name()
        mobile = self.fake.phone_number()
        new_userid = self.user.add(get_unique_name, name, mobile, 1).json()
        assert new_userid.get("errcode") == 0
        assert self.user.get(get_unique_name).json().get("errcode") == 0

    def test_get(self, get_unique_name):
        name = self.fake.name()
        mobile = self.fake.phone_number()
        self.user.add(get_unique_name, name, mobile, 1)
        assert self.user.get(get_unique_name).json().get("errcode") == 0

    def test_delete(self, get_unique_name):
        name = self.fake.name()
        mobile = self.fake.phone_number()
        self.user.add(get_unique_name, name, mobile, 1)
        assert self.user.delete(get_unique_name).json().get("errcode") == 0
        assert self.user.userid_is_not_exist(get_unique_name)

    def test_update(self, get_unique_name):
        name = self.fake.name()
        mobile = self.fake.phone_number()
        new_name = self.fake.name()
        self.user.add(get_unique_name, name, mobile, 1)
        assert self.user.update(get_unique_name, new_name).json().get("errcode") == 0
