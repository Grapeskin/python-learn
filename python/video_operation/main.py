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


def download_pdd_share_urls():
    """下载拼多多视频链接"""
    for video in get_pdd_videos():
        try:
            print(
                common.any_download(
                    url=video.get("url"), output_dir=os.path.join(os.getcwd(), "pdd")
                )
            )
            cursor.execute(
                f"update pdd_video set status = 1 where id = {video.get('id')}"
            )
            db.commit()
        except Exception as e:
            db.rollback()


def get_pdd_videos():
    """获取拼多多视频链接"""
    cursor.execute("select * from pdd_video where status = 0")
    res = cursor.fetchall()
    return [{"url": item.get("url"), "id": item.get("id")} for item in res]


if __name__ == "__main__":
    # download_ks_share_urls(
    #     cookies="did=web_cbf2e4e8bc694e56a30fd5295ce28ea8; didv=1652011511000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; userId=1680869379; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABsoTiDhvcdyJEK-Ut0gGV-MYiO8foEeADFKbmVryHQw3FhF0xNiQ7DwcPWD_unKxUMxuLJp-fFrz9bWefkZWpOn4rIemVz8rgG8MAjUBmSrmsFJzgTOmvXHCtrAryRDfP_E52EAwe99tyrnep1cn8G_3Fjk0oyH8--FTz3kBwDggzMfK7S5CILII4I3bOYUspFZ_3rZ386ou9f2JExB0DKRoSsmhEcimAl3NtJGybSc8y6sdlIiATKk7DGHFyGY3egCOWusSI5ku6U7yuZLLxBHYkx2sRnigFMAE; kuaishou.server.web_ph=99d48baa0b24c33e459ac187b55ee698389b",
    #     urls=["https://v.kuaishou.com/jFpS2n"]
    # )
    # 'https://v.kuaishou.com/jFpS2n @阿浩好物分享 发了一个快手作品，一起来看！复制此消息，打开【快手】直接观看！'
    # download_ks_user_all(user_id='3xvw6xmjeqat32s',
    #                      cookies='did=web_cbf2e4e8bc694e56a30fd5295ce28ea8; didv=1652011511000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; userId=1680869379; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABsoTiDhvcdyJEK-Ut0gGV-MYiO8foEeADFKbmVryHQw3FhF0xNiQ7DwcPWD_unKxUMxuLJp-fFrz9bWefkZWpOn4rIemVz8rgG8MAjUBmSrmsFJzgTOmvXHCtrAryRDfP_E52EAwe99tyrnep1cn8G_3Fjk0oyH8--FTz3kBwDggzMfK7S5CILII4I3bOYUspFZ_3rZ386ou9f2JExB0DKRoSsmhEcimAl3NtJGybSc8y6sdlIiATKk7DGHFyGY3egCOWusSI5ku6U7yuZLLxBHYkx2sRnigFMAE; kuaishou.server.web_ph=99d48baa0b24c33e459ac187b55ee698389b; clientid=3; did=web_43c22563da6c2789e316930f5aeb3891; kpf=PC_WEB; kpn=KUAISHOU_VISION')
    # download_pdd_share_urls([
    #     'https://mobile.yangkeduo.com/fyxmkief.html?refer_share_id=fcHutf63jqxPyRKjWRYkDLUBdGYMJMnf&refer_share_channel=message&refer_share_uid=8647772212739&_x_share_id=fWZTaXA566E5XsdIT9wA2SUbCVIOXyDr&_wvx=10&_x_source_feed_id=4569916880722973607&share_uid=8647772212739&share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&page_from=602100&feed_id=4628849246568566060&refer_share_uin=3LS2542HF32COXS3ZR5VDK5EJA_GEXDA&needs_login=1&shared_time=1653311024255&shared_sign=a653b53db3e2f8a1353d58effac76d42&_wv=41729&goods_id=330659862161'
    # ])
    db = pymysql.connect(
        host="localhost", port=3306, user="root", password="123456", database="test"
    )
    cursor = db.cursor(cursor=SSDictCursor)
    download_pdd_share_urls()
