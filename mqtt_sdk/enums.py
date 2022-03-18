#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/17 15:33
@Author  :   JiaYou
"""

from enum import unique, Enum


@unique
class Platform(Enum):
    DEVICE = 'device'
    ENGINE = 'engine'
    WEB = 'web'
    DETECTION_NODE = 'detection_node'
    AUTO_TEST = 'auto_test'


@unique
class EventType(Enum):
    NULL_STR = ""
    EVENT = "event"
    SERVICE = "service"


@unique
class EventId(Enum):
    NULL_STR = ""
    GetDeviceInfo = "GetDeviceInfo"
