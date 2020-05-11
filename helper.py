#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_isbn_or_key(word):
    """
    判断是isbn 还是key
    :param word:
    :return:
    """
    # isbn  isbn13 13个0-9的数据组成
    # isbn  10个0-9数据组成，含有一些 ' - '
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
