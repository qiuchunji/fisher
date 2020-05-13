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
    连接数据库
with :  (上下文表达式)
    操作数据库的
__exit__ 
    释放资源
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


# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']


# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__  __exit__
# 上下文表达式必须返回一个上下文管理器

# class MyResource:
#     def __enter__(self):
#         print('connect to resource')
#         return self
#
#     def __exit__(self, exc_type, exc_value, tb):
#         if tb:
#             print('process exception')
#         else:
#             print('no exception')
#         print('close resource connection')
#         return False  # True 不抛出异常, 去掉return 即返回False
#
#     def query(self):
#         print('query data')
#
#
# try:
#     with MyResource() as resource:
#         1/0
#         resource.query()
# except Exception as ex:
#     pass
