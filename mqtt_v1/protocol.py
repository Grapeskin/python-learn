#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2022/3/17 20:44
@Author  :   JiaYou
"""
import json
from json import JSONDecodeError

from paho.mqtt.client import MQTTMessage

from mqtt_v1.exception import DataFormatError
from mqtt_v1.logger import logger


class MsgProtocol:
    def __init__(self, msg_id: str):
        self.msg_id = msg_id

    def to_json(self):
        raise NotImplementedError


class RequestMsgProtocol(MsgProtocol):
    def __init__(self, params: dict = None):
        if params is None:
            params = {}
        super().__init__(params.get("msg_id"))
        self.id = params.get("id")
        self.timestamp = params.get("timestamp")
        self.type = params.get("type")
        self.data = params.get("data")

    def to_json(self):
        return json.dumps(
            {
                "id": self.id,
                "msg_id": self.msg_id,
                "timestamp": self.timestamp,
                "type": self.type,
                "data": self.data,
            }
        )


class ResponseMsgProtocol(MsgProtocol):
    def __init__(self, params: dict = None):
        if params is None:
            params = {}
        super().__init__(params.get("msg_id"))
        self.id = params.get("id")
        self.msg_id = params.get("msg_id")
        self.timestamp = params.get("timestamp")
        self.type = params.get("type")
        self.data = params.get("data")

    def to_json(self):
        return json.dumps(
            {
                "id": self.id,
                "msg_id": self.msg_id,
                "timestamp": self.timestamp,
                "type": self.type,
                "data": self.data,
            }
        )


class SyncStatus:
    _REQ_STATUS = {}


class MessageCallback:
    receive_count = 0

    def __init__(self, response_msg_protocol: MsgProtocol):
        self.msg_protocol = response_msg_protocol
        self.debug_mode = False

    def on_message(self, client, userdata, message: MQTTMessage):
        raise NotImplementedError

    @staticmethod
    def log_message(message: MQTTMessage):
        logger.info(
            f"Receive message {message.topic} {message.payload.decode('utf-8')}"
        )

    @staticmethod
    def count_receive_msg():
        MessageCallback.receive_count = MessageCallback.receive_count + 1
        logger.info(f"Receive msg count={MessageCallback.receive_count}")


class SimpleMessageCallback(MessageCallback):
    def __init__(
        self,
        response_msg_protocol: MsgProtocol = ResponseMsgProtocol(),
        debug_mode=False,
    ):
        super(SimpleMessageCallback, self).__init__(response_msg_protocol)
        self.debug_mode = debug_mode

    def on_message(self, client, userdata, message: MQTTMessage):
        """It's a simple on message callback."""

        self.log_message(message)
        if self.debug_mode:
            self.count_receive_msg()


class SyncMessageCallback(MessageCallback, SyncStatus):
    def __init__(
        self,
        response_msg_protocol: MsgProtocol = ResponseMsgProtocol(),
        debug_mode=False,
    ):
        super(SyncMessageCallback, self).__init__(response_msg_protocol)
        self.debug_mode = debug_mode

    def on_message(self, client, userdata, message: MQTTMessage):
        self.log_message(message)
        payload = message.payload.decode("utf-8")
        try:
            self.msg_protocol.__init__(json.loads(payload))
        except JSONDecodeError:
            raise DataFormatError()
        if self._REQ_STATUS.get(self.msg_protocol.msg_id) is None:
            self._REQ_STATUS[self.msg_protocol.msg_id] = self.msg_protocol.to_json()
            if self.debug_mode:
                self.count_receive_msg()


class RequestProtocol:
    def __init__(
        self,
        topic: str,
        payload: MsgProtocol = RequestMsgProtocol(),
        qos: int = 0,
        retain: bool = False,
    ):
        self.topic = topic
        self.payload = payload
        self.qos = qos
        self.retain = retain


class CallbackProtocol:
    def __init__(
        self,
        topic: str,
        callback_class: MessageCallback = SimpleMessageCallback(),
        qos: int = 0,
    ):
        self.topic = topic
        self.callback_class = callback_class
        self.qos = qos


class RobotRequestProtocol(RequestProtocol):
    def __init__(
        self,
        topic: str,
        payload: MsgProtocol = RequestMsgProtocol(),
        qos: int = 0,
        retain: bool = False,
    ):
        super().__init__(topic, payload, qos, retain)


class RobotCallbackProtocol(CallbackProtocol):
    def __init__(
        self,
        topic: str,
        callback_class: MessageCallback = SimpleMessageCallback(),
        qos: int = 0,
    ):
        super().__init__(topic, callback_class, qos)
