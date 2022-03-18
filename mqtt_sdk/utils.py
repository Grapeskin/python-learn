#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/17 15:32
@Author  :   JiaYou
"""
import uuid

from mqtt_sdk.enums import Platform


def generate_client_id(platform: Platform):
    return f"{platform.value}_{str(uuid.uuid4()).replace('-', '')}"


def generate_msg_id() -> str:
    # TODO 唯一ID算法实现
    return str(uuid.uuid4()).replace('-', '')
