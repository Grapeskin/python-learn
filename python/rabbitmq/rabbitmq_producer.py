#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/1/23 10:49
"""
import time

import pika

parameters = pika.ConnectionParameters(host="localhost", port=5672)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue="hello")
for i in range(10000):
    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body=bytes(f"Test message [{i}].".encode("utf-8")),
    )
    time.sleep(0.5)

connection.close()
