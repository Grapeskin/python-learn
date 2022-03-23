#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2022/1/6 15:27
@Author  :   JiaYou
"""
import socket
from wsgiref.simple_server import make_server


def handler_request(connection):
    content = connection.recv(1024)
    print(content)
    connection.send(
        bytes(
            "HTTP/1.1 200 OK\r\nServer: nginx\r\nContent-Type: text/plain;charset=UTF-8\r\n\r\nhello, World!".encode(
                "utf-8"
            )
        )
    )
    # connection.send(bytes("hello, World!".encode("utf-8")))


def socket_service():
    server = socket.socket()
    server.bind(("127.0.0.1", 8000))
    server.listen(5)
    while True:
        conn, client_address = server.accept()
        print(f"{conn=}, {client_address=}")
        handler_request(conn)
        conn.close()


def demo_app(environ, start_response):
    print(f"{environ=},{start_response=}")
    from io import StringIO

    stdout = StringIO()
    print("Hello world!", file=stdout)
    print(file=stdout)
    h = sorted(environ.items())
    for k, v in h:
        print(k, "=", repr(v), file=stdout)
    start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
    return [stdout.getvalue().encode("utf-8")]


def wsgi_service():
    server = make_server(host="127.0.0.1", port=8000, app=demo_app)
    server.serve_forever()


if __name__ == "__main__":
    """Python Web服务学习"""
    # socket_service()
    wsgi_service()
