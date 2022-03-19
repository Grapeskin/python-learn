#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/3/19 17:02
"""
import time
from multiprocessing import Process

from mqtt_v1 import (
    MqttClientV1,
    Platform,
    RobotCallbackProtocol,
    logger,
    RobotRequestProtocol,
    RequestMsgProtocol,
    SyncMessageCallback,
    SimpleMessageCallback,
    generate_msg_id,
)


def test_sub(callback_topic):
    mqtt_client.sub(RobotCallbackProtocol(callback_topic))


def test_async_sub_on_single_thread(
    request_topic, callback_topic, max_concurrency=10, debug_mode=False
):
    while max_concurrency > 0:
        payload = get_payload()
        mqtt_client.async_pub(
            RobotRequestProtocol(
                request_topic,
                RequestMsgProtocol(payload),
            ),
            RobotCallbackProtocol(
                callback_topic, SimpleMessageCallback(debug_mode=debug_mode)
            ),
        )
        max_concurrency = max_concurrency - 1


def async_pub(client, request_topic, callback_topic, debug_mode=False):
    payload = get_payload()
    client.async_pub(
        RobotRequestProtocol(
            request_topic,
            RequestMsgProtocol(payload),
        ),
        RobotCallbackProtocol(
            callback_topic, SimpleMessageCallback(debug_mode=debug_mode)
        ),
    )


def test_async_sub_on_multi_process(
    request_topic, callback_topic, max_concurrency=10, debug_mode=False
):
    while max_concurrency > 0:
        Process(
            target=async_pub,
            args=(mqtt_client, request_topic, callback_topic, debug_mode),
        ).run()
        max_concurrency = max_concurrency - 1


def test_sync_pub_on_single_thread(
    request_topic, callback_topic, timeout, max_concurrency=10, debug_mode=False
):
    while max_concurrency > 0:
        payload = get_payload()
        res = mqtt_client.sync_pub(
            RobotRequestProtocol(request_topic, RequestMsgProtocol(payload)),
            RobotCallbackProtocol(
                callback_topic, SyncMessageCallback(debug_mode=debug_mode)
            ),
            timeout=timeout,
        )
        logger.info(f"Sync request result. [result={res}]")
        max_concurrency = max_concurrency - 1


def sync_pub(client, request_topic, callback_topic, timeout, debug_mode):
    payload = get_payload()
    res = client.sync_pub(
        RobotRequestProtocol(request_topic, RequestMsgProtocol(payload)),
        RobotCallbackProtocol(
            callback_topic, SyncMessageCallback(debug_mode=debug_mode)
        ),
        timeout=timeout,
    )
    logger.info(f"Sync request result. [result={res}]")


def get_payload():
    payload = {
        "msg_id": generate_msg_id(),
        "type": "service",
        "id": "Carrier.SetPWM",
        "timestamp": int(time.time()),
        "data": '{"PwmL":-4000,"PwmR":-4000}',
    }
    return payload


def test_sync_pub_on_multi_process(
    request_topic, callback_topic, timeout, max_concurrency=10, debug_mode=False
):
    while max_concurrency > 0:
        Process(
            target=sync_pub,
            args=(mqtt_client, request_topic, callback_topic, timeout, debug_mode),
        ).run()
        max_concurrency = max_concurrency - 1


def block_main_thread():
    while 1:
        time.sleep(1)


if __name__ == "__main__":
    mqtt_client = MqttClientV1(
        platform=Platform.DETECTION_NODE,
        host="localhost",
        port=1883,
        username="debug",
        password="12345678",
    )
    """
    使用规则引擎模拟响应，规则如下：
    SELECT
      topic as topic,
      replace(topic, 'request', 'response') as res_topic,
      payload.id as id,
      payload.msg_id as msg_id,
      payload.data as data,
      payload.type as type,
      payload.timestamp as timestamp
    FROM
      "/dev/robot/+/service/request"


    重新发布至 -> ${res_topic}：
    {
      "msg_id": "${msg_id}",
      "type": "${type}",
      "id": "${id}",
      "timestamp": ${timestamp},
      "data": "{\"Result\": true}"
    }
    """

    req_topic = "/dev/robot/123/service/request"
    call_topic = "/dev/robot/123/service/response"
    timeout_sec = 2
    concurrency = 500
    debug = True

    # test sub
    # test_sub(call_topic)

    # test async pub
    test_async_sub_on_single_thread(req_topic, call_topic, concurrency, debug)
    # test_async_sub_on_multi_process(req_topic, call_topic, concurrency, debug)

    # test sync pub
    # test_sync_pub_on_single_thread(req_topic, call_topic, timeout_sec, concurrency, debug)
    # test_sync_pub_on_multi_process(req_topic, call_topic, timeout_sec, concurrency, debug)

    block_main_thread()
