#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2022/3/18 14:15
@Author  :   JiaYou
"""
import logging
from sys import stdout

_formatter = logging.Formatter(
    "%(levelname)s %(asctime)s %(filename)s[line:%(lineno)d] %(message)s"
)
logger = logging.root
logger.name = "autopack_mqtt"
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(stdout)
stdout_handler.setFormatter(_formatter)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)
