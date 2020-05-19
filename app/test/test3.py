#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flask 如何使用线程隔离
# 原理 字典 保存数据
# 操作数据
# werkzeug local Local 字典

# {thread_id1:value, thread_id2_value2 ...}
# L 线程隔离的对象
# t1 L.a, t2 L.a
import threading
import time

from werkzeug.local import Local


class A:
    b = 1


# my_obj = A()   # 普通调用
my_obj = Local()  # 使用Local() 实现线程隔离
my_obj.b = 1


def worker():
    # 新线程
    my_obj.b = 2   # 新线程的值影响到主线程的结果，非线程隔离。
    print('in new thread b is:' + str(my_obj.b))


new_t = threading.Thread(target=worker, name='qiu_thread')
new_t.start()
time.sleep(1)

# 主线程
print('in main thread b is:' + str(my_obj.b))
