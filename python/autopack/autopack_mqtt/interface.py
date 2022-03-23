#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2022/3/18 11:21
@Author  :   JiaYou
"""
import abc

from .protocol import (
    RequestProtocol,
    CallbackProtocol,
    SyncStatus,
)


class SubInterface:
    @abc.abstractmethod
    def sub(self, callback_protocol: CallbackProtocol):
        """Sub wait callback message

        Args:
            callback_protocol: callback protocol after sending the sync request

        Raises:
            ParamError: param error exception.
        Returns:
            callback message payload
        """
        pass


class AsyncPubInterface:
    @abc.abstractmethod
    def async_pub(
        self, request_protocol: RequestProtocol, callback_protocol: CallbackProtocol
    ):
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
    def sync_pub(
        self,
        request_protocol: RequestProtocol,
        callback_protocol: CallbackProtocol,
        timeout: int,
    ) -> str:
        """Sync request and wait response until timeout raise Exception

        Args:
            request_protocol: sync request protocol
            callback_protocol: callback protocol after sending the sync request
            timeout: max wait time

        Raises:
            ParamError: param error exception.
            SyncTimeoutError: wait timeout exception.
            DataFormatError：response data format error.
        Returns:
            response payload
        """
        pass
