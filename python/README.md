# 涂鸦T4后台配置检查工具
## 使用方式
1. 安装python3环境，且安装`requests`库
2. 创建配置文件`config.json`
3. 执行`python3 check_tuya_config.py --config=./config.json`开始检测
## config.json配置说明
1. log_level

日志等级：默认INFO级别(20)，DEBUG(10)

2. csrf_token

涂鸦后台访问令牌：登录并选定好工作空间后浏览器F12获取某个接口的请求参数csrf-token。示例：

```shell
curl 'https://iot.tuya.com/micro-app/device/api/prodservice/linkage/combo/list' \
  -H 'authority: iot.tuya.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json; charset=UTF-8' \
  -H 'cookie: gTyPlatLang=zh; _tpmGuid=TY-a439153cfa8f6057; locale=zh; tz=8; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; operation_guide_flag=1; Hm_lvt_3be32b3bb5351c17025006d025cf42e7=1670223638; projectCode=; d41d8cd98f00b204e9800998ecf8427e=%5B%5D; 9f53cc1f59328e4c644eed5fa7ff64bc=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D; fast-sid=40apeiVpewKnSJv0poTEUKKBfLnXvpgr; 3b0beffbab3dcc336bd263560ac7939a=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsgCtrl%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%5D; e7078bd3ea5ed1f8e61b84d686fb92bf=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_i18n_product%22%5D; 3fd2fb499694a20ff69bb874ff51ba6a=%5B%22smart_menu_i18n_product%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_product_dev%22%5D; 9b1a6dd057338832b7c1452c9614ea87=%5B%22smart_menu_product_dev%22%5D; navbarShowExpand=1; router-prefix=; _tpmSid=a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27; _tpmSeqId=seq_id_902b2899514d4493; s-sid=s:ccadb473-7256-4906-9a33-82102015b757.mD5d9lRdw5h1tkPuh6M6tPcuV1sdSSKUu5G8/mg0Fv8; csr-test-csrf-token=gt424D4S-BR7tuXNmGH2_oZBBGEgc542GbNY; 3759e392f25da605e49643aa75517913=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_page_exp_intro%22%5D; csrf-token=zsACoD2u-Ko7urKPMQyiZNqsbI1ybT_UF_iY; csrf-token.sig=Uk2lMuS0iTnGb43Qzo2eofvZSMU' \
  -H 'csrf-token: zplketqg-TgSfYSi9yUE-Sgd9ZYWIKhjdrTY' \
  -H 'origin: https://iot.tuya.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://iot.tuya.com/device/equipment?pid=xvisauybxnryijqq' \
  -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw '{}' \
  --compressed
```

3. cookie

涂鸦后台访问令牌：登录并选定好工作空间后浏览器F12获取某个接口的请求参数cookie。示例：

```shell
curl 'https://iot.tuya.com/micro-app/device/api/prodservice/linkage/combo/list' \
  -H 'authority: iot.tuya.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json; charset=UTF-8' \
  -H 'cookie: gTyPlatLang=zh; _tpmGuid=TY-a439153cfa8f6057; locale=zh; tz=8; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; operation_guide_flag=1; Hm_lvt_3be32b3bb5351c17025006d025cf42e7=1670223638; projectCode=; d41d8cd98f00b204e9800998ecf8427e=%5B%5D; 9f53cc1f59328e4c644eed5fa7ff64bc=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D; fast-sid=40apeiVpewKnSJv0poTEUKKBfLnXvpgr; 3b0beffbab3dcc336bd263560ac7939a=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsgCtrl%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%5D; e7078bd3ea5ed1f8e61b84d686fb92bf=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_i18n_product%22%5D; 3fd2fb499694a20ff69bb874ff51ba6a=%5B%22smart_menu_i18n_product%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_product_dev%22%5D; 9b1a6dd057338832b7c1452c9614ea87=%5B%22smart_menu_product_dev%22%5D; navbarShowExpand=1; router-prefix=; _tpmSid=a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27; _tpmSeqId=seq_id_902b2899514d4493; s-sid=s:ccadb473-7256-4906-9a33-82102015b757.mD5d9lRdw5h1tkPuh6M6tPcuV1sdSSKUu5G8/mg0Fv8; csr-test-csrf-token=gt424D4S-BR7tuXNmGH2_oZBBGEgc542GbNY; 3759e392f25da605e49643aa75517913=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_page_exp_intro%22%5D; csrf-token=zsACoD2u-Ko7urKPMQyiZNqsbI1ybT_UF_iY; csrf-token.sig=Uk2lMuS0iTnGb43Qzo2eofvZSMU' \
  -H 'csrf-token: zplketqg-TgSfYSi9yUE-Sgd9ZYWIKhjdrTY' \
  -H 'origin: https://iot.tuya.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://iot.tuya.com/device/equipment?pid=xvisauybxnryijqq' \
  -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw '{}' \
  --compressed
```

4. config

检测产品配置（目前只支持**单个PID**进行检测），pid：产品PID，type：协议类型(public-涂鸦T4公版、custom_yinxing-涂鸦T4银星定制协议)

