#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/5/8 21:22
"""
import requests

if __name__ == "__main__":
    urls = ["https://v.kuaishou.com/k0BAhi"]
    for url in urls:
        res = requests.get(url, headers={"User-Agent": "xx"})
        print(res.url)
