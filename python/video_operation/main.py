#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/5/8 21:22
"""
import re

import requests
from you_get import common

if __name__ == "__main__":
    urls = ["https://v.kuaishou.com/k0BAhi"]
    payload = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Cookie": "clientid=3; did=web_43c22563da6c2789e316930f5aeb3891; kpf=PC_WEB; kpn=KUAISHOU_VISION",
        "Accept": "*/*",
    }

    for url in urls:
        redirect = requests.get(url, headers=headers)
        print(f"redirect.url={redirect.url}")
        for cookie in redirect.cookies.items():
            print(f"cookie {cookie}")
        res = requests.get(redirect.url, headers=headers)
        print(f"{res.headers=}")
        print(f"{res.text=}")
        video_url = (
            re.findall('"photoUrl":"(.*?)"', res.text)[0]
            .encode("utf-8")
            .decode("unicode-escape")
        )
        print(video_url)
        common.any_download(url=video_url)
