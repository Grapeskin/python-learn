#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/11 15:54
@Author  :   JiaYou
"""
import logging

from paho.mqtt.client import Client, MQTTMessage

from custom_mqtt import CustomMqttClient


def on_message(client: Client, userdata, message: MQTTMessage):
    logging.info(message.payload.decode('utf-8'))


mqtt = CustomMqttClient(client_id='reciever_2', on_message_callback=on_message, host='127.0.0.1', port=1883)
mqtt.get_client_instance().loop_forever()
