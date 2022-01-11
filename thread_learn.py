#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2021/12/23 15:16
@Author  :   JiaYou
"""
import threading

local_school = threading.local()


def process_student():
    print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