示例：
```json
{
    "log_level": 20,
    "csrf_token": "VQrl3QYX-UrMYl3TY3lpF6nvPUOjywIDPn2I",
    "cookie": "gTyPlatLang=zh; _tpmGuid=TY-a439153cfa8f6057; locale=zh; tz=8; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; operation_guide_flag=1; Hm_lvt_3be32b3bb5351c17025006d025cf42e7=1670223638; projectCode=; d41d8cd98f00b204e9800998ecf8427e=%5B%5D; 9f53cc1f59328e4c644eed5fa7ff64bc=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D; fast-sid=40apeiVpewKnSJv0poTEUKKBfLnXvpgr; 3b0beffbab3dcc336bd263560ac7939a=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsgCtrl%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%5D; e7078bd3ea5ed1f8e61b84d686fb92bf=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_i18n_product%22%5D; 3fd2fb499694a20ff69bb874ff51ba6a=%5B%22smart_menu_i18n_product%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_product_dev%22%5D; 9b1a6dd057338832b7c1452c9614ea87=%5B%22smart_menu_product_dev%22%5D; navbarShowExpand=1; router-prefix=; _tpmSid=a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27; 3759e392f25da605e49643aa75517913=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_page_exp_intro%22%5D; _tpmSeqId=seq_id_902b2899514d4493; s-sid=s:ccadb473-7256-4906-9a33-82102015b757.mD5d9lRdw5h1tkPuh6M6tPcuV1sdSSKUu5G8/mg0Fv8; csr-test-csrf-token=gt424D4S-BR7tuXNmGH2_oZBBGEgc542GbNY; csrf-token=dKuznA6I-zdMSrgt7JnVlfJKPKK23cEybems; csrf-token.sig=Ni5G5P-iniTUbKRAInL_ITT_BUk",
    "config": [
        {
            "pid": "xvisauybxnryijqq",
            "type": "public"
        }
    ]
}
```

## 示例日志
```text
INFO 2023-09-01 14:58:02,421 check_tuya_config.py[line:461] 【开始校验产品配置. pid=xvisauybxnryijqq】
INFO 2023-09-01 14:58:02,422 check_tuya_config.py[line:462] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:03,712 check_tuya_config.py[line:182] Step 1. 校验DP点是否存在. pid=xvisauybxnryijqq, result=True 
INFO 2023-09-01 14:58:03,712 check_tuya_config.py[line:185] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:05,477 check_tuya_config.py[line:182] Step 1. 校验DP点是否存在. pid=xvisauybxnryijqq, result=True 
INFO 2023-09-01 14:58:05,477 check_tuya_config.py[line:185] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:08,960 check_tuya_config.py[line:182] Step 1. 校验DP点是否存在. pid=xvisauybxnryijqq, result=True 
INFO 2023-09-01 14:58:08,960 check_tuya_config.py[line:185] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:08,960 check_tuya_config.py[line:199] Step 2. 校验DP点的参数设置是否正确. pid=xvisauybxnryijqq, dp_id=28, result=True
INFO 2023-09-01 14:58:08,960 check_tuya_config.py[line:203] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:12,417 check_tuya_config.py[line:225] Step 3. 校验DP点的消息推送是否正确. pid=xvisauybxnryijqq, dp_id=28, result=True 
INFO 2023-09-01 14:58:12,417 check_tuya_config.py[line:226] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
WARNING 2023-09-01 14:58:12,417 check_tuya_config.py[line:197] expect=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15], actual=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
INFO 2023-09-01 14:58:12,417 check_tuya_config.py[line:199] Step 2. 校验DP点的参数设置是否正确. pid=xvisauybxnryijqq, dp_id=101, result=False
INFO 2023-09-01 14:58:12,417 check_tuya_config.py[line:203] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ERROR 2023-09-01 14:58:12,417 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=101, message_code=10, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=101, message_code=11, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=101, message_code=12, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=101, message_code=13, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=101, message_code=14, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=101, message_code=15, find=False
INFO 2023-09-01 14:58:12,418 check_tuya_config.py[line:225] Step 3. 校验DP点的消息推送是否正确. pid=xvisauybxnryijqq, dp_id=101, result=False 
INFO 2023-09-01 14:58:12,418 check_tuya_config.py[line:226] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:12,418 check_tuya_config.py[line:199] Step 2. 校验DP点的参数设置是否正确. pid=xvisauybxnryijqq, dp_id=128, result=True
INFO 2023-09-01 14:58:12,418 check_tuya_config.py[line:203] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=2, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=3, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=4, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=5, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=6, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=7, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=8, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=9, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=10, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=11, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=12, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=14, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=15, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=16, find=False
ERROR 2023-09-01 14:58:12,418 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=18, find=False
ERROR 2023-09-01 14:58:12,428 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=20, find=False
ERROR 2023-09-01 14:58:12,428 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=21, find=False
ERROR 2023-09-01 14:58:12,428 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=22, find=False
ERROR 2023-09-01 14:58:12,428 check_tuya_config.py[line:222] 未配置消息推送或已配置未开启. dp_id=128, message_code=23, find=False
INFO 2023-09-01 14:58:12,428 check_tuya_config.py[line:225] Step 3. 校验DP点的消息推送是否正确. pid=xvisauybxnryijqq, dp_id=128, result=False 
INFO 2023-09-01 14:58:12,428 check_tuya_config.py[line:226] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:12,428 check_tuya_config.py[line:492] 【结束校验产品配置. pid=xvisauybxnryijqq, result=False】
INFO 2023-09-01 14:58:12,428 check_tuya_config.py[line:493] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
INFO 2023-09-01 14:58:12,428 check_tuya_config.py[line:497] 测试结果：[
    {
        "xvisauybxnryijqq": false
    }
]


```
## 