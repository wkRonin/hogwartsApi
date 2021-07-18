# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 16:03
# @Author  : wkRonin
# @File    :test_tag.py

from zhibo.api.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def test_get(self):
        r = self.tag.get().json()
        assert r.get('errcode') == 0

    def test_add(self, get_unique_name):
        new_tag = self.tag.add(get_unique_name).json()
        assert new_tag.get('errcode') == 0
        assert self.tag.is_in_taglist(new_tag.get("tagid"))

    def test_delete(self, get_unique_name):
        new_tag = self.tag.add(get_unique_name).json()
        assert self.tag.delete(new_tag.get("tagid")).json().get("errcode") == 0

    def test_update(self, get_unique_name):
        new_tag = self.tag.add(get_unique_name).json()
        assert self.tag.update(new_tag.get("tagid"), get_unique_name).json().get("errcode") == 0
