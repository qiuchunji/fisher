#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, request, Request


app = Flask(__name__)


# 应用上下文  对象  Flask 封装
# 请求上下文  对象  Request 封装
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试
ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']
ctx.pop()
