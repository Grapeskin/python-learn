#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/16 15:55
@Author  :   JiaYou
"""
import time

from paho.mqtt.client import Client, MQTTMessageInfo

from mqtt_v1.enums import Platform
from mqtt_v1.exception import ParamError, SyncTimeoutError
from mqtt_v1.interface import SubInterface, AsyncPubInterface, SyncPubInterface
from mqtt_v1.logger import logger
from mqtt_v1.protocol import CallbackProtocol, RequestProtocol, MsgProtocol, MessageCallback, RobotRequestProtocol, \
    RobotCallbackProtocol, RequestMsgProtocol, SyncMessageCallback
from mqtt_v1.utils import generate_client_id, generate_msg_id


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

    logger.info(msg=f"Connection disconnect. [client_id = {userdata}, rc={rc}.")


class MqttClientV1(SubInterface, AsyncPubInterface, SyncPubInterface):
    """
    V1 version mqtt client sdk
    """

    def __init__(self, platform: Platform, client_id: str, host: str, port: int = 1883, keepalive: int = 60,
                 username: str = None, password: str = None):
        if not all([platform, host]):
            raise ParamError()
        if not client_id:
            client_id = generate_client_id(platform)

        self._client = Client(client_id=client_id, clean_session=True, userdata=client_id)

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
        self._client.message_callback_add(callback_protocol.topic, callback_protocol.callback_class.on_message)

    def sync_pub(self, request_protocol: RequestProtocol, callback_protocol: CallbackProtocol, timeout: int = 2) -> str:

        if not request_protocol.topic:
            raise ParamError()
        if not isinstance(request_protocol.request_msg, MsgProtocol):
            raise ParamError()
        start = time.time()
        msg_id = request_protocol.request_msg.msg_id
        self._REQ_STATUS[msg_id] = None
        pub_res: MQTTMessageInfo = self._client.publish(request_protocol.topic,
                                                        request_protocol.request_msg.to_json(),
                                                        request_protocol.qos, request_protocol.retain)
        logger.info(f'Publish message. req_info=[msg_id={msg_id}],res_info=[rc={pub_res.rc}, mid={pub_res.mid}]')
        self._client.subscribe(callback_protocol.topic, callback_protocol.qos)
        self._client.message_callback_add(callback_protocol.topic, callback_protocol.callback_class.on_message)
        while time.time() - start <= timeout and self._REQ_STATUS.get(msg_id) is None:
            time.sleep(0.1)
        if msg_id in self._REQ_STATUS.keys() and self._REQ_STATUS.get(msg_id) is None:
            raise SyncTimeoutError()
        return self._REQ_STATUS.pop(msg_id)

    def async_pub(self, request_protocol: RequestProtocol, callback_protocol: CallbackProtocol):

        if not request_protocol.topic:
            raise ParamError()
        if not isinstance(callback_protocol.callback_class, MessageCallback):
            raise ParamError()

        if callback_protocol.callback_class:
            self._client.subscribe(callback_protocol.topic, callback_protocol.qos)
            self._client.message_callback_add(callback_protocol.topic, callback_protocol.callback_class.on_message)
        pub_res = self._client.publish(request_protocol.topic,
                                       request_protocol.request_msg.to_json(),
                                       request_protocol.qos,
                                       request_protocol.retain)
        logger.info(
            f'Publish message. req_info=[msg_id={request_protocol.request_msg.msg_id}],res_info=[rc={pub_res.rc}, mid={pub_res.mid}]')


if __name__ == '__main__':
    mqtt_client = MqttClientV1(platform=Platform.DETECTION_NODE, client_id='', host='192.168.160.45', port=2883,
                               username='debug', password='12345678')

    # test sub
    mqtt_client.sub(RobotCallbackProtocol('/dev/robot/123/service/response'))

    payload = {
        "msg_id": generate_msg_id(),
        "type": "service",
        "id": "Carrier.SetPWM",
        "timestamp": int(time.time()),
        "data": "{\"PwmL\":-4000,\"PwmR\":-4000}"
    }
    # test async pub
    # mqtt_client.async_pub(
    #     RobotRequestProtocol(topic='/dev/robot/123/service/request', request_msg=RequestMsgProtocol(payload)),
    #     RobotCallbackProtocol(topic='/dev/robot/123/service/response')
    # )

    # test sync pub
    # res = mqtt_client.sync_pub(
    #     RobotRequestProtocol(
    #         '/dev/robot/123/service/request', RequestMsgProtocol(payload))
    #     ,
    #     RobotCallbackProtocol(
    #         '/dev/robot/123/service/response', SyncMessageCallback()
    #     ),
    #     timeout=10
    # )
    # logger.info(f'Sync request result. [result={res}]')
    while 1:
        time.sleep(1)
