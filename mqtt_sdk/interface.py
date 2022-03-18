#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/3/18 11:21
@Author  :   JiaYou
"""
import abc

from mqtt_sdk.protocol import MessageCallback, RequestProtocol, CallbackProtocol, SyncStatus


class SubInterface:
    @abc.abstractmethod
    def sub(self, message_callback: MessageCallback):
        """Sub wait callback message

        Args:
            message_callback: callback protocol after sending the sync request

        Raises:
            ParamError: param error exception.
        Returns:
            callback message payload
        """
        pass


class AsyncPubInterface:
    @abc.abstractmethod
    def async_pub(self, request_protocol: RequestProtocol, callback_protocol: CallbackProtocol):
        """Async request and wait response

        Args:
            request_protocol: sync request protocol
            callback_protocol: callback protocol after sending the sync request

        Raises:
            ParamError: param error exception.
        """
        pass


class SyncPubInterface(SyncStatus):
    @abc.abstractmethod
    def sync_pub(self, request_protocol: RequestProtocol, callback_protocol: CallbackProtocol, timeout: int = 2):
        """Sync request and wait response until timeout raise Exception

        Args:
            request_protocol: sync request protocol
            callback_protocol: callback protocol after sending the sync request
            timeout: max wait time

        Raises:
            ParamError: param error exception.
            SyncTimeoutError: wait timeout exception.
        Returns:
            response payload
        """
        pass
