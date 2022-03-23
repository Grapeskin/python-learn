#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2021/12/14 17:41
@Author  :   JiaYou
"""
import logging

from paho.mqtt import client as cli
from paho.mqtt.client import Client, MQTTMessage


def on_connect(client: Client, userdata, flags, rc):
    """

    Args:
        client: the client instance for this callback.
        userdata: the private user data as set in Client() or user_data_set().
        flags: response flags sent by the broker.
        rc: 0: Connection successful
            1: Connection refused - incorrect protocol version
            2: Connection refused - invalid client identifier
            3: Connection refused - server unavailable
            4: Connection refused - bad username or password
            5: Connection refused - not authorised
            6-255: Currently unused.
    """

    logging.debug(
        msg=f"Connection returned result: {rc}, client_id = [{client._client_id}]"
    )


def on_message(client: Client, userdata, message: MQTTMessage):
    """

    Args:
        client: the client instance for this callback.
        userdata: the private user data as set in Client() or user_data_set().
        message: an instance of MQTTMessage.
    """
    logging.debug(
        msg="Received message. [topic={message.topic}, qos={message.qos}, payload={message.payload}]"
    )


def on_subscribe(client: Client, userdata, mid, granted_qos):
    """

    Args:
        client: the client instance for this callback.
        userdata: the private user data as set in Client() or user_data_set().
        mid: 变量匹配从相应的subscribe()调用返回的mid变量
        granted_qos: 变量是一个整数列表，它给出了代理为每个不同的订阅请求授予的QoS级别
    """
    logging.debug(f"Subscribe successfully. client_id = {client._client_id}")


def on_publish(client: Client, userdata, mid):
    """
    Called when a message that was to be sent using the publish() call has completed transmission to the broker.
    For messages with QoS levels 1 and 2, this means that the appropriate handshakes have completed.
    For QoS 0, this simply means that the message has left the client.
    This callback is important because even if the publish() call returns success, it does not always mean that the message has been sent.

    Args:
        client: the client instance for this callback.
        userdata: the private user data as set in Client() or user_data_set().
        mid: 变量匹配从相应的publish()调用返回的mid变量，以允许跟踪传出的消息。
    """
    logging.debug(f"Publish successfully. client_id = {client._client_id}.")


class CustomMqttClient(object):
    def __init__(
        self,
        client_id,
        on_message_callback,
        host: str = "localhost",
        port: int = 1883,
        **kwargs,
    ):
        """
        获取一个MQTT连接. 参考文档：https://pypi.org/project/paho-mqtt
        Args:
            client_id: 连接标识
            host: MQTT Broker. example: localhost
            port: 端口. example: 1883
            **kwargs: MQTT 扩展连接参数
        """
        self._mqtt_client = cli.Client(client_id=client_id)

        self._mqtt_client.on_disconnect = self.on_disconnect
        self._mqtt_client.on_connect = on_connect
        self._mqtt_client.on_message = (
            on_message_callback if on_message_callback else on_message
        )
        self._mqtt_client.on_subscribe = on_subscribe
        self._mqtt_client.on_publish = on_publish
        if not self._mqtt_client.is_connected():
            # self._mqtt_client.username_pw_set("debug", "12345678")
            self._mqtt_client.connect(host=host, port=port, **kwargs)
            self._mqtt_client.loop_start()

    def get_client_instance(self) -> Client:
        return self._mqtt_client

    def on_disconnect(self, client: Client, userdata, rc):
        """

        Args:
            client: the client instance for this callback.
            userdata: the private user data as set in Client() or user_data_set().
            rc: 0: the callback was called in response to a disconnect() call.
                other: might be caused by a network error.
        """
        if rc != 0:
            logging.warning(msg=f"Unexpected disconnection. {rc=}")
        self._mqtt_client.loop_stop()
