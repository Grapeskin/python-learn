#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/1/23 10:50
"""
import time

import pika

parameters = pika.ConnectionParameters(host="localhost", port=5672)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):  # 四个参数为标准格式
    print("[x]Received %r" % body)
    time.sleep(1)
    # time.sleep(15)

    # ch.basic_ack(delivry_tay=method.delivery_tay)  # 告诉生成者，消息处理完成


channel.basic_consume(  # 消费消息
    on_message_callback=callback,  # 如果收到消息，就调用callback函数来处理消息
    queue="hello",  # 要消费的队列
    auto_ack=True,
)
print("[*]Waiting for messages.To exit press CTRL+C")
channel.start_consuming()  # 开始消费消息
