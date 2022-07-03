#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/7/2 13:48
"""
from typing import List

from pydantic import BaseModel, constr, Field, validator
from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.orm import declarative_base


class Address(BaseModel):
    """地址对象"""

    street: str


class User(BaseModel):
    """user对象"""

    id: int
    name = "Jane Doe"
    address: Address


user = User(id=1, address=Address(street="西乡街道"))
assert user.id == 1
assert user.name == "Jane Doe"
print(user.__fields_set__)
print(user.dict())
print(dict(user))
print(user.json())
print(user.copy())
print(user.parse_obj({"id": 3, "address": {"street": "西丽街道"}}))
print(User.parse_obj({"id": 4, "address": {"street": "西丽街道"}}))

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, nullable=False)
    public = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20) = Field(alias="public")
    name: constr(max_length=63)
    domains: List[constr(max_length=255)]

    @validator("name")
    def value_must_equal_bar(cls, v):
        if v != "bar":
            raise ValueError('value must be "bar"')

        return v

    class Config:
        orm_mode = True


co_orm = CompanyOrm(
    id=123,
    public="foobar",
    name="bar",
    domains=["example.com", "foobar.com"],
)
print(co_orm)

co_model = CompanyModel.from_orm(co_orm)
print(co_model)
