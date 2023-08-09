#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/9/18 21:12
"""
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.102:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"/hello")
    socket.send(b"Hello")

    #  Get the reply.
    topic = socket.recv()
    message = socket.recv()
    print(f"Received reply {topic}, request {request} message {message} %s")
