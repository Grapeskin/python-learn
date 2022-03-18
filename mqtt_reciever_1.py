#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/11 15:54
@Author  :   JiaYou
"""
import logging
import time

from paho.mqtt.client import Client, MQTTMessage

from custom_mqtt import CustomMqttClient


def on_message(client: Client, userdata, message: MQTTMessage):
    print(message.payload.decode('utf-8'))
    time.sleep(1)


mqtt = CustomMqttClient(client_id='mqttx_1086d3e', on_message_callback=on_message, host='localhost',
                        port=1883).get_client_instance()
mqtt.subscribe(topic='/test', qos=0)

while True:
    time.sleep(1)
