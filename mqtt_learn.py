#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/3/16 17:42
"""
import json
import time

from paho.mqtt.client import Client, MQTTMessage
from paho.mqtt.publish import single


def message_callback(cli, userdata, message: MQTTMessage):
    print(userdata)
    print(message.payload.decode("utf-8"))


class B:
    def __init__(self, id):
        self.id = id


class A:
    b = None

    def __init__(self, param, b=B("1")):
        self.a = param
        self.b = b


if __name__ == "__main__":
    a = A({})
    print(a.b.id)
    a.__init__({"k": "v"})
    print(a.b.id)
    # client = Client(client_id="test", userdata={'k': 'v'})
    # client.user_data_set(11)
    # client.connect(host='localhost', port=1883)
    # client.subscribe(topic='/test')
    # client.loop_start()
    # client.on_message = message_callback
    # client.loop_forever()
    # client.loop_stop()
    #
    i = 0
    while True:
        time.sleep(0.1)
        i += 1
