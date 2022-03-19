#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/3/17 10:52
"""
import requests
from example_package.test import http_test


def plus(a, b):
    return a * b


# def http_test():
#     return requests.post('http://www.httpbin.org/post').json()


if __name__ == "__main__":
    print(http_test())
