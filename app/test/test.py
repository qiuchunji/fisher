#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, request, Request


app = Flask(__name__)


# 应用上下文  对象  Flask 封装
# 请求上下文  对象  Request 封装
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with 主要对资源的管理。
"""
例：数据管理
1. 连接数据
2. sql
3. 释放资源
__enter__
__exit__
"""

# 文件的读写
# try:
#     f = open(r'./t.text')
#     print(f.read())
# finally:
#     f.close()
#
# with open(r'./t.txt') as f:
#     print(f.read())


with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']


# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__  __exit__
# 上下文表达式必须返回一个上下文管理器

# class A:
#     def __enter__(self):
#         a = 1
#
#     def __exit__(self):
#         b = 2
#
#
# with A() as obj_A:
#     pass
