#!/usr/bin/python3
# -*- coding: utf-8 -*- 
"""
@Time    :   2022/1/14 16:36
@Author  :   JiaYou
"""
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://ldrobot:ldrobot2022@localhost:3306/auto_detection')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    new_user = User(id='5', name='Bob')
    session.add(new_user)
    session.commit()
    session.close()
