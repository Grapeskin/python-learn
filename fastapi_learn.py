#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/1/16 22:36
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    """fast api 使用
    1. 
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
