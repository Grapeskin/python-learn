# MQTT SDK 通信库
基于MQTT协议的通信库，主要是在MQTT协议的基础上进行了更上层的封装，对外部提供三个接口：订阅、同步请求、异步请求，且对每个接口均可自定义回调处理逻辑。对通信协议进行了一层封装，也可自行扩展新的通信协议。
- 订阅(_SubInterface_)

订阅topic并指定回调处理逻辑，异步非阻塞。

- 同步请求(_SyncPubInterface_)

客户端A发送`msg_id=1`的消息给客户端B，客户端A在超时时间内等待客户端B发送`msg_id=1`的响应消息，同步阻塞。

- 异步请求(_AsyncPubInterface_)

客户端A发送`msg_id=1`的消息给客户端B，客户端A在回调函数异步处理客户端B发送`msg_id=1`的响应消息，异步非阻塞。

## Directory Structure
~~~
autopack
    ├── README.md
    ├── __init__.py
    ├── autopack.egg-info
    │       ├── PKG-INFO
    │       ├── SOURCES.txt
    │       ├── dependency_links.txt
    │       ├── requires.txt
    │       └── top_level.txt
    ├── autopack_mqtt
    │       ├── __init__.py
    │       ├── client.py
    │       ├── enums.py
    │       ├── exception.py
    │       ├── interface.py
    │       ├── logger.py
    │       ├── protocol.py
    │       └── utils.py
    ├── dist
    │       ├── autopack-1.0.0-py3-none-any.whl
    │       └── autopack-1.0.0.tar.gz
    ├── pyproject.toml
    ├── setup.py
    └── tests
        ├── __init__.py
        └── test_mqtt.py
~~~

## Installation
- package

从源码打包本地安装包 `python -m build`

- install

在项目根目录下将本地安装包安装到本地python环境 `pip install ./dist/autopack-1.0.0.tar.gz`

## Quick Start

[接口设计详细文档](autopack_mqtt.svg)

创建 mqtt client 连接及导入相关依赖文件：
```
from autopack_mqtt import (
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

# 创建一个mqtt连接
mqtt_client = MqttClientV1(
    platform=Platform.DETECTION_NODE,
    host="localhost",
    port=1883,
    username="debug",
    password="12345678",
)
```

- 异步订阅

```
# 回调接收topic
call_topic = "/dev/robot/123/service/response"

mqtt_client.sub(RobotCallbackProtocol(callback_topic))
```

- 异步请求

```
# 请求发送topic
req_topic = "/dev/robot/123/service/request"

# 回调接收topic
call_topic = "/dev/robot/123/service/response"

# 请求发送payload
payload = {
    "msg_id": generate_msg_id(),
    "type": "service",
    "id": "Carrier.SetPWM",
    "timestamp": int(time.time()),
    "data": '{"PwmL":-4000,"PwmR":-4000}',
}

mqtt_client.async_pub(
    RobotRequestProtocol(
        request_topic,
        RequestMsgProtocol(payload),
    ),
    RobotCallbackProtocol(
        callback_topic, SimpleMessageCallback(ResponseMsgProtocol())
    ),
)
```

- 同步请求

```
# 请求发送topic
req_topic = "/dev/robot/123/service/request"

# 回调接收topic
call_topic = "/dev/robot/123/service/response"

# 请求发送payload
payload = {
    "msg_id": generate_msg_id(),
    "type": "service",
    "id": "Carrier.SetPWM",
    "timestamp": int(time.time()),
    "data": '{"PwmL":-4000,"PwmR":-4000}',
}

# 请求等待超时时间
timeout_sec = 2

res = mqtt_client.sync_pub(
    RobotRequestProtocol(
        request_topic,
        RequestMsgProtocol(payload)
    ),
    RobotCallbackProtocol(
        callback_topic, SyncMessageCallback(ResponseMsgProtocol())
    ),
    timeout=timeout,
)
logger.info(f"Sync request result. [result={res}]")
```

## Q & A

## References
https://www.emqx.io/docs/zh/v4.4/

https://pypi.org/project/paho-mqtt/
