#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/9/18 21:12
"""

import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:5555")

while True:
    #  Wait for next request from client
    topic = socket.recv()
    # message = socket.recv()
    print(f"Received request: {message} from topic: {topic}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"/word")
    socket.send(b"World")
