#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/17 15:42
@Author  :   JiaYou
"""


class BusinessException(Exception):
    pass


class ParamError(BusinessException):
    def __init__(self):
        super(ParamError, self).__init__(f"Parameter error.")


class SyncTimeoutError(BusinessException):
    def __init__(self):
        super(SyncTimeoutError, self).__init__(f"Sync event request timeout.")


class DataFormatError(BusinessException):
    def __init__(self):
        super(DataFormatError, self).__init__(f"Sync event response format error.")
