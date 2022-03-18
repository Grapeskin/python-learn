#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/17 20:44
@Author  :   JiaYou
"""
import json
from json import JSONDecodeError

from paho.mqtt.client import MQTTMessage

from mqtt_sdk.exception import DataFormatError
from mqtt_sdk.logger import logger


class MsgProtocol:
    def __init__(self, msg_id: str):
        self.msg_id = msg_id

    def to_json(self):
        raise NotImplementedError


class RequestMsgProtocol(MsgProtocol):

    def __init__(self, params: dict = None):
        if params is None:
            params = {}
        super().__init__(params.get('msg_id'))
        self.id = params.get('id')
        self.timestamp = params.get('timestamp')
        self.type = params.get('type')
        self.data = params.get('data')

    def to_json(self):
        return json.dumps({
            'id': self.id,
            'msg_id': self.msg_id,
            'timestamp': self.timestamp,
            'type': self.type,
            'data': self.data
        })


class ResponseMsgProtocol(MsgProtocol):
    def __init__(self, params: dict = None):
        if params is None:
            params = {}
        super().__init__(params.get('msg_id'))
        self.id = params.get('id')
        self.msg_id = params.get('msg_id')
        self.timestamp = params.get('timestamp')
        self.type = params.get('type')
        self.data = params.get('data')

    def to_json(self):
        return json.dumps({
            'id': self.id,
            'msg_id': self.msg_id,
            'timestamp': self.timestamp,
            'type': self.type,
            'data': self.data
        })


class SyncStatus:
    _REQ_STATUS = {}


class MessageCallback:
    msg_protocol = None

    def __init__(self, response_msg_protocol: MsgProtocol):
        MessageCallback.msg_protocol = response_msg_protocol

    @classmethod
    def on_message(cls, client, userdata, message: MQTTMessage):
        raise NotImplementedError

    @staticmethod
    def log_message(message: MQTTMessage):
        logger.info(f"Receive message {message.topic} {message.payload.decode('utf-8')}")


class SimpleMessageCallback(MessageCallback):
    def __init__(self, response_msg_protocol: MsgProtocol = ResponseMsgProtocol()):
        super(SimpleMessageCallback, self).__init__(response_msg_protocol)

    @classmethod
    def on_message(cls, client, userdata, message: MQTTMessage):
        """It's a simple on message callback."""
        cls.log_message(message)


class SyncMessageCallback(MessageCallback, SyncStatus):
    def __init__(self, response_msg_protocol: MsgProtocol = ResponseMsgProtocol()):
        super(SyncMessageCallback, self).__init__(response_msg_protocol)

    @classmethod
    def on_message(cls, client, userdata, message: MQTTMessage):
        """"""
        cls.log_message(message)
        payload = message.payload.decode('utf-8')
        try:
            cls.msg_protocol.__init__(json.loads(payload))
        except JSONDecodeError:
            raise DataFormatError()
        if cls._REQ_STATUS.get(cls.msg_protocol.msg_id) is None:
            cls._REQ_STATUS[cls.msg_protocol.msg_id] = cls.msg_protocol.to_json()


class RequestProtocol:
    def __init__(self, topic: str, request_msg: MsgProtocol = RequestMsgProtocol(), qos: int = 0, retain: bool = False):
        self.topic = topic
        self.request_msg = request_msg
        self.qos = qos
        self.retain = retain


class CallbackProtocol:
    def __init__(self, topic: str, callback_class: MessageCallback = SimpleMessageCallback(), qos: int = 0):
        self.topic = topic
        self.callback_class = callback_class
        self.qos = qos


class RobotRequestProtocol(RequestProtocol):
    def __init__(self, topic: str, request_msg: MsgProtocol = RequestMsgProtocol(), qos: int = 0, retain: bool = False):
        super().__init__(topic, request_msg, qos, retain)


class RobotCallbackProtocol(CallbackProtocol):
    def __init__(self, topic: str, callback_class: MessageCallback = SimpleMessageCallback(), qos: int = 0):
        super().__init__(topic, callback_class, qos)
