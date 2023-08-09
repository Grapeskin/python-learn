#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/5/8 21:22
"""
import json
import os
import re
from enum import Enum, unique

import pymysql
import requests
from pymysql.cursors import SSDictCursor
from you_get import common


@unique
class Platform(Enum):
    KS = "kuaishou"
    DY = "douyin"


def download_ks_share_urls(cookies: str, urls: list):
    """解析并下载快手分享链接"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Cookie": cookies,
        "Accept": "*/*",
    }
    for url in urls:
        redirect = requests.get(url, headers=headers)
        print(f"redirect.url={redirect.url}")
        for cookie in redirect.cookies.items():
            print(f"cookie {cookie}")
        res = requests.get(redirect.url, headers=headers)
        print(f"{res.headers=}")
        print(f"{res.text=}")
        video_url = (
            re.findall('"photoUrl":"(.*?)"', res.text)[0]
            .encode("utf-8")
            .decode("unicode-escape")
        )
        print(video_url)
        common.any_download(url=video_url, output_dir=os.path.join(os.getcwd(), "ks"))


def get_ks_user_profile(user_id: str, cookies: str):
    """获取快手用户主页信息"""
    url = "https://www.kuaishou.com/graphql"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Cookie": cookies,
        "Accept": "*/*",
    }
    res = requests.post(
        url,
        json={
            "operationName": "visionProfile",
            "variables": {"userId": user_id},
            "query": """query visionProfile($userId: String) {
                      visionProfile(userId: $userId) {
                        result
                        hostName
                        userProfile {
                          ownerCount {
                            fan
                            photo
                            follow
                            photo_public
                            __typename
                          }
                          profile {
                            gender
                            user_name
                            user_id
                            headurl
                            user_text
                            user_profile_bg_url
                            __typename
                          }
                          isFollowing
                          __typename
                        }
                        __typename
                      }
                    }
                """,
        },
        headers=header,
    )
    print(json.dumps(res.json(), indent=4, ensure_ascii=False))


def download_ks_user_all(user_id: str, cookies: str):
    """下载快手用户下所有视频"""
    url = "https://www.kuaishou.com/graphql"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Cookie": cookies,
        "Accept": "*/*",
    }
    res = requests.post(
        url,
        json={
            "operationName": "visionProfilePhotoList",
            "variables": {"userId": user_id, "pcursor": "", "page": "profile"},
            "query": """fragment photoContent on PhotoEntity {
                      id
                      duration
                      caption
                      likeCount
                      viewCount
                      realLikeCount
                      coverUrl
                      photoUrl
                      photoH265Url
                      manifest
                      manifestH265
                      videoResource
                      coverUrls {
                        url
                        __typename
                      }
                      timestamp
                      expTag
                      animatedCoverUrl
                      distance
                      videoRatio
                      liked
                      stereoType
                      profileUserTopPhoto
                      __typename
                    }

                    fragment feedContent on Feed {
                      type
                      author {
                        id
                        name
                        headerUrl
                        following
                        headerUrls {
                          url
                          __typename
                        }
                        __typename
                      }
                      photo {
                        ...photoContent
                        __typename
                      }
                      canAddComment
                      llsid
                      status
                      currentPcursor
                      __typename
                    }

                    query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {
                      visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {
                        result
                        llsid
                        webPageArea
                        feeds {
                          ...feedContent
                          __typename
                        }
                        hostName
                        pcursor
                        __typename
                      }
                    }
                    """,
        },
        headers=header,
    )
    print(json.dumps(res.json(), indent=4, ensure_ascii=False))
    result = res.json()
    feeds = result.get("data").get("visionProfilePhotoList").get("feeds", [])

    current_dir = os.getcwd()
    suffix = ".mp4"
    for feed in feeds:
        url = feed.get("photo").get("photoUrl")
        dst_file_name = feed.get("photo").get("caption") + suffix
        src_file_name = url.split("/")[-1].split("?")[0][:-17:] + suffix

        print(url)
        common.any_download(url=url, output_dir=os.path.join(os.getcwd(), "ks"))
        # os.rename(
        #     os.path.join(current_dir, src_file_name),
        #     os.path.join(current_dir, dst_file_name),
        # )


def download_pdd_share_urls(res):
    """下载拼多多视频链接"""
    for video in res:
        try:
            print(
                common.any_download(
                    url=video.get("url"), output_dir=os.path.join(os.getcwd(), "pdd")
                )
            )
            # cursor.execute(
            #     f"update pdd_video set status = 1 where id = {video.get('id')}"
            # )
            # db.commit()
        except Exception as e:
            # db.rollback()
            pass

def get_pdd_videos():
    """获取拼多多视频链接"""
    # cursor.execute("select * from pdd_video where status = 0")
    # res = cursor.fetchall()
    return [{"url": item.get("url"), "id": item.get("id")} for item in res]


if __name__ == "__main__":
    # download_ks_share_urls(
    #     cookies="did=web_cbf2e4e8bc694e56a30fd5295ce28ea8; didv=1652011511000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; userId=1680869379; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABdY1aTrRGovdedIuXlP_IkYGjfg_B924npP9FIH_BFWtRyIspxL5hWPX5sroz2vbSoL_AytO4SWMoMrlscb7rbQzZKZQ_21KXsQgRHWPJnqTOCyF_vFn75VScYjmWhhgejnndil2VYoEy7fwWFL53fa3yRtvlXCbNpdfFzOtVWEmkayWDL1awXLEpRAAG1_Py3sLzfo4Itvv5HmvAl3IcoRoS5Uf6LooXNTrpm4StA9DDXaoVIiCUSSi7zicMw_zQDTwVi5Ku9g2_g40DxqAiyKYgpGBvHSgFMAE; kuaishou.server.web_ph=08d6302e9b986a2d2b54fea807715bd5635a",
    #     urls=["https://v.kuaishou.com/k0BAhi", "https://v.kuaishou.com/jzcuGY"]
    # )
    # download_ks_user_all(user_id='3x7eraehru72ky4',
    #                      cookies='did=web_cbf2e4e8bc694e56a30fd5295ce28ea8; didv=1652011511000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; userId=1680869379; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABdY1aTrRGovdedIuXlP_IkYGjfg_B924npP9FIH_BFWtRyIspxL5hWPX5sroz2vbSoL_AytO4SWMoMrlscb7rbQzZKZQ_21KXsQgRHWPJnqTOCyF_vFn75VScYjmWhhgejnndil2VYoEy7fwWFL53fa3yRtvlXCbNpdfFzOtVWEmkayWDL1awXLEpRAAG1_Py3sLzfo4Itvv5HmvAl3IcoRoS5Uf6LooXNTrpm4StA9DDXaoVIiCUSSi7zicMw_zQDTwVi5Ku9g2_g40DxqAiyKYgpGBvHSgFMAE; kuaishou.server.web_ph=08d6302e9b986a2d2b54fea807715bd5635a')
    download_pdd_share_urls([
        {"url": 'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=a49FeeO4lLboLtJhVy0AJlnzNZuoj4jO&refer_share_channel=qq&_wvx=10&channel=2&_wv=41729&page_from=602100&feed_id=6111547885169477478&refer_share_uin=5QERZT3OESIUNRURREVL5VQDDY_GEXDA&needs_login=1&shared_time=1683454390604&shared_sign=3c213a6f50a11dfce689520443d1275f&goods_id=469644045270'}
    ])
    # db = pymysql.connect(
    #     host="localhost", port=3306, user="root", password="123456", database="test"
    # )
    # cursor = db.cursor(cursor=SSDictCursor)
    # download_pdd_share_urls()
