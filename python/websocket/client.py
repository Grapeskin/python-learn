import asyncio
import json
import time
from asyncio import Future

import websockets
from websockets.legacy.client import WebSocketClientProtocol


def hello():
    uri = "ws://localhost:8765"
    i = 0
    print(f'start_time={time.time()}')
    client = websockets.connect(uri,)
    while True:
        print(f'send_time={time.time()}')
        client.send(json.dumps({'ping': "test"}))
        # receive = client.recv()
        # print(receive)
        time.sleep(1)


if __name__ == "__main__":
    hello()
    while True:
        time.sleep(1)
