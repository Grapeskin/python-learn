import asyncio
import json
import time

import websockets


async def hello(websocket):
    async for message in websocket:
        print(f'receive_time={time.time()}')
        print(message)
        websocket.send(json.dumps({'pong': "test"}))


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.sleep(100)  # run forever


if __name__ == "__main__":
    asyncio.run(main())
