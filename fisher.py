#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from app import create_app

app = create_app()


if __name__ == '__main__':
    # print('id为 ' + str(id(app)) + '的启动')
    # 生产环境 nginx + uwsgi
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])


#  基地址： http://t.yushu.im
#  关键字搜索:  http://t.yushu.im/v2/book/search?/q={}&start={}&count={}
#  isbn搜索:  http://t.yushu.im/v2/book/isbn/{isbn}
#  豆瓣API:  https://api.douban.com/v2/book

# @app.route('/hello')    # 装饰器注册路由
# def hello():
#     # status code
#     # content-type http headers
#     # content-type = text/html, 默认值
#     # Response 方法1创建 response对象
#     headers = {
#         'content-type': 'application/json',
#         'location': 'http://www.bing.com'
#     }
#     # json
#     # response = make_response('<html></html>', 301)  # http 301重定向
#     # response.headers = headers
#     # return response
#
#     return '<html></html>', 404, headers  # 方法2
#
#
# def helloo():
#     return 'Helloo, World'

# 基于类的视图（即插视图）
# app.add_url_rule('/hello', view_func=hello)  # add_url_rule 来注册路由
