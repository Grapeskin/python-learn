#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/1/14 15:38
@Author  :   JiaYou
"""
import functools
import threading
import time

import uuid

local_ctx = threading.local()


def request_aspect():
    """请求切面"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = int(time.time() * 1000)
            request_id = uuid.uuid4()

            res = func(*args, **kwargs)
            end_time = int(time.time() * 1000)

        return wrapper

    return decorator
