#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def worker():
    print('i am thread')
    t = threading.currentThread()
    time.sleep(8)
    print(t.getName())


new_t = threading.Thread(target=worker, name='t_Thread')
new_t.start()

# 更加充分的利用CPU的性能优势
# 异常编程
# 单核CPU 同一时间只允许一个线程来执行CPU
# 多核 A核 B核 并行的执行程序
# python 不能充分利用多核CPU优势
# GIL 全局解释器锁 global interpreter lock

# 锁 线程安全
# 细粒度锁， 程序员 主动加锁
# 粗粒度锁， 解释器 GIL 多核CPU 1个线程执行 一定程度上保证线程安全


# print('i am kingdom')
t = threading.currentThread()
print(t.getName())

# 主线程
