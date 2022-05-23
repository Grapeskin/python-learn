# 短视频

## 快手

### 获取博主主页信息

#### request:

##### header

```http request
POST /graphql HTTP/1.1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Connection: keep-alive
Content-Length: 552
Cookie: did=web_cbf2e4e8bc694e56a30fd5295ce28ea8; didv=1652011511000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; userId=1680869379; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABGqjH4Zoode2cqHDOgkOVTI0thsHle8sbkhbxvWIYKDyLXwKYQR_V7ZhrKqEGw8hxQ_G5GdI_rqM9leZ7qtmlVRpc0ngJuiQr7IU0ZBitBDM0FsUY00iHFir9JvsgVbfJsbOyhglx1rSAkjUw0es06yxRQznGdM5xRFa9v6m8JHEp8vGlG1X8qTMXWR_LRlEau_rKPfJEJd5JQneqSqolIRoSf061Kc3w5Nem7YdpVBmH39ceIiDRS2IjqOnmroiJUIqSM5fz008E82LBx95QhLVvNukJWygFMAE; kuaishou.server.web_ph=e97f70cd95a53fa09bdce7dada843f19936f
Host: www.kuaishou.com
Origin: https://www.kuaishou.com
Referer: https://www.kuaishou.com/profile/3x27q2f82gnxn4e
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36
accept: */*
content-type: application/json
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
```

##### body

```json
{
  "operationName": "visionProfile",
  "variables": {
    "userId": "3x27q2f82gnxn4e"
  },
  "query": "query visionProfile($userId: String) {\n  visionProfile(userId: $userId) {\n    result\n    hostName\n    userProfile {\n      ownerCount {\n        fan\n        photo\n        follow\n        photo_public\n        __typename\n      }\n      profile {\n        gender\n        user_name\n        user_id\n        headurl\n        user_text\n        user_profile_bg_url\n        __typename\n      }\n      isFollowing\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```

#### response body:

```json
{
  "data": {
    "visionProfile": {
      "result": 1,
      "hostName": "public-bjmt-c9-kce-node582.idcyz.hb1.kwaidc.com",
      "userProfile": {
        "ownerCount": {
          "fan": "169.8w",
          "photo": null,
          "follow": 396,
          "photo_public": 202,
          "__typename": "VisionUserProfileOwnerCount"
        },
        "profile": {
          "gender": "M",
          "user_name": "徐医 .",
          "user_id": "3x27q2f82gnxn4e",
          "headurl": "https://p2.a.yximgs.com/uhead/AB/2022/03/15/11/BMjAyMjAzMTUxMTM3MjlfMTYzMDk5MjQyMF8xX2hkOTM5XzIyNw==_s.jpg",
          "user_text": "302·医生为瑶❤️\n收徒 xx11103c （待遇好）",
          "user_profile_bg_url": "//s2-10623.kwimgs.com/kos/nlav10623/vision_images/profile_background.5bc08b1bf4fba1f4.svg",
          "__typename": "VisionUserProfileUser"
        },
        "isFollowing": false,
        "__typename": "VisionUserProfile"
      },
      "__typename": "VisionProfileResult"
    }
  }
}
```

### 获取主页所有视频

#### request:

##### header

```http request
POST /graphql HTTP/1.1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Connection: keep-alive
Content-Length: 1160
Cookie: did=web_cbf2e4e8bc694e56a30fd5295ce28ea8; didv=1652011511000; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; client_key=65890b29; userId=1680869379; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABGqjH4Zoode2cqHDOgkOVTI0thsHle8sbkhbxvWIYKDyLXwKYQR_V7ZhrKqEGw8hxQ_G5GdI_rqM9leZ7qtmlVRpc0ngJuiQr7IU0ZBitBDM0FsUY00iHFir9JvsgVbfJsbOyhglx1rSAkjUw0es06yxRQznGdM5xRFa9v6m8JHEp8vGlG1X8qTMXWR_LRlEau_rKPfJEJd5JQneqSqolIRoSf061Kc3w5Nem7YdpVBmH39ceIiDRS2IjqOnmroiJUIqSM5fz008E82LBx95QhLVvNukJWygFMAE; kuaishou.server.web_ph=e97f70cd95a53fa09bdce7dada843f19936f
Host: www.kuaishou.com
Origin: https://www.kuaishou.com
Referer: https://www.kuaishou.com/profile/3x27q2f82gnxn4e
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36
accept: */*
content-type: application/json
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
```

##### body

```json
{
  "operationName": "visionProfilePhotoList",
  "variables": {
    "userId": "3x27q2f82gnxn4e",
    "pcursor": "",
    "page": "profile"
  },
  "query": "fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  likeCount\n  viewCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
}
```

#### response body:

