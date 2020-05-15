#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def worker():
    print('i am thread')
    t = threading.currentThread()
    time.sleep(100)
    print(t.getName())


# print('i am kingdom')
t = threading.currentThread()
print(t.getName())


new_t = threading.Thread(target=worker, name='t_Thread')
new_t.start()
# 主线程
