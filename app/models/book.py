#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String

# sqlalchemy
# Flask_SQLAlchemy
# WTFORMS
# Flask_WTFORMS


class Book():
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

