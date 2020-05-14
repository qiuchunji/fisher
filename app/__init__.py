#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    # print('id为 ' + str(id(app)) + '的app实例化')
    # app.config.from_object('config')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_buleprint(app)

    db.init_app(app)  # init_app 没有保存传进来的app对象
    with app.app_context():
        db.create_all()
    return app


def register_buleprint(app):
    from app.web.book import web
    app.register_blueprint(web)
