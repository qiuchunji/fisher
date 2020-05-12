#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
# sqlalchemy
# Flask_SQLAlchemy
# WTFORMS
# Flask_WTFORMS

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    isbn = Column(String(15), nullable=False, unique=True)
    price = Column(String(20))
    binding = Column(String(20))
    publisher = Column(String(50))
    pages = Column(Integer)
    pubdate = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))

    # MVC M Model 只有数据 = 数据表
    # 业务逻辑应该写在 MVC 里的 Model层。
    # ORM 对象关系映射 和 Code First 有什么区别
    # Code First 关心数据表是怎么创建
    # ORM 通过操作数据模型来间接操作数据库 - 更为广阔（数据创建、查询、更新...）

