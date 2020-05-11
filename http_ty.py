#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


# url = 'http://t.yushu.im/v2/isbn/9787501524044'


# urllib
# requests
class HTTP:
    # 经典类和新式类
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

