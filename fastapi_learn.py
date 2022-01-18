#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/1/16 22:36
"""
from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str = Field(
        None, title="The description of the item", max_length=5
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    is_offer: Optional[bool] = None
    images: Optional[List[Image]] = None

    # 示例参数
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "is_offer": False,
                "price": 1.5
            }
        }


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


"""
显式声明路径放前面，匹配路径放后面！！
"""


@app.get("/items/cookie")
def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


@app.get("/items/header")
def read_items(x_token: Optional[List[str]] = Header(None)):
    # Header 将把参数名称的字符从下划线 (_) 转换为连字符 (-) 来提取并记录 headers.
    return {"X-Token values": x_token}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title='this is item id'),
              q: Optional[List[str]] = Query(default=['abc', 'def', 'fff'], min_length=3, max_length=5)):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(
        item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item": item, "item_id": item_id}


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: str
    full_name: Optional[str] = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved


if __name__ == '__main__':
    """fast api 使用
    1. 
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
