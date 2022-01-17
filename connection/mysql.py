#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/1/14 10:34
@Author  :   JiaYou
"""

import pymysql as pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import Cursor, DictCursor

"""MySQL数据库连接处理
业务线程<-- 连接对象的游标 <-- 连接池 --> MySQL instance
"""


class ConnectConfig:
    def __init__(self):
        """
        References: https://pymysql.readthedocs.io/en/latest/modules/connections.html
        """
        self.host = "localhost"
        self.port = 3306
        self.user = "ldrobot"
        self.password = "ldrobot@2022"
        self.database = "auto_detection"
        self.charset = "utf8mb4"
        self.read_timeout = 30
        self.write_timeout = 60
        self.connect_timeout = 10
        # 默认非自动提交
        self.autocommit = False

    def to_dict(self):
        return {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "database": self.database,
            "charset": self.charset,
            "read_timeout": self.read_timeout,
            "write_timeout": self.write_timeout,
            "connect_timeout": self.connect_timeout,
            "cursorclass": DictCursor,
            "autocommit": self.autocommit
        }


class ConnectionPool:
    """数据库连接池"""
    _pool = None

    def __init__(self, connect_config: dict = None):
        if connect_config is None:
            # TODO 异常处理
            raise Exception()
        self._connect_config = connect_config
        self.conn = self._get_conn()
        self.cursor: Cursor = self._get_cursor()

    def _get_conn(self):
        """从数据库连接池获取一个连接对象"""
        if ConnectionPool._pool is None:
            """
            References: https://webwareforpython.github.io/DBUtils/main.html
            """
            pool = PooledDB(creator=pymysql, mincached=2, maxcached=10, maxshared=10, maxconnections=40, blocking=False,
                            **self._connect_config)

            ConnectionPool._pool = pool
        return ConnectionPool._pool.connection()

    def _get_cursor(self):
        return self._get_conn().cursor()


if __name__ == '__main__':
    pool = ConnectionPool(ConnectConfig().to_dict())
