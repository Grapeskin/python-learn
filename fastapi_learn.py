#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/1/16 22:36
"""
import time
from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form, File, UploadFile
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, HttpUrl
from starlette import status
from starlette.exceptions import HTTPException as StarletteHTTPException, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

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


@app.get("/items/{item_id}", deprecated=True)
def read_item(item_id: int = Path(..., title='this is item id'),
              q: Optional[List[str]] = Query(default=['abc', 'def', 'fff'], min_length=3, max_length=5)):
    if item_id not in [1, 2]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found', headers={'k': 'v'})
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}", tags=['items'])
def update_item(
        item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.post("/items/{item_id}", tags=['items'],
          summary="Create an item",
          response_description='test response message'
          )
def update_item(item_id: int, item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
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


@app.post("/user/", response_model=UserOut, status_code=status.HTTP_200_OK)
def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved


@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}


@app.post("/files/")
def create_file(file: List[bytes] = File(...)):
    return [{"file_size": len(file)} for item in file]


@app.post("/uploadfile/")
def create_upload_file(file: List[UploadFile] = File(...)):
    return [{"filename": item.filename, "content_type": item.content_type} for item in file]


@app.post("/files/form")
def create_file(
        file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow... {str(exc)}"},
    )


"""该异常必须要是异步操作"""


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)


"""该异常必须要是异步操作"""


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)


@app.get("/unicorns/{name}")
def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    if name == "youge":
        # will raise ValidationError on code. but on user is Internal Server Error response
        temp = 1 / 0
    if name == "hello":
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"unicorn_name": name}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    print(response)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == '__main__':
    """fast api 使用
    1. 
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
