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

# python 多线程到底是不是鸡肋
# GIL node.js 单进程， 单线程
# 10 线程 非常严重的依赖CPU计算，CPU密集型程序（代码计算：视频解码、圆周率计算）
# IO密集型程序 查询数据库、 请求网络资源、读写文件

# python 多线程 在IO密集型 是有意义的。
# python 多线程 不适合CPU密集型的程序。


# print('i am kingdom')
t = threading.currentThread()
print(t.getName())

# 主线程
