#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2022/3/16 15:55
@Author  :   JiaYou
"""
import time

from paho.mqtt.client import Client, MQTTMessageInfo

from .enums import Platform
from .exception import ParamError, SyncTimeoutError
from .interface import SubInterface, AsyncPubInterface, SyncPubInterface
from .logger import logger
from .protocol import (
    CallbackProtocol,
    RequestProtocol,
    MsgProtocol,
    MessageCallback,
)
from .utils import generate_client_id


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

    logger.info(
        msg=f"Connection created. [client_id = {userdata} flags={flags}, rc={rc}.]"
    )


def on_disconnect(client: Client, userdata, rc):
    """

    Args:
        client: the client instance for this callback.
        userdata: the private user data as set in Client() or user_data_set().
        rc: 0: the callback was called in response to a disconnect() call.
            other: might be caused by a network error.
    """

    logger.info(msg=f"Connection disconnected. [client_id = {userdata}, rc={rc}.")


class MqttClientV1(SubInterface, AsyncPubInterface, SyncPubInterface):
    """
    V1 version mqtt client sdk
    """

    def __init__(
        self,
        platform: Platform,
        host: str,
        client_id: str = "",
        port: int = 1883,
        keepalive: int = 60,
        username: str = None,
        password: str = None,
    ):
        if not all([platform, host]):
            raise ParamError()
        if not client_id:
            client_id = generate_client_id(platform)

        self._client = Client(
            client_id=client_id, clean_session=True, userdata=client_id
        )

        self._client.on_connect = on_connect
        self._client.on_disconnect = on_disconnect

        if any([username, password]):
            self._client.username_pw_set(username, password)
        if not self._client.is_connected():
            self._client.connect(host=host, port=port, keepalive=keepalive)
        self._client.loop_start()

    def sub(self, callback_protocol: CallbackProtocol):
        if not all([callback_protocol.topic, callback_protocol.callback_class]):
            raise ParamError()
        self._client.subscribe(callback_protocol.topic, callback_protocol.qos)
        self._client.message_callback_add(
            callback_protocol.topic, callback_protocol.callback_class.on_message
        )

    def sync_pub(
        self,
        request_protocol: RequestProtocol,
        callback_protocol: CallbackProtocol,
        timeout: int = 2,
    ) -> str:
        if not request_protocol.topic:
            raise ParamError()
        if not isinstance(request_protocol.payload, MsgProtocol):
            raise ParamError()
        start = time.time()
        msg_id = request_protocol.payload.msg_id
        self._REQ_STATUS[msg_id] = None
        self._client.subscribe(callback_protocol.topic, callback_protocol.qos)
        self._client.message_callback_add(
            callback_protocol.topic, callback_protocol.callback_class.on_message
        )
        pub_res: MQTTMessageInfo = self._client.publish(
            request_protocol.topic,
            request_protocol.payload.to_json(),
            request_protocol.qos,
            request_protocol.retain,
        )
        logger.info(
            f"Publish message. req_info=[msg_id={msg_id}],res_info=[rc={pub_res.rc}, mid={pub_res.mid}]"
        )
        while time.time() - start <= timeout and self._REQ_STATUS.get(msg_id) is None:
            time.sleep(0.1)
        if msg_id in self._REQ_STATUS.keys() and self._REQ_STATUS.get(msg_id) is None:
            raise SyncTimeoutError()
        self._client.unsubscribe(callback_protocol.topic)
        return self._REQ_STATUS.pop(msg_id)

    def async_pub(
        self, request_protocol: RequestProtocol, callback_protocol: CallbackProtocol
    ):
        if not request_protocol.topic:
            raise ParamError()
        if not isinstance(callback_protocol.callback_class, MessageCallback):
            raise ParamError()

        if callback_protocol.callback_class:
            self._client.subscribe(callback_protocol.topic, callback_protocol.qos)
            self._client.message_callback_add(
                callback_protocol.topic, callback_protocol.callback_class.on_message
            )
        pub_res: MQTTMessageInfo = self._client.publish(
            request_protocol.topic,
            request_protocol.payload.to_json(),
            request_protocol.qos,
            request_protocol.retain,
        )
        msg_id = request_protocol.payload.msg_id
        logger.info(
            f"Publish message. req_info=[msg_id={msg_id}],res_info=[rc={pub_res.rc}, mid={pub_res.mid}]"
        )