```json
{
  "data": {
    "visionProfilePhotoList": {
      "result": 1,
      "llsid": "2005176069751607249",
      "webPageArea": "profilexxnull",
      "feeds": [
        {
          "type": 1,
          "author": {
            "id": "3x27q2f82gnxn4e",
            "name": "徐医 .",
            "headerUrl": "https://p2.a.yximgs.com/uhead/AB/2022/03/15/11/BMjAyMjAzMTUxMTM3MjlfMTYzMDk5MjQyMF8xX2hkOTM5XzIyNw==_s.jpg",
            "following": false,
            "headerUrls": null,
            "__typename": "Author"
          },
          "photo": {
            "id": "3xa7hvqbt9rg9my",
            "duration": 9800,
            "caption": "还有很多事 想和你慢 慢 做 @苏芷暖.(O3x9yjsxs4p39r6w)",
            "likeCount": "7610",
            "viewCount": "154028",
            "realLikeCount": 7610,
            "coverUrl": "https://p2.a.yximgs.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_Bded84a1cad28fd531ef865a415d59f11.jpg?tag=1-1653123292-xpcwebprofile-0-ye6vxipgbl-1bc03208561e2195&clientCacheKey=3xa7hvqbt9rg9my.jpg&di=b70be6e3&bp=14734",
            "photoUrl": "https://v1.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_b_B6252bd5a9470739c8cd7bdd930df2fe7.mp4?pkey=AAXcEwuohnEBRHT9e3ZSjVEhIJ8_-qQLDqkD0OfakjdPH_NMm9skZQ2be3ZVbFp5mV9nIlOZiPCszMA16IvWkti9RPh-zySJkQDRI9ohMErdQVgefhnKQBQMkjFq7RsMf6Q&tag=1-1653123292-unknown-0-dhuwp54qf9-5e7b3087ea3804f2&clientCacheKey=3xa7hvqbt9rg9my_b.mp4&di=b70be6e3&bp=14734&tt=b&ss=vp",
            "photoH265Url": "https://v2.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_hd15_B98f58d747f83176207ebea3ef44e2d47.mp4?pkey=AAXexZp32HLPhtz7FTrihV4kvqqdFxe0dpcoB04zFB4sbJdIlv8gs7bvToGwG4yRGjJ8-yTXAsXKHyCpr6pNid-so_udQlJfyAnG3Im5ItPsMXd4kkb91xdZ_izzf-ak4i4&tag=1-1653123292-unknown-0-efgyefdo4y-004c4f679508f8a4&clientCacheKey=3xa7hvqbt9rg9my_hd15.mp4&di=b70be6e3&bp=14734&tt=hd15&ss=vp",
            "manifest": {
              "version": "1.0.0",
              "businessType": 2,
              "mediaType": 2,
              "videoId": "db4210b2fa736828",
              "hideAuto": false,
              "manualDefaultSelect": false,
              "stereoType": 0,
              "adaptationSet": [
                {
                  "id": 1,
                  "duration": 9800,
                  "representation": [
                    {
                      "id": 1,
                      "url": "https://v1.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_b_B6252bd5a9470739c8cd7bdd930df2fe7.mp4?pkey=AAV-Ls4pObyzJAnPmKwGFakTMuL5IQHxi2A9D5tCMZZNQeO56JYh6R5XoRqvmqumX2miP9u5StC2vAzFJGk7Pfu5n4FSuGVF6zYF4QM3ss500Im4uvl85GOjH3e8-uUP4nY&tag=1-1653123292-unknown-0-evb4cjqdsd-e0aaac50f5d81fe8&clientCacheKey=3xa7hvqbt9rg9my_b.mp4&di=b70be6e3&bp=14734&tt=b&ss=vp",
                      "backupUrl": [
                        "https://v2.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_b_B6252bd5a9470739c8cd7bdd930df2fe7.mp4?pkey=AAWaeyZluCuBdOEKdkjBrPBoq3F66RISIunCqY8bx0kCv62ilXbBxW_O3npOaKuDuyUVJQt9UqzmobOf_G293udKnG2he77Gc-Qsb7LONZD56M08lqDNSY5DHH80iPePa0Y&tag=1-1653123292-unknown-1-h5waan2oie-68eb7ea79d3dff56&clientCacheKey=3xa7hvqbt9rg9my_b.mp4&di=b70be6e3&bp=14734&tt=b&ss=vp"
                      ],
                      "maxBitrate": 4900,
                      "avgBitrate": 3116,
                      "width": 720,
                      "height": 1280,
                      "frameRate": 60,
                      "quality": 1.5,
                      "qualityType": "720p",
                      "qualityLabel": "高清",
                      "featureP2sp": false,
                      "hidden": false,
                      "disableAdaptive": false,
                      "defaultSelect": false,
                      "comment": "db4210b2fa736828/b",
                      "hdrType": 5,
                      "fileSize": 3928959,
                      "bitratePattern": [
                        3207,
                        2421,
                        4435,
                        2248,
                        698
                      ]
                    }
                  ]
                }
              ],
              "playInfo": {
              },
              "videoFeature": {
                "blurProbability": 0.5342053771018982,
                "blockyProbability": 0.5063997507095337,
                "avgEntropy": 6.799987115358052,
                "mosScore": 0.410698801279068
              }
            },
            "manifestH265": {
              "version": "1.0.0",
              "businessType": 2,
              "mediaType": 2,
              "videoId": "db4210b2fa736828",
              "hideAuto": false,
              "manualDefaultSelect": false,
              "stereoType": 0,
              "adaptationSet": [
                {
                  "id": 1,
                  "duration": 9800,
                  "representation": [
                    {
                      "id": 1,
                      "url": "https://v2.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_hd15_B98f58d747f83176207ebea3ef44e2d47.mp4?pkey=AAWeqmb62oSyZ50c8UC7VC5Qz9IdrAeSy-OkgIkNjmrByC2JE9ShTqK0Br94Kh4kucva_k6svOVXDi5wxBIqOsf56neqooRbyFUTL7_Bfz9eDmy66qql4OKG2g_xDJ9TAmY&tag=1-1653123292-unknown-0-nxvfqtc5nx-b01fd9c75906f201&clientCacheKey=3xa7hvqbt9rg9my_hd15.mp4&di=b70be6e3&bp=14734&tt=hd15&ss=vp",
                      "backupUrl": [
                        "https://v1.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_hd15_B98f58d747f83176207ebea3ef44e2d47.mp4?pkey=AAU_wkOOdrFCBvCiNIBdbWVYDPjtP6gGq3BJrIkTmOL6YNFRqj8yObN7jaNTk03qzEx_PhJBoJA5PlsP0v4QRfl25n1GOkXBbWVsVa-3Ttp9v3M2ZWzAYOI1ChQOaYTnWIA&tag=1-1653123292-unknown-1-kw5yel1g6q-87e8866e4ff8085b&clientCacheKey=3xa7hvqbt9rg9my_hd15.mp4&di=b70be6e3&bp=14734&tt=hd15&ss=vp"
                      ],
                      "maxBitrate": 3000,
                      "avgBitrate": 1123,
                      "width": 720,
                      "height": 1280,
                      "frameRate": 60,
                      "quality": 1.5,
                      "qualityType": "720p",
                      "qualityLabel": "高清",
                      "featureP2sp": false,
                      "hidden": false,
                      "disableAdaptive": false,
                      "defaultSelect": false,
                      "comment": "db4210b2fa736828/hd15",
                      "hdrType": 5,
                      "fileSize": 1375825
                    }
                  ]
                }
              ],
              "playInfo": {
              },
              "videoFeature": {
                "blurProbability": 0.5342053771018982,
                "blockyProbability": 0.5063997507095337,
                "avgEntropy": 6.799987115358052,
                "mosScore": 0.410698801279068
              }
            },
            "videoResource": {
              "h264": {
                "version": "1.0.0",
                "businessType": 2,
                "mediaType": 2,
                "videoId": "db4210b2fa736828",
                "hideAuto": false,
                "manualDefaultSelect": false,
                "stereoType": 0,
                "adaptationSet": [
                  {
                    "id": 1,
                    "duration": 9800,
                    "representation": [
                      {
                        "id": 1,
                        "url": "https://v1.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_b_B6252bd5a9470739c8cd7bdd930df2fe7.mp4?pkey=AAV-Ls4pObyzJAnPmKwGFakTMuL5IQHxi2A9D5tCMZZNQeO56JYh6R5XoRqvmqumX2miP9u5StC2vAzFJGk7Pfu5n4FSuGVF6zYF4QM3ss500Im4uvl85GOjH3e8-uUP4nY&tag=1-1653123292-unknown-0-evb4cjqdsd-e0aaac50f5d81fe8&clientCacheKey=3xa7hvqbt9rg9my_b.mp4&di=b70be6e3&bp=14734&tt=b&ss=vp",
                        "backupUrl": [
                          "https://v2.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_b_B6252bd5a9470739c8cd7bdd930df2fe7.mp4?pkey=AAWaeyZluCuBdOEKdkjBrPBoq3F66RISIunCqY8bx0kCv62ilXbBxW_O3npOaKuDuyUVJQt9UqzmobOf_G293udKnG2he77Gc-Qsb7LONZD56M08lqDNSY5DHH80iPePa0Y&tag=1-1653123292-unknown-1-h5waan2oie-68eb7ea79d3dff56&clientCacheKey=3xa7hvqbt9rg9my_b.mp4&di=b70be6e3&bp=14734&tt=b&ss=vp"
                        ],
                        "maxBitrate": 4900,
                        "avgBitrate": 3116,
                        "width": 720,
                        "height": 1280,
                        "frameRate": 60,
                        "quality": 1.5,
                        "qualityType": "720p",
                        "qualityLabel": "高清",
                        "featureP2sp": false,
                        "hidden": false,
                        "disableAdaptive": false,
                        "defaultSelect": false,
                        "comment": "db4210b2fa736828/b",
                        "hdrType": 5,
                        "fileSize": 3928959,
                        "bitratePattern": [
                          3207,
                          2421,
                          4435,
                          2248,
                          698
                        ]
                      }
                    ]
                  }
                ],
                "playInfo": {
                },
                "videoFeature": {
                  "blurProbability": 0.5342053771018982,
                  "blockyProbability": 0.5063997507095337,
                  "avgEntropy": 6.799987115358052,
                  "mosScore": 0.410698801279068
                }
              },
              "hevc": {
                "version": "1.0.0",
                "businessType": 2,
                "mediaType": 2,
                "videoId": "db4210b2fa736828",
                "hideAuto": false,
                "manualDefaultSelect": false,
                "stereoType": 0,
                "adaptationSet": [
                  {
                    "id": 1,
                    "duration": 9800,
                    "representation": [
                      {
                        "id": 1,
                        "url": "https://v2.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_hd15_B98f58d747f83176207ebea3ef44e2d47.mp4?pkey=AAWeqmb62oSyZ50c8UC7VC5Qz9IdrAeSy-OkgIkNjmrByC2JE9ShTqK0Br94Kh4kucva_k6svOVXDi5wxBIqOsf56neqooRbyFUTL7_Bfz9eDmy66qql4OKG2g_xDJ9TAmY&tag=1-1653123292-unknown-0-nxvfqtc5nx-b01fd9c75906f201&clientCacheKey=3xa7hvqbt9rg9my_hd15.mp4&di=b70be6e3&bp=14734&tt=hd15&ss=vp",
                        "backupUrl": [
                          "https://v1.kwaicdn.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_hd15_B98f58d747f83176207ebea3ef44e2d47.mp4?pkey=AAU_wkOOdrFCBvCiNIBdbWVYDPjtP6gGq3BJrIkTmOL6YNFRqj8yObN7jaNTk03qzEx_PhJBoJA5PlsP0v4QRfl25n1GOkXBbWVsVa-3Ttp9v3M2ZWzAYOI1ChQOaYTnWIA&tag=1-1653123292-unknown-1-kw5yel1g6q-87e8866e4ff8085b&clientCacheKey=3xa7hvqbt9rg9my_hd15.mp4&di=b70be6e3&bp=14734&tt=hd15&ss=vp"
                        ],
                        "maxBitrate": 3000,
                        "avgBitrate": 1123,
                        "width": 720,
                        "height": 1280,
                        "frameRate": 60,
                        "quality": 1.5,
                        "qualityType": "720p",
                        "qualityLabel": "高清",
                        "featureP2sp": false,
                        "hidden": false,
                        "disableAdaptive": false,
                        "defaultSelect": false,
                        "comment": "db4210b2fa736828/hd15",
                        "hdrType": 5,
                        "fileSize": 1375825
                      }
                    ]
                  }
                ],
                "playInfo": {
                },
                "videoFeature": {
                  "blurProbability": 0.5342053771018982,
                  "blockyProbability": 0.5063997507095337,
                  "avgEntropy": 6.799987115358052,
                  "mosScore": 0.410698801279068
                }
              }
            },
            "coverUrls": null,
            "timestamp": 1653048380883,
            "expTag": "1_i/2005176069751607249_xpcwebprofilexxnull0",
            "animatedCoverUrl": "https://p2.a.yximgs.com/upic/2022/05/20/20/BMjAyMjA1MjAyMDA1MjlfMTYzMDk5MjQyMF83NDg1ODQzMjM2N18xXzM=_animatedV5_B030c30368b91c5dbb16905b1b7a1a247.webp?tag=1-1653123292-xpcwebprofile-0-q5ngyizhmx-5fd4f168ee1e83a0&clientCacheKey=3xa7hvqbt9rg9my_animatedV5.webp&di=b70be6e3&bp=14734",
            "distance": null,
            "videoRatio": 0.5625,
            "liked": false,
            "stereoType": 0,
            "profileUserTopPhoto": null,
            "__typename": "PhotoEntity"
          },
          "canAddComment": 0,
          "llsid": "2005176069751607249",
          "status": 1,
          "currentPcursor": "",
          "__typename": "Feed"
        }
      ],
      "hostName": null,
      "pcursor": "1.648548115016E12",
      "__typename": "VisionProfilePhotoList"
    }
  }
}
```
