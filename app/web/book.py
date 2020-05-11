#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify, request
from app.forms.book import SearchForm
from . import web
from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


# print('id为 ' + str(id(web)) + '的app注册路由')


@web.route('/book/search')
def search():
    """
        q: 普通关键字 isbn
        page:
        ?q=金庸&page=1
    """
    # q = request.args['q']
    # page = request.args['page']
    # a = request.args.to_dict()   # 调用此方法是将不可变的字典转成常见的可变字典。
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
        # return json.dumps(result), 200, {'content-type': 'application/json'}
    else:
        return jsonify(form.errors)
