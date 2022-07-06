#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/5/28 16:36
"""
import json
import logging
import os
import random
import re
import time

import requests
import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from pymysql import DataError, DatabaseError, Error
from sqlalchemy import (
    Column,
    String,
    create_engine,
    Integer,
    TIMESTAMP,
    text,
    Boolean,
    Text,
)
from sqlalchemy.orm import declarative_base, sessionmaker
from you_get import common

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)-15s %(levelname)s %(filename)s %(process)d %(message)s",
)
logger = logging.getLogger(__name__)

Base = declarative_base()


class AuthorInfo(Base):
    """作者基本信息"""

    __tablename__ = "author_info"
    __table_args__ = {"comment": "作者基本信息", "mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    uid = Column(String(16), nullable=False, unique=True, comment="UID")
    uin = Column(String(32), nullable=False, unique=True, comment="UIN")
    nickname = Column(String(16), nullable=False, comment="昵称")
    gender = Column(Boolean, nullable=True, comment="性别：0、女. 1、男")
    targetUid = Column(String(16), nullable=True, comment="targetUid")
    headUrl = Column(String(512), nullable=True, comment="小头像")
    linkUrl = Column(String(256), nullable=False, comment="主页地址")
    chatUrl = Column(String(512), nullable=True, comment="私信地址")
    description = Column(String(512), nullable=True, comment="主页描述")
    avatar = Column(String(512), nullable=False, comment="大头像")
    vipType = Column(Integer, nullable=True, comment="VIP类型")
    fansJumpUrl = Column(String(128), nullable=False, comment="粉丝地址")
    # sharePageUrl = Column(Text, nullable=False, comment="分享主页地址")

    createTime = Column(TIMESTAMP(True), nullable=False, server_default=text("NOW()"))
    updateTime = Column(
        TIMESTAMP(True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


class AuthorFans(Base):
    """作者粉丝信息"""

    __tablename__ = "author_fans"
    __table_args__ = {"comment": "作者粉丝信息", "mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    uid = Column(String(16), nullable=False, comment="UID")
    fans_number = Column(Integer, nullable=False, comment="作者粉丝数")

    createTime = Column(TIMESTAMP(True), nullable=False, server_default=text("NOW()"))
    updateTime = Column(
        TIMESTAMP(True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


class FeedInfo(Base):
    """资源信息"""

    __tablename__ = "feed_info"
    __table_args__ = {"comment": "资源信息", "mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    uid = Column(String(16), nullable=False, comment="UID")
    feedId = Column(String(32), nullable=False, unique=True, comment="资源ID")
    publishTime = Column(TIMESTAMP(True), nullable=False, comment="视频发布时间")
    cover = Column(String(128), nullable=False, comment="视频封面")
    description = Column(Text, nullable=True, comment="视频描述")
    h5AutoPlayUrl = Column(String(128), nullable=True, comment="视频地址")

    goodsId = Column(String(32), nullable=False, comment="商品ID")
    goodsName = Column(String(128), nullable=False, comment="商品名称")
    goodsHdThumbUrl = Column(String(128), nullable=False, comment="商品封面")
    goodsLinkUrl = Column(String(128), nullable=False, comment="商品封面")

    createTime = Column(TIMESTAMP(True), nullable=False, server_default=text("NOW()"))
    updateTime = Column(
        TIMESTAMP(True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


class ProductAnalysis(Base):
    """商品分析信息"""

    __tablename__ = "product_analysis"
    __table_args__ = {"comment": "商品分析信息", "mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    feedId = Column(String(32), nullable=False, comment="资源ID")

    likeCount = Column(Integer, nullable=False, comment="点赞数")
    viewCount = Column(Integer, nullable=False, comment="播放数")
    commentCount = Column(Integer, nullable=False, comment="评论数")
    shareCount = Column(Integer, nullable=False, comment="分享数")

    price = Column(Integer, nullable=False, comment="价格(分)")
    normalPrice = Column(Integer, nullable=False, comment="正常价格(分)")
    promoPrice = Column(Integer, nullable=False, comment="促销价(分)")
    quantity = Column(Integer, nullable=False, comment="库存(件)")
    sales = Column(Integer, nullable=False, comment="销量(件)")

    createTime = Column(TIMESTAMP(True), nullable=False, server_default=text("NOW()"))
    updateTime = Column(
        TIMESTAMP(True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


engine = create_engine(
    "mysql+pymysql://root:123456@localhost:3306/pdd?charset=utf8mb4", echo=True
)
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

app = FastAPI()


class Params(BaseModel):
    """获取用户数据参数列表"""

    user_agent: str = None
    cookie: str = None
    target_uid_list: list = None


class UrlParams(BaseModel):
    """下载视频参数列表"""

    urls: list


class AuthorInfoBO:
    """作者信息业务对象"""

    def __init__(self, **kwargs):
        self.uid = str(kwargs.get("uid"))
        self.uin = str(kwargs.get("uin"))
        self.nickname = kwargs.get("nickname")
        self.gender = 0 if kwargs.get("tags") and kwargs.get("tags")[0] == "女" else 1
        self.targetUid = kwargs.get("targetUid")
        self.headUrl = kwargs.get("headUrl")
        self.linkUrl = kwargs.get("linkUrl")
        self.chatUrl = kwargs.get("chatUrl")
        self.description = kwargs.get("desc")
        self.avatar = kwargs.get("avatar")
        self.vipType = int(kwargs.get("vipType", -1))
        self.fansJumpUrl = kwargs.get("headTabs", [])[0].get("jumpUrl")
        # self.sharePageUrl = target_uid

    def to_json(self):
        """返回对象序列化字典"""
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)


class AuthorFansBO:
    """作者粉丝业务对象"""

    def __init__(self, t_uid, **kwargs):
        self.uid = t_uid
        self.fans_number = kwargs.get("headTabs", [])[0].get("number")

    def to_json(self):
        """返回对象序列化字典"""
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)


class FeedInfoBO:
    """资源业务对象"""

    def __init__(self, uid, **kwargs):
        self.uid = uid
        feed = kwargs.get("data", {})
        self.feedId = feed.get("feedId")
        self.publishTime = feed.get("time")
        self.cover = feed.get("cover")
        self.description = feed.get("desc")
        self.h5AutoPlayUrl = feed.get("h5AutoPlayUrl")
        goods = feed.get("goodsV2", {})
        self.goodsId = goods.get("goodsId")
        self.goodsName = goods.get("goodsName")
        self.goodsHdThumbUrl = goods.get("hdThumbUrl")
        self.goodsLinkUrl = goods.get("linkUrl")

    def to_json(self):
        """返回对象序列化字典"""
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)


class ProductAnalysisBO:
    """产品分析业务对象"""

    def __init__(self, feed_id, **kwargs):
        self.feedId = feed_id
        data = kwargs.get("data", {})
        self.likeCount = data.get("likeCount")
        self.viewCount = data.get("viewCount")
        self.commentCount = data.get("commentCount")
        self.shareCount = data.get("shareCount")
        goods = data.get("goodsV2", {})
        self.price = goods.get("price", -1)
        self.normalPrice = goods.get("normalPrice", -1)
        self.promoPrice = goods.get("promoPrice", -1)
        self.quantity = goods.get("quantity", -1)
        base = float(re.findall(re.compile("\d+\.?\d*"), goods.get("salesTip"))[0])
        multi = 10000 if re.findall(re.compile("万"), goods.get("salesTip")) else 1
        self.sales = int(base * multi)

    def to_json(self):
        """返回对象序列化字典"""
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)


@app.post("/invoke")
def invoke(params: Params = Body(...)):
    """触发数据抓取"""
    print(params)
    # for index, target_uid in enumerate(params.target_uid_list):
    #     logger.info(f"{index=}, {target_uid=}")
    #     time.sleep(random.randint(2, 5))
    #     store = get_origin_data(
    #         target_uid=target_uid, user_agent=params.user_agent, cookie=params.cookie
    #     )
    prefix = os.path.join(
        os.getcwd(), time.strftime("%Y%m%d", time.localtime(time.time()))
    )
    for file_name in os.listdir(prefix):
        if file_name.endswith(".txt"):
            with open(os.path.join(prefix, file_name), mode="r") as f:
                res = f.read()
                store = re.findall(re.compile('{"store".*}'), res)
                store = json.loads(store[0]).get("store", {})
                author_info_bo = AuthorInfoBO(**store)

                print(author_info_bo.to_json())
                print(author_info_bo.uid)
                try:
                    user = (
                        session.query(AuthorInfo)
                        .filter(AuthorInfo.uid == author_info_bo.uid)
                        .first()
                    )
                    if not user:
                        session.add(AuthorInfo(**author_info_bo.__dict__))
                    author_fans_bo = AuthorFansBO(t_uid=author_info_bo.uid, **store)
                    print(author_fans_bo.to_json())
                    session.add(AuthorFans(**author_fans_bo.__dict__))
                    feeds_list = (
                        store.get("tabListData", {}).get("5", {}).get("feedsList", [])
                    )
                    for feed in feeds_list:
                        feed_info_bo = FeedInfoBO(author_info_bo.uid, **feed)
                        feed_info = (
                            session.query(FeedInfo)
                            .filter(FeedInfo.feedId == feed_info_bo.feedId)
                            .first()
                        )
                        if not feed_info:
                            session.add(FeedInfo(**feed_info_bo.__dict__))
                        product_analysis_bo = ProductAnalysisBO(
                            feed_id=feed_info_bo.feedId, **feed
                        )
                        session.add(ProductAnalysis(**product_analysis_bo.__dict__))
                    session.commit()
                except Exception as e:
                    logger.error(e, exc_info=True)
                    session.rollback()
    return {"result": "ok"}


def get_data(url: str, headers: dict, retry: int = 2):
    result = {}
    while retry > 0:
        res = requests.get(
            url=url,
            headers=headers,
        )
        # print(res.text)
        data = re.findall(re.compile('{"store".*}'), res.text)
        if data:
            result = data
            break
        retry -= 1

    return result


def get_origin_data(target_uid, cookie, user_agent=None):
    """获取原始数据"""
    if not user_agent:
        user_agent = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/102.0.5005.61 Safari/537.36 "
        )
    url = f"https://mobile.yangkeduo.com/svideo_personal.html?target_uid={target_uid}"
    headers = {
        "User-Agent": user_agent,
        "Cookie": cookie,
        "Accept": "*/*",
    }
    data = get_data(url, headers)
    if not data:
        raise Exception(f"获取data失败, {target_uid=}")
    res_json = json.loads(data[0])
    store = res_json.get("store", {})
    if not store:
        raise Exception("获取store失败")
    return store


@app.post("/download")
def download(params: UrlParams = Body(...)):
    """下载视频"""
    print(params)
    result = []
    for url in params.urls:
        common.any_download(
            url=url,
            output_dir=os.path.join(
                os.getcwd(), time.strftime("%Y%m%d", time.localtime(time.time()))
            ),
        )
        result.append(url)
    return result


class DetailParams(BaseModel):
    """获取单个用户数据参数列表"""

    uid: str
    user_agent: str
    cookie: str


@app.post("/detail")
def invoke(params: DetailParams = Body(...)):
    """下载视频"""
    print(params)
    result = []
    store = get_origin_data(
        target_uid=params.uid, cookie=params.cookie, user_agent=params.user_agent
    )
    return store


@app.post("/analysis")
def invoke(path_dir: str):
    """分析文件数据"""
    print(path_dir)
    result = []
    store = get_origin_data(
        target_uid=params.uid, cookie=params.cookie, user_agent=params.user_agent
    )
    return store


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
