#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/3/15 12:16
"""
from typing import Optional

import uvicorn
from fastapi import FastAPI, Header, Body
from pydantic import BaseModel

app = FastAPI()

count = 0


class User(BaseModel):
    username: str
    password: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def read_root(token: Optional[str] = Header(...)):
    return {"Hello": "World", "token": token}


@app.post("/login")
def read_item(user: User = Body(...)):
    global count
    count = count + 1
    return {"token": f"token-{count}"}


if __name__ == "__main__":
    """fast api 使用
    1.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
