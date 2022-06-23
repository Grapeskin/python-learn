#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/6/11 14:00
"""
import json
import re

import pymysql
import requests
from pymysql.cursors import SSDictCursor

from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street_name = Column(String(64))
    post_code = Column(String(10))
    user_id = Column(Integer)


class MysqlDao:
    def __init__(self, **kwargs):
        host = kwargs.get("host", "localhost")
        port = kwargs.get("port", 3306)
        username = kwargs.get("username", "root")
        password = kwargs.get("password", "123456")
        database = kwargs.get("database", "pdd")
        self.cursor = pymysql.connect(
            host=host, port=port, user=username, password=password, database=database
        ).cursor(cursor=SSDictCursor)

    def get_all_user_page_info(self):
        self.cursor.execute("select ")

    def insert_user_page_info(self, info_dict: dict):
        refer_share_id = info_dict.get("refer_share_id")
        target_uid = info_dict.get("target_uid")
        refer_share_channel = info_dict.get("refer_share_channel")
        wvx = info_dict.get("_wvx")
        x_source_feed_id = info_dict.get("_x_source_feed_id")
        pdd_fs = info_dict.get("_pdd_fs")
        wv = info_dict.get("_wv")
        share_uin = info_dict.get("share_uin")
        share_uid = info_dict.get("share_uid")
        refer_share_uin = info_dict.get("refer_share_uin")
        target_uin = info_dict.get("target_uin")
        page_key = info_dict.get("page_key")
        url = info_dict.get("url")

        sql = """

        """
        self.cursor.execute(sql)


class Main:
    def __init__(self, **kwargs):
        self.mysql_dao = MysqlDao(**kwargs)


def check_user_exist():
    global sql
    sql = f"""
    select id from author where uid = '{uid}'
    """
    cursor.execute(sql)
    return cursor.fetchone()


def update_user_info():
    global sql
    sql = f"""
            update author
            set
                uid = '{uid}',
                uin = '{uin}',
                nickname = '{nickname}',
                avatar = '{avatar}',
                link_url = '{link_url}',
                gender = '{gender}',
                target_uid = '{target_uid}',
                head_url = '{head_url}',
                chat_url = '{chat_url}',
                description = '{description}',
                fans_count = {fans_count},
                fans_jump_url = '{fans_jump_url}'
            where
                uid = '{uid}'
        """
    cursor.execute(sql)


def insert_user_info():
    global sql
    sql = f"""
            insert into author(
                uid,
                uin,
                nickname,
                avatar,
                link_url,
                gender,
                target_uid,
                head_url,
                chat_url,
                description,
                fans_count,
                fans_jump_url)
            values (
                '{uid}',
                '{uin}',
                '{nickname}',
                '{avatar}',
                '{link_url}',
                '{gender}',
                '{target_uid}',
                '{head_url}',
                '{chat_url}',
                '{description}',
                {fans_count},
                '{fans_jump_url}'
            )
        """
    cursor.execute(sql)


def insert_product_info(feed_list: list):
    global sql
    for feed in feed_list:
        feed_data = feed.get("data", {})
        feed_id = feed_data.get("feedId")
        publish_time = feed_data.get("time")
        cover = feed_data.get("cover")
        feed_link_url = feed_data.get("linkUrl")
        like_count = feed_data.get("likeCount")
        view_count = feed_data.get("viewCount")
        comment_count = feed_data.get("commentCount")
        share_count = feed_data.get("shareCount")
        native_auto_play_url = feed_data.get("nativeAutoPlayUrl")
        h5_auto_play_url = feed_data.get("h5AutoPlayUrl")
        goods = feed_data.get("goodsV2")
        goods_id = goods.get("goodsId")
        goods_name = goods.get("goodsName")
        hd_thumb_url = goods.get("hdThumbUrl")
        price = goods.get("price", -1)
        normal_price = goods.get("normalPrice", -1)
        quantity = goods.get("quantity", -1)
        sales_tip = goods.get("salesTip")
        goods_link_url = goods.get("linkUrl")
        promo_price = goods.get("promoPrice", -1)
        sql = f"""
            insert into product(feedId,
                                publish_time,
                                cover,
                                feedLinkUrl,
                                likeCount,
                                viewCount,
                                commentCount,
                                shareCount,
                                nativeAutoPlayUrl,
                                h5AutoPlayUrl,
                                goodsId,
                                goodsName,
                                hdThumbUrl,
                                price,
                                normalPrice,
                                quantity,
                                salesTip,
                                goodsLinkUrl,
                                promoPrice)
            VALUES (
                '{feed_id}',
                '{publish_time}',
                '{cover}',
                '{feed_link_url}',
                '{like_count}',
                '{view_count}',
                '{comment_count}',
                '{share_count}',
                '{native_auto_play_url}',
                '{h5_auto_play_url}',
                '{goods_id}',
                '{goods_name}',
                '{hd_thumb_url}',
                {price},
                {normal_price},
                {quantity},
                '{sales_tip}',
                '{goods_link_url}',
                {promo_price}
            )
        """
        cursor.execute(sql)


if __name__ == "__main__":
    """
    1. 定时获取分享用户列表最近所有视频
    2. 保存所有数据
    """
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=rc19d8IkvcusD707ZdDW3PtAJe0grMtt&target_uid=2140933900581&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4672347885514570425&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=MMQSBWUT5ZLIPFUXEBQ7RMC65U_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=DfE6M8SUVek2ElWAvkZ6mE8iFC6Usf50&target_uid=9744418692663&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=3FLE347ICJHL5IVCI7N5QVKMC4_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=ZhhjeR2MCtjXQzhv3Zp6Y37xWMaXk2LL&target_uid=5841601371&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4635483119437966133&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=2A55RDTOE4R7XCSLNLYFPLM7TE_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=N0vz1EVORrLtip1K0l1NVPfOv9r10Bur&target_uid=7585003467&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4551312026323480527&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=U3LY4VHBIGNIF43A6YBUVFQIE4_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=fWZTaXA566E5XsdIT9wA2SUbCVIOXyDr&target_uid=6635619718254&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4569916880722973607&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=UFURED2RT4ELD76Y7L5HWOAK7Y_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=30OWlvmb0lBDuIVVflysROYvzxRHEEu5&target_uid=3046401383679&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4555644246968754914&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=6QMNQDDBSZOFV4YMGCWDFI6EIA_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=U32LbWByrNX11lzWAiTHICrRelXmeThr&target_uid=9836678837303&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4637144067380537390&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=KUSVMPBC2R3QKOPNTDGMMB25YQ_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=BmjdLJcMUiscWrKlIvCwfqryzWQGoIW5&target_uid=3576628796&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4603350608610035693&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=KAMZJFPOTWMNZ4GZIRFAPQM3VE_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=ceRdd8CQ2DGvrkUOVkI84rY212zp12MH&target_uid=7508366439741&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4620931023791171315&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=BZ7IKOGDN2S2L626VYLW4IIRZ4_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=K6ObkGK9XAAcHuU5LTMkSwOimAPftV73&target_uid=6603751829301&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4559313516555052376&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=3JONABWETHSORKC2LT3G33TN3Y_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=9egIerKPoons2Fp87FDepaVEWjR9UoQz&target_uid=2768852940&refer_share_channel=message&refer_share_uid=2768852940&_wvx=10&_pdd_fs=1&_wv=41729&share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&share_uid=2768852940&refer_share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&target_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=gNTo79tP6M0mQTKJmQ34q6pCoxx0lRSV&target_uid=9554514590980&refer_share_channel=message&refer_share_uid=9554514590980&_wvx=10&_pdd_fs=1&_wv=41729&share_uin=CY7USXJ7MNL757AYV55SE22QWQ_GEXDA&share_uid=9554514590980&refer_share_uin=CY7USXJ7MNL757AYV55SE22QWQ_GEXDA&target_uin=CY7USXJ7MNL757AYV55SE22QWQ_GEXDA&page_key=1',
    # url = 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=i1QxFL9UXHPtdSlco8DHcIaXxEnRhv1W&target_uid=6564751287134&refer_share_channel=message&refer_share_uid=2768852940&_x_share_id=8uRDVKRBBk98Vwxw6iTNA2Tl9yk73WEO&_wvx=10&_x_source_feed_id=4584750326089499530&_pdd_fs=1&_wv=41729&share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&share_uid=2768852940&refer_share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&target_uin=KHEKWKUFHTMDKWH7FBKHLNHLNE_GEXDA&page_key=1',
    urls = [
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=rc19d8IkvcusD707ZdDW3PtAJe0grMtt&target_uid=2140933900581&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4672347885514570425&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=MMQSBWUT5ZLIPFUXEBQ7RMC65U_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=DfE6M8SUVek2ElWAvkZ6mE8iFC6Usf50&target_uid=9744418692663&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=3FLE347ICJHL5IVCI7N5QVKMC4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=ZhhjeR2MCtjXQzhv3Zp6Y37xWMaXk2LL&target_uid=5841601371&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4635483119437966133&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=2A55RDTOE4R7XCSLNLYFPLM7TE_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=N0vz1EVORrLtip1K0l1NVPfOv9r10Bur&target_uid=7585003467&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4551312026323480527&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=U3LY4VHBIGNIF43A6YBUVFQIE4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=fWZTaXA566E5XsdIT9wA2SUbCVIOXyDr&target_uid=6635619718254&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4569916880722973607&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=UFURED2RT4ELD76Y7L5HWOAK7Y_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=30OWlvmb0lBDuIVVflysROYvzxRHEEu5&target_uid=3046401383679&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4555644246968754914&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=6QMNQDDBSZOFV4YMGCWDFI6EIA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=U32LbWByrNX11lzWAiTHICrRelXmeThr&target_uid=9836678837303&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4637144067380537390&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=KUSVMPBC2R3QKOPNTDGMMB25YQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=BmjdLJcMUiscWrKlIvCwfqryzWQGoIW5&target_uid=3576628796&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4603350608610035693&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=KAMZJFPOTWMNZ4GZIRFAPQM3VE_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=ceRdd8CQ2DGvrkUOVkI84rY212zp12MH&target_uid=7508366439741&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4620931023791171315&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=BZ7IKOGDN2S2L626VYLW4IIRZ4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=K6ObkGK9XAAcHuU5LTMkSwOimAPftV73&target_uid=6603751829301&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4559313516555052376&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=3JONABWETHSORKC2LT3G33TN3Y_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=9egIerKPoons2Fp87FDepaVEWjR9UoQz&target_uid=2768852940&refer_share_channel=message&refer_share_uid=2768852940&_wvx=10&_pdd_fs=1&_wv=41729&share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&share_uid=2768852940&refer_share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&target_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=gNTo79tP6M0mQTKJmQ34q6pCoxx0lRSV&target_uid=9554514590980&refer_share_channel=message&refer_share_uid=9554514590980&_wvx=10&_pdd_fs=1&_wv=41729&share_uin=CY7USXJ7MNL757AYV55SE22QWQ_GEXDA&share_uid=9554514590980&refer_share_uin=CY7USXJ7MNL757AYV55SE22QWQ_GEXDA&target_uin=CY7USXJ7MNL757AYV55SE22QWQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=i1QxFL9UXHPtdSlco8DHcIaXxEnRhv1W&target_uid=6564751287134&refer_share_channel=message&refer_share_uid=2768852940&_x_share_id=8uRDVKRBBk98Vwxw6iTNA2Tl9yk73WEO&_wvx=10&_x_source_feed_id=4584750326089499530&_pdd_fs=1&_wv=41729&share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&share_uid=2768852940&refer_share_uin=A5BGVEP3NP75VQZFRHSMRFDGGY_GEXDA&target_uin=KHEKWKUFHTMDKWH7FBKHLNHLNE_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=9swaLRquEv7yCr1mtBe2XfbavZCaZCW0&target_uid=2692091088032&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4457449805275467465&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=V3NQENO7FY72HFJ722V756LMKA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=Npy2r3Nt0mUH3VS7E5EWQeceu8ZuduWH&target_uid=7493454340183&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4382624213405201311&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=BLNN3BR4TW3WIEWVRJLOCUXIS4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=M0HIfjQoRfHMfOv8RAZWCC9dRpUCeY74&target_uid=7855156424896&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4695367336634879766&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=EKF4V3KSA42UX3OUGXGKBRBVMQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=JfgSdlHfLAU1tFYXu9RkvEK2XUc5ryeU&target_uid=9239752387661&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4634698951374253690&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=KVVOXRLNF6JNC2D3NSRHRHFOUI_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=vAWLSUhMP7Nbjq2P0KWUEdETl3ydwHk9&target_uid=6775611813195&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4673258432213121722&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=ODCVZGVT6LM3KIISMAQRTYOPBM_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=rGeS5kzIgRmc5zIuKCX8u06c8yFzvGhG&target_uid=1666353479037&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4682278575828609530&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=7I2A76EVIUK6WM46S3P7F2JK3I_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=xMSbnLKNYY32JnObA9vvKUdJgLJfCeyS&target_uid=7855156424896&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4672265673950888812&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=EKF4V3KSA42UX3OUGXGKBRBVMQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=ealFAYQd7ee7FM3uE5FfYLQQcOt7MpFP&target_uid=4439506521002&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4606147468742449379&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=4YG7KYPMYF65NFK3VHFOJ4RPIA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=Wfgg5IjcnlVGKlxDjBY0L74NwAIFGS7G&target_uid=5186014243063&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4684096921225065220&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=SQFUB4EQ7W6IQHMHEZPXXJK734_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=acmLIl2did9c7d4wTUe1tRqAZBFP6OgA&target_uid=6149160238335&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4681154888030216370&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=5TJ6LRO4INZA7FTDFHO4NVQICY_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=qL7yGTWtxgKX48bJMyHqOkvQZOuqYTq4&target_uid=4108781523234&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4696095082605205536&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=YI4EVSGN5EIMVIM2X7B3XIOIGA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=a1uAHoFwRV7tflJIbxxyMeqGBYw2Vgum&target_uid=4048253216&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4692546986801627629&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=UADVNTP6RRJD6M2I3KMT5YZEAU_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=XBCcaNn5KyT8r8LXLe9hElCesPtIgMXZ&target_uid=1845561305648&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4528220726930835275&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=7MLQYGT2WN5EOAHHEQOHD37OWE_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=09dcTFwpJXABjGo4qbgqdVR9nT6x9bKO&target_uid=4477352692&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4478359097671847787&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=UMZ6RLBEK34ORITMVCLHFIIBJ4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=PKoL2XhBy7d3tz4uFIUrPATJqIhjwQbU&target_uid=6069838489&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4635285470544342272&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=D37N7J5URUQVHQR3MFPOBEC34U_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=dwfPWXzHZVFGi7NXQh25pyTSfTRWPNjn&target_uid=4697193411&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4700982945227763145&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=FUR3NWMQBEBDCNNMOBTK4TYCDQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=7luwwo8LZzpJMf1mNS5HSpxzvDFKep9W&target_uid=5586988702791&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4577038952175300679&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=R5Z6OZUACWM4OUCYSBMMCLLQQY_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=P9tIcWzdgEW4nV3BtKRuAw5FL49lxCJV&target_uid=2500143790213&refer_share_channel=qq&refer_share_uid=6557394080&_wvx=10&_x_source_feed_id=4637386128894241366&_pdd_fs=1&_wv=41729&share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&share_uid=6557394080&refer_share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&target_uin=SEDK6BUELVO76J5NJQGM65MJC4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=u4M3N1GRRFkfC6FRcIgs7eLpAaySL7HP&target_uid=4692954117896&refer_share_channel=qq&refer_share_uid=6557394080&_wvx=10&_x_source_feed_id=4591685717853280913&_pdd_fs=1&_wv=41729&share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&share_uid=6557394080&refer_share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&target_uin=GZW76WW5XDNRFUTULVME6HNEQI_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=SQc6TmHykvmJttAJyAVGUqjXCbOBGhsQ&target_uid=4009766496516&refer_share_channel=qq&refer_share_uid=6557394080&_wvx=10&_x_source_feed_id=4664463576468070369&_pdd_fs=1&_wv=41729&share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&share_uid=6557394080&refer_share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&target_uin=RC23JOPXWSYWRIR7XTCVX4AHE4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=tZdJM4oOxXCYSfUTcBvGCzvaCmugWaSZ&target_uid=2993885166491&refer_share_channel=qq&refer_share_uid=6557394080&_wvx=10&_x_source_feed_id=4466229564534911452&_pdd_fs=1&_wv=41729&share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&share_uid=6557394080&refer_share_uin=AT7KLQIKM7E3LF56KV4V3OH4EI_GEXDA&target_uin=K5BHPDGLQZ6OTCGCF74CWNMHB4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=WO2VxPEU7CZdSNaEHtFG59ChDXFvvJo9&target_uid=3502709770930&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4620723846324310000&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=I4JT37L6WNUM3DISODMGRLMRK4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=c4YoDHZX0eeSE7U0UhGgd3rewu9fyxdG&target_uid=1095267241089&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4692235367218164700&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=5EHSQKEWOX26VZBR3SDDEOZ6D4_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=sIgdqUPABCKkxpVwi04UpRP8Ip0olWkI&target_uid=7607874366155&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4556270484099529596&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=4VTZ5KQRUBFT6WDQHSUOUP76SI_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=2g8UE5MlEsP3dOOAl1PA0hCdzwLYw86u&target_uid=6990264715&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4582372896851195411&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=3IUWBAEJQX7TCIDJ6HQUSMV2QQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=jahqBuPNYEBxUxe1MPrIfrK0AdyV22Se&target_uid=7410762227810&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4642803091921195211&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=YUIG5MMBUPJ65PLGI3XH35DPAQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=NGLHx98vWPlsoaOxLNEy1MAybSykZ2vR&target_uid=4108781523234&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4680085546442447817&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=YI4EVSGN5EIMVIM2X7B3XIOIGA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=ntAIsT9med7WGa1XuLE9cyb9LOSV9qXO&target_uid=8037876281&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4483010536531243333&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=F6RZOAPV3FZM6YGMA572S544NI_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=RceLExGJJuUzUV3dtrbxhqJhUrnfIop3&target_uid=7129784694284&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4693510804786483231&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=6HPK3IY4QFCH7C5624SKEVWNYY_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=I14wzRRoup4I599nA8TxlUaHV3JBvPkl&target_uid=7510741626822&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4701216963911271452&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=FVBLFL3IIABJXJ5X6RAX6NGYCQ_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=yRZaXaN6r7f7o4e3rvyZi4cPJMhiD1BX&target_uid=8355523898058&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4686191209492337589&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=XHYB2F7CSTRAVCOSR3Y2FX6VYA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=2sw1uQl2ssfAOAttjrB2YzudWXkFIenb&target_uid=3816828944824&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4654980391171986396&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=3TSGNJWRVIF2EUG3FUPZVXRBEA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=jYdmWM7n3if1YwoIqZCPa7rkEYt3CWKt&target_uid=4216425556&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4664511184576873384&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=UEDU4LU4B7J26WN5RKUVE6WLAE_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=iIRGVosazCa7SiM35b7iLqg6RYJgKwL1&target_uid=1251780693115&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4484550461072834152&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=YGTTB7V4A4UWFF4KU5CPUESSAU_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=Mk3X2Dv5v3qTAw9mx0BjfKXo9mh0XIEj&target_uid=5346532812697&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4559417682347373209&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=IPNXBRUXZQRMKCWX6JOYXO4A7E_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=WNm0V5TdD772fnsIHE2kXLhVKEHcNO83&target_uid=6627204455173&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4255065274780268073&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=OFW7Z6R4AZWPTK6STCAN26TFQU_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=bw6eY9ujMZ7qaRurAyKCHrUvWSOyOfz0&target_uid=7342099410&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4666076415412290521&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=FV2JS7UFRSSGZ7BEBA7HKIQO5M_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=W3vbhjyPaEz5O7KZV3Cme6uXsb63J5z1&target_uid=4750623374&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4675149468005417207&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=5TXG6FRP5J7BXEDT7TAMJGZJZA_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=zYJCISGLiBjyFZ6fJnWx2fAOYwrGzUw7&target_uid=4664377545&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4678776662238245881&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=77HQIU6UX2WIWSSNGBSBGFIEWI_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=Sx7n3JP0ukBvOIU6BSEKtS45z7ZZ5LCN&target_uid=5238694334&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4683685990650858487&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=ARIPN6OWZRVQII7SPCHFDA4GOE_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=MtpUm3WsYBrpLzE3Gj4abARl2ubODCpO&target_uid=3733510690&refer_share_channel=qq&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4512733609651884072&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=MXZBP2U4X5MS3IJ4ZAO3ZINUZI_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=u8uok6L30gE72nzjb0B5FEacA7ctndNL&target_uid=7129784694284&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4696033820208635193&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=6HPK3IY4QFCH7C5624SKEVWNYY_GEXDA&page_key=1",
        "https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=0kydzFtgTvX7o51WIItdudzKXBlN3rVL&target_uid=2692091088032&refer_share_channel=message&refer_share_uid=8647772212739&_wvx=10&_x_source_feed_id=4457449805275467465&_pdd_fs=1&_wv=41729&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&share_uid=8647772212739&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&target_uin=V3NQENO7FY72HFJ722V756LMKA_GEXDA&page_key=1",
    ]
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
        "Cookie": "api_uid=Ck5psWKkOlZgigBwCJdaAg==; _nano_fp=XpEyn0UqX09on5EaXo_VRtpb~bon2k2dC~ikAiKl; webp=1; jrpl=m2UEmjb1uPNkFdIhjTU6iifJQ14vpF6E; njrpl=m2UEmjb1uPNkFdIhjTU6iifJQ14vpF6E; dilx=B7fRebVT2pFo~_tQj4wfy; PDDAccessToken=LKO4P2FO3T4RGD7WGECN6WGT76KKK3UOV6T45ABOCDRDCWLAB6IQ113225d; pdd_user_id=2934615063330; pdd_user_uin=CACBYJFPLJLE2BVDL3SJ7UAJOY_GEXDA; webgl=1; pdd_vds=gaLuNLPNybnGLGnmOuQwosGtytalOdotOIIttsilPNyxybLONGmsQnmIOtyb",
        "Accept": "*/*",
    }
    db = pymysql.connect(
        host="localhost", port=3306, user="root", password="123456", database="pdd"
    )
    cursor = db.cursor(cursor=SSDictCursor)
    for url in urls:
        res = requests.get(url=url, headers=header)
        # print(res.text)
        data = re.findall(re.compile('{"store".*}'), res.text)[0]
        if not data:
            raise Exception("获取data失败")
        res_json = json.loads(data)
        store = res_json.get("store", {})
        if not store:
            raise Exception("获取store失败")
        # 用户信息
        uid = store.get("uid")
        uin = store.get("uin")
        nickname = store.get("nickname")
        gender = 0 if store.get("tags", []) and store.get("tags", [])[0] == "女" else 1
        target_uid = store.get("targetUid")
        head_url = store.get("headUrl")
        avatar = store.get("avatar")
        link_url = store.get("linkUrl")
        chat_url = store.get("chatUrl")
        description = store.get("desc")
        head_tabs = store.get("headTabs", [])[0]
        fans_count = head_tabs.get("number")
        fans_jump_url = head_tabs.get("jumpUrl")

        tab_list_data = store.get("tabListData", {}).get("5", {})
        # 视频信息
        if not tab_list_data:
            raise Exception("获取tab_list_data失败")
        feeds_list = tab_list_data.get("feedsList", [])

        offset = tab_list_data.get("offset")
        feed_scene_id = tab_list_data.get("feedSceneId", [])
        page_from = tab_list_data.get("pageFrom", [])
        real_list_id = tab_list_data.get("realListId", [])

        # print(len(feeds_list))
        # print(offset)

        sql = ""
        try:
            user_exist = check_user_exist()

            if user_exist:
                update_user_info()
            else:
                insert_user_info()

            insert_product_info(feeds_list)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
