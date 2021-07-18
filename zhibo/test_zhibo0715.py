# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 21:19
# @Author  : wkRonin
# @File    :test_zhibo0715.py
import requests

corpid = "wwc71c43dfb2ba3f16"
corpsecret = "nuTI08otYivePm7enI9RkBFzEkwQIdwdieu-i39Qvt4"
url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
r = requests.get(url)
access_token = r.json().get("access_token")
print(access_token)
# 添加的标签json体
tag_add_json = {
   "tagname": "通讯录标签2"
}
# 添加标签
tag_add = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={access_token}", json=tag_add_json)
print(tag_add.json())
# 查询标签
tag_search = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={access_token}")
print(tag_search.json())


