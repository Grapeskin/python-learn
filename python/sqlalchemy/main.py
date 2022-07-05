#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/7/4 20:43
"""
import json

from sqlalchemy import Integer, Column, String, DateTime, func, create_engine, or_, text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")

    name = Column(String(16), nullable=False, comment="用户名")
    age = Column(Integer, nullable=False, comment="年龄")

    create_time = Column(
        DateTime(), nullable=False, server_default=func.now(), comment="创建时间"
    )
    update_time = Column(
        DateTime(),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新时间",
    )

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name, "age": self.age})


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")

    name = Column(String(32), nullable=False, comment="地址")
    user_id = Column(Integer, nullable=False, comment="用户ID")
    create_time = Column(
        DateTime(), nullable=False, server_default=func.now(), comment="创建时间"
    )
    update_time = Column(
        DateTime(),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新时间",
    )


if __name__ == "__main__":
    engine = create_engine(
        url="mysql+pymysql://root:123456@localhost:3306/test", echo=True
    )
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    """使用如下方式查看ORM生成并执行的SQL
    打开一个MySQL连接终端并开启日志记录：
        SET GLOBAL log_output = "FILE"; the default.
        SET GLOBAL general_log_file = "/path/to/your/mysql.log";
        SET GLOBAL general_log = 'ON';

        show variables like '%log_output%';
        show variables like '%general_log_file%';
        show variables like '%general_log%';
    """
    """添加"""
    # user = User(**{'name': 'admin', 'age': 24})
    # user = [
    #     User(name='zhangsan', age=12),
    #     User(name='lisi', age=33),
    #     User(name='wangwu', age=22),
    # ]
    # print(f'pre add user {user=}')
    # res = session.add(user)
    # session.add_all(user)
    # 显式flush会把add的SQL发送到数据库连接，默认flush=True，在commit之前调用 https://zhuanlan.zhihu.com/p/48994990
    # session.flush()
    # session.rollback()
    # print(f'post add user {user=}')
    # session.commit()
    # cursor = session.execute("insert into user(name, age) value('aa', 23)")
    # print(cursor.lastrowid)
    # session.commit()
    # print(f'post commit post user {user=}')

    """查询"""
    # 1. 基本过滤条件查询
    # query对象只有在first()、all()等处理之后才会将SQL发送到数据库连接，不需要commit
    # user = session.query(User.id, User.name).filter_by(name="admin").first()
    # print(user)

    # 2. 根据条件动态构造查询条件，子查询
    # name = None
    # page = 1
    # page_size = 10
    # order_by = '-create_time'
    # sub_q = session.query(User.id, func.count(Address.id).label('street_num')) \
    #     .join(Address, User.id == Address.user_id) \
    #     .group_by(User.id) \
    #     .subquery()
    # res = session.query(User.id, User.name, User.age, User.create_time, User.update_time, sub_q.c.street_num) \
    #     .filter(User.id == sub_q.c.id) \
    #     .filter(or_(name is None, User.name.like(f'%{name}%'))) \
    #     .order_by(text(order_by)) \
    #     .offset(page_size * (page - 1)) \
    #     .limit(page_size) \
    #     .all()
    # for item in res:
    #     print(dict(item))

    # 3. 连表查询
    # res = session.query(User.id, User.name, User.age, User.create_time.label('u_time'), Address.name,
    #                     Address.id.label('a_id'),
    #                     Address.create_time.label('a_time')) \
    #     .join(Address, User.id == Address.user_id) \
    #     .filter(User.id == 18) \
    #     .order_by(text('-a_time')) \
    #     .all()
    # print(res)

    """修改"""
    # 只有commit之后才会将SQL发送到数据库连接
    # user = session.query(User).filter_by(name='zhangsan').first()
    # print(f'update pre {user=}')
    # user.age = 88
    # print(f'update post {user}')
    # session.commit()

    """删除"""
    # 只有commit之后才会将SQL发送到数据库连接
    # session.query(User).filter(User.id == 16).delete()
    # session.commit()
