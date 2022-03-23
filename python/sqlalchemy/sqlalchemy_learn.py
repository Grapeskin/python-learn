#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    :   2022/1/14 16:36
@Author  :   JiaYou
"""
from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street_name = Column(String(64))
    post_code = Column(String(10))
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"<Address(id={self.id}, street_name='{self.street_name}', post_code={self.post_code}, user_id={self.user_id})>"


class User(Base):
    # 表的名字:
    __tablename__ = "user"

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    age = Column(Integer)

    address = relationship("Address", back_populates="user", order_by=Address.id)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age}, address={self.address})>"


if __name__ == "__main__":
    # echo=True 打印生成执行SQL中日志
    engine = create_engine(
        "mysql+pymysql://ldrobot:ldrobot2022@localhost:3306/auto_detection", echo=True
    )
    # 创建表，不存在则创建，存在则跳过
    User.metadata.create_all(engine)
    # 未指定的属性为None，egg: id=None
    user = User(name="jiayou1", age=32)
    """
    References: https://docs.sqlalchemy.org/en/14/orm/tutorial.html#creating-a-session
    1. 创建Engine对象
    2. 构造工厂类Session（将Engine对象注入Session类）
        实现方式1：
            engine = create_engine('sqlite:///:memory:', echo=True)
            Session = sessionmaker(bind=engine)
        实现方式2：
            Session = sessionmaker()
            engine = create_engine('sqlite:///:memory:', echo=True)
            Session.configure(bind=engine)
    3. 实例化Session对象
    4. 使用Session对象（Session对象从Engine中连接池获取一个连接给Session对象，直到commit或关闭session对象释放连接）
    """
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    # 每次add都会生成一个自增ID，若没有提交该次add，依然会按序号自增
    user.address = [
        Address(street_name="test street", post_code="123333"),
        Address(street_name="test street 2", post_code="123443"),
    ]
    session.add(user)
    # print(session.query(User).filter(User.name == 'zhangsan').all())
    # print(session.query(Address).filter(Address.id.in_([1, 2])).all())
    session.commit()

    # for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(Address.street_name == '南山街道').all():
    #     print(u)
    #     print(a)
    connection = session.connection()
    # 使用原生SQL
    print(
        [
            dict(zip(result.keys(), result))
            for result in connection.execute("select * from user").fetchall()
        ]
    )
    # for item in session.query(Address).select_from(Address).join(User, User.id == Address.user_id).all():
    #     print(item)

    # u = session.get(User, 3)
    u = session.query(User.age.label("l_age"), User.name).filter(User.id == 4).all()
    print([dict(zip(result.keys(), result)) for result in u])
    # u.delete()
    # session.commit()
    """
    放入对象     ==>     session.new 生成
    """
    # print(session.new)
    # print(session.dirty)  # IdentitySet([])
    # our_user = session.query(User).filter_by(name='jiayou').first()
    # print(our_user is user)  # True
    # user.age = 99
    """
    user = User(name='jiayou', age=22, address_id=1)
    1. session.add(user)
    2. our_user = session.query(User).filter_by(name='jiayou').first()
    3. user.age = 99
    放入对象-->查询对象-->修改对象    ==>     session.dirty 生成
    """
    # print(session.dirty)  # IdentitySet([<User(name='jiayou', age=99, address_id=1)>])
    # print(our_user.id)
    # query = session.query(User).filter(User.name.like('%xiao%')).order_by(User.id.desc())
    # print(query.all())
    # for instance in session.query(User).filter(User.name.like('%xiao%')):
    #     print(instance)
    # session.commit()
