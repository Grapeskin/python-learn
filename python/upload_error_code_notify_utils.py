import requests

# cookies = {
# }
#
# headers = {
# }

cookies = {
    'gTyPlatLang': 'zh',
    '_tpmGuid': 'TY-a439153cfa8f6057',
    'locale': 'zh',
    'tz': '8',
    'notice_preferences': '2:',
    'notice_gdpr_prefs': '0,1,2:',
    'operation_guide_flag': '1',
    'Hm_lvt_3be32b3bb5351c17025006d025cf42e7': '1670223638',
    'projectCode': '',
    'd41d8cd98f00b204e9800998ecf8427e': '%5B%5D',
    '3b0beffbab3dcc336bd263560ac7939a': '%5B%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_cloud_develop_api_group%22%2C%22smart_menu_developer_platform_home%22%5D',
    '9f53cc1f59328e4c644eed5fa7ff64bc': '%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D',
    '3759e392f25da605e49643aa75517913': '%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_voice_access%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_authorization%22%2C%22smart_menu_product_deviceLog%22%5D',
    'fast-sid': '_DdvGmGsj3rZWzU6RPPlmuNXJove0A-m',
    '_tpmSeqId': 'seq_id_d9e3969f86c518d0',
    '_tpmSid': 'd9b48e296c2e2a8e718cacdda4858bd7d292953237645e1f5f15d79e6bffc264',
    'router-prefix': '',
    '__th_p_c': '1|1|1',
    'navbarShowExpand': '1',
    'e7078bd3ea5ed1f8e61b84d686fb92bf': '%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_dev%22%5D',
    's-sid': 's:8691d528-f58d-4cac-9528-2913dec3f176.P5lZzc5afVD2HWa8DJZ0rZQVXLun/I5s1XNnmZFIQzw',
    'csr-test-csrf-token': 'vmzADmDA-neZhTUJ5hgkYSE6fM4Vs1OSp_-w',
    'csrf-token': 'A45lvxg5-lK4kRpjTw5FilpXNdANNfFvP7SU',
    'csrf-token.sig': 'HmxhYnxqZlYyKEcAkNJuo-hqjxE',
}

headers = {
    'authority': 'iot.tuya.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'gTyPlatLang=zh; _tpmGuid=TY-a439153cfa8f6057; locale=zh; tz=8; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; operation_guide_flag=1; Hm_lvt_3be32b3bb5351c17025006d025cf42e7=1670223638; projectCode=; d41d8cd98f00b204e9800998ecf8427e=%5B%5D; 3b0beffbab3dcc336bd263560ac7939a=%5B%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_cloud_develop_api_group%22%2C%22smart_menu_developer_platform_home%22%5D; 9f53cc1f59328e4c644eed5fa7ff64bc=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D; 3759e392f25da605e49643aa75517913=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_voice_access%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_authorization%22%2C%22smart_menu_product_deviceLog%22%5D; fast-sid=_DdvGmGsj3rZWzU6RPPlmuNXJove0A-m; _tpmSeqId=seq_id_d9e3969f86c518d0; _tpmSid=d9b48e296c2e2a8e718cacdda4858bd7d292953237645e1f5f15d79e6bffc264; router-prefix=; __th_p_c=1|1|1; navbarShowExpand=1; e7078bd3ea5ed1f8e61b84d686fb92bf=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_dev%22%5D; s-sid=s:8691d528-f58d-4cac-9528-2913dec3f176.P5lZzc5afVD2HWa8DJZ0rZQVXLun/I5s1XNnmZFIQzw; csr-test-csrf-token=vmzADmDA-neZhTUJ5hgkYSE6fM4Vs1OSp_-w; csrf-token=A45lvxg5-lK4kRpjTw5FilpXNdANNfFvP7SU; csrf-token.sig=HmxhYnxqZlYyKEcAkNJuo-hqjxE',
    'csrf-token': 'vmzADmDA-neZhTUJ5hgkYSE6fM4Vs1OSp_-w',
    'origin': 'https://iot.tuya.com',
    'pragma': 'no-cache',
    'referer': 'https://iot.tuya.com/device/equipment',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# 32
# event_notify_code = {
#     "time_total_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_total_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_total_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_cur_point_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_cur_point_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_cur_point_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_point_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_point_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_point_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_area_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_area_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_area_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_auto_area_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_auto_area_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_auto_area_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_edge_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_edge_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "time_edge_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     "charge_ok_resume_clean": {"msg": {"cn": "充电完毕，继续清扫", "en": "Charging is completed, continue to clean"}, "code": 2},
#     "low_battery_find_charger": {"msg": {"cn": "电量不足，开始回充", "en": "Low Battery. Heading Home."}, "code": 3},
#     "back_charger_fail": {"msg": {"cn": "找不到回充座，停止回充", "en": "Unable to find charging base. Stop heading home"},
#                           "code": 4},
#     "cannot_upgrade": {"msg": {"cn": "请将机器放到充电座充电，并确保电量大于20%再升级",
#                                "en": "Please put the robot into the charging base for charging and make sure the battery is more than 20%."},
#                        "code": 5},
#     "clean_finish": {"msg": {"cn": "清扫结束，开始回充", "en": "Finished Cleaning. Heading Home."}, "code": 6},
#     "firmware_upgrade_fail": {"msg": {"cn": "升级失败，请重试", "en": "Upgrading failed. Please try again"}, "code": 7},
#     "firmware_upgrade_done": {"msg": {"cn": "升级成功", "en": "Successfully upgraded"}, "code": 8},
#     "collect_dust_full": {"msg": {"cn": "请及时清理尘袋", "en": "Please clean the dust bag in time "}, "code": 9},
#     "time_task_disable_in_silent_mode": {
#         "msg": {"cn": "勿扰时间段内，预约清扫未执行", "en": "Do Not Disturb time, schedule not implemented."}, "code": 11},
#     "collect_dust_start": {"msg": {"cn": "集尘中", "en": "Dust collecting"}, "code": 13},
#     "low_bat_need_poweroff": {"msg": {"cn": "电量不足，自动关机", "en": "Low Battery, Shutting Down"}, "code": 14},
#     "opt_during_upgrade": {"msg": {"cn": "系统升级中，请耐心等待", "en": "Please wait patiently while upgrading"}, "code": 17},
#     "mop_out": {"msg": {"cn": "拖布支架已取下，退出拖地模式", "en": "The mop support has been removed"}, "code": 25},
#     "mop_in": {"msg": {"cn": "拖布支架已安装，进入拖地模式", "en": "The mop support has been installed"}, "code": 26}
# }
event_notify_code = {
    "low_battery_to_clean": {"msg": {"cn": "低电清扫", "en": "clean cannot arrive"}, "code": 1},
    "restart_work_and_build_map": {"msg": {"cn": "定位失败,重新建图", "en": "restart work and build map"}, "code": 2},
    "try_poweroff_on_charger": {"msg": {"cn": "充电桩上无法关机", "en": "try power off on charger"}, "code": 3},
    "enter_silent_mode": {"msg": {"cn": "进入勿扰模式", "en": "enter silent mode"}, "code": 4},
    "time_to_work_start": {"msg": {"cn": "预约清扫开始", "en": "time to work start"}, "code": 5},
    "clean_finish": {"msg": {"cn": "清扫完成", "en": "clean finish"}, "code": 6},
    "back_charger_lost_pose": {"msg": {"cn": "回充定位失败", "en": "back charger lost pose"}, "code": 7},
    "charge_ok_resume_clean": {"msg": {"cn": "充电已完成继续清扫", "en": "charge ok resume clean"}, "code": 8},
    "time_task_disable": {"msg": {"cn": "当前有清扫任务预约启动失败", "en": "time task disable"}, "code": 9},
    "clean_lost_pose": {"msg": {"cn": "清扫定位失败", "en": "clean lost pose"}, "code": 10},
    "low_bat_need_recharge": {"msg": {"cn": "低电需要回充", "en": "low bat need recharge"}, "code": 11},
    "clean_cannot_arrive": {"msg": {"cn": "清扫区域无法到达", "en": "clean cannot arrive"}, "code": 12},
    "collect_dust_full": {"msg": {"cn": "工作站尘袋已满", "en": "collect dust full"}, "code": 14},
    "collect_dust_no_bag": {"msg": {"cn": "工作站未安装尘袋", "en": "collect dust no bag"}, "code": 15},
    "time_task_disable_in_silent_mode": {"msg": {"cn": "勿扰模式下定时任务不执行", "en": "time task disable in silent mode"},
                                         "code": 16},
    "collect_dust_no_fan": {"msg": {"cn": "工作站风机异常", "en": "collect dust no fan"}, "code": 18},
    "mop_out": {"msg": {"cn": "拖布移除事件", "en": "mop out"}, "code": 19},
    "collect_dust_done": {"msg": {"cn": "集尘完成", "en": "collect dust done"}, "code": 20},
    "pressure_too_high": {"msg": {"cn": "基站压力过高", "en": "pressure too high"}, "code": 21},
    "pressure_too_low": {"msg": {"cn": "基站压力过低", "en": "pressure too low"}, "code": 22},
}

#23
error_notify_code = {
    "left_wheel_err": {"msg": {"cn": "错误2：轮子模组异常，请查阅说明书或APP。", "en": "Error 2: Wheel Module Error. Please refer to the manual or APP."}, "code": 1},
    "middle_brush_stuck": {"msg": {"cn": "滚刷被卡住。", "en": "Rolling Brush Stuck"}, "code": 2},
    "right_wheel_err": {"msg": {"cn": "错误2：轮子模组异常，请查阅说明书或APP。", "en": "Error 2: Wheel Module Error. Please refer to the manual or APP."}, "code": 3},
    "left_wheel_stuck": {"msg": {"cn": "轮子被卡住。", "en": "Wheel Stuck"}, "code": 4},
    "right_wheel_stuck": {"msg": {"cn": "轮子被卡住。", "en": "Wheel Stuck"}, "code": 5},
    "side_brush_err": {"msg": {"cn": "错误3：边刷模组异常，请查阅说明书或APP。", "en": "Error 3: Side Brush Error. Please refer to the manual or APP."}, "code": 6},
    "side_brush_stuck": {"msg": {"cn": "边刷被卡住。", "en": "Side Brush Error"}, "code": 7},
    "tilt_do_task": {"msg": {"cn": "机器倾斜，请将机器放到水平地面启动", "en": "The machine tilts, please put the machine on the level ground to start it"}, "code": 8},
    "collision_stuck": {"msg": {"cn": "碰撞缓冲器被卡住。", "en": "Front Bumper Stuck"}, "code": 9},
    "no_dust_water_box": {"msg": {"cn": "二合一尘盒水箱缺失", "en": "Please replace the two in one dust box water tank"}, "code": 10},
    "11": {"code": 11},
    "drop": {"msg": {"cn": "悬崖传感器被遮挡，请擦拭", "en": "Anti-drop sensor blocked, please wipe"}, "code": 12},
    "middle_brush_err": {"msg": {"cn": "错误5：滚刷异常，请查阅说明书或APP。", "en": "Error 5: Rolling Brush Error. Please refer to the manual or APP."}, "code": 13},
    "lidar_protective_cover": {"msg": {"cn": "激光传感器被卡住或缠绕，请检查", "en": "The laser sensor is stuck or entangled, please check"}, "code": 14},
    "fan_err": {"msg": {"cn": "错误4：风机异常，请查阅说明书或APP。", "en": "Error 4: Suction Fan Error. Please refer to the manual or APP."}, "code": 15},
    "lidar_err": {"msg": {"cn": "错误7：点激光传感器异常，请查阅说明书或APP。", "en": "Error 7: Laser Sensor Error. Please refer to the manual or APP."}, "code": 16},
    "air_flue_blocked": {"msg": {"cn": "错误12：集尘座通道被堵住，请清理", "en": "Error 12: The passage of the dust collector is blocked, please clean up"}, "code": 17},
    "water_pump_err": {"msg": {"cn": "错误6：水泵异常，请查阅说明书或APP", "en": "Error 6: Water Pump Error"}, "code": 18},
    "physical_trapped": {"msg": {"cn": "机器被困，请移动到地面重新启动", "en": "The machine is trapped. Please put the machine on the ground to restart"}, "code": 19},
    "20": {"code": 20},
    "21": {"code": 21},
    "lidar_obscured": {"msg": {"cn": "点激光传感器被遮挡，请擦拭", "en": "Laser sensor blocked, please wipe"}, "code": 22},
    "water_box_empty": {"msg": {"cn": "错误15：水箱水量不足，请加水。", "en": "Error 15: Insufficient water. Add WaterInsufficient water. Add Water"}, "code": 23},
    "forbid_area": {"msg": {"cn": "启动机器遇到禁区。", "en": "Restricted area detected, please move to a new location to start"}, "code": 24},
    "battery_disconnect": {"msg": {"cn": "错误1：电池异常，请查阅说明书或APP。", "en": "Error 1: Battery Error. Please refer to the manual or APP."}, "code": 25},
    "pickup": {"msg": {"cn": "轮子悬空，请将机器放到地面启动", "en": "The wheel is suspended, please put the machine on the ground to start"}, "code": 26},
    "low_bat_poweroff": {"msg": {"cn": "电量过低，系统即将自动关机", "en": "Low Battery. Please charge and try again later."}, "code": 27},
    "28": {"code": 28},
    "29": {"code": 29},
}
# event_notify_code = {
#     "mop_in": {"msg": {"cn": "拖布支架已安装，进入拖地模式", "en": "The mop support has been installed"}, "code": 26}
# }
#
# error_notify_code = {
#     "low_bat_poweroff": {"msg": {"cn": "电量过低，系统即将自动关机", "en": "Low Battery. Please charge and try again later."}, "code": 27},
# }

def message_report():
    # 消息推送
    for k, v in event_notify_code.items():
        json_data = {
            'ruleExpr': {
                'name': '${device}',
                'productId': f'{product_key}',
                'conditions': [
                    {
                        'entityType': 1,
                        'entityId': f'{product_key}',
                        'expr': [
                            [
                                [
                                    '$dp128',
                                    '==',
                                    f'{v.get("code")}',
                                    None,
                                ],
                            ],
                        ],
                        'entitySubIds': '128',
                        'extraInfo': {
                            'durationTime': None,
                            'cumulativeTime': None,
                        },
                    },
                ],
                'actions': [
                    {
                        'actionExecutor': 'warnAction',
                        'executorProperty': {
                            'degree': '1',
                            'saveLog': True,
                            'notifyKinds': 3,
                            'content': f'{v.get("msg", {}).get("cn")}',
                            'sound': 0,
                            'link': 'panel',
                            'pushSpanUnit': 'h',
                            'pushSpanTime': 0,
                        },
                        'actionStrategy': 'repeat',
                    },
                ],
                'matchType': 3,
                'delayTime': None,
                'approvalStatus': 1,
                'iotAutoAlarm': True,
            },
            'productId': f'{product_key}',
            'langContent': {
                'name': {
                    '1': '${device}',
                    '4': '${device}',
                },
                'content': {
                    '1': f'{v.get("msg", {}).get("cn")}',
                    '4': f'{v.get("msg", {}).get("en")}',
                },
            },
        }

        response = requests.post('https://iot.tuya.com/micro-app/pmg/api/iot/device/msgpush/save', cookies=cookies,
                                 headers=headers, json=json_data)
        print(response.json())


def error_report():
    # 故障推送
    for k, v in error_notify_code.items():
        if v.get("msg"):
            json_data = {
                'ruleExpr': {
                    'name': '${device}',
                    'productId': f'{product_key}',
                    'conditions': [
                        {
                            'entityType': 1,
                            'entityId': f'{product_key}',
                            'expr': [
                                [
                                    [
                                        '$dp28',
                                        'bitEq',
                                        int(f'{v.get("code") - 1}'),
                                        None,
                                    ],
                                ],
                            ],
                            'entitySubIds': '28',
                            'extraInfo': {
                                'durationTime': None,
                                'cumulativeTime': None,
                            },
                        },
                    ],
                    'actions': [
                        {
                            'actionExecutor': 'warnAction',
                            'executorProperty': {
                                'degree': '3',
                                'saveLog': True,
                                'notifyKinds': 3,
                                'content': f'{v.get("msg", {}).get("cn")}',
                                'sound': 0,
                                'link': 'panel'
                            },
                            'actionStrategy': 'repeat',
                        },
                    ],
                    'matchType': 3,
                    'delayTime': None,
                    'approvalStatus': 1,
                    'iotAutoAlarm': True,
                },
                'productId': f'{product_key}',
                'langContent': {
                    'name': {
                        '1': '${device}',
                        '4': '${device}',
                    },
                    'content': {
                        '1': f'{v.get("msg", {}).get("cn")}',
                        '4': f'{v.get("msg", {}).get("en")}',
                    },
                },
            }

            response = requests.post('https://iot.tuya.com/micro-app/pmg/api/iot/device/msgpush/save', cookies=cookies,
                                     headers=headers, json=json_data)
            print(response.json())


def update_fault_dp_content():
    dp_id = 28
    json_data = {
        'dp': {
            'id': dp_id,
            'name': '故障告警',
            'code': 'fault',
            'desc': '故障含义见 银星 故障事件协议文档和多语言配置',
            'mode': 'rw',
            'property': {
                'type': 'bitmap',
                'maxlen': len(error_notify_code.keys()),
                'label': [key for key in error_notify_code.keys()],
            },
            'type': 'obj',
            'scope': 'fault',
            'attr': 0,
            'triggerEnable': False,
            'passiveEnable': False,
            'routeType': 0,
            'cloudlessEnable': False,
        },
        'productId': product_key,
    }

    response = requests.post('https://iot.tuya.com/micro-app/pmg/api/product/dp/dpUpdate/v2', cookies=cookies,
                             headers=headers, json=json_data)
    print(response.json())


"""
./event_tool -p -t /hardware/error -e error_kit_left_wheel_err -d {}
./event_tool -p -t /hardware/error -e error_middle_brush_stuck -d {}
./event_tool -p -t /hardware/error -e error_kit_right_wheel_err -d {}
./event_tool -p -t /hardware/error -e error_left_wheel_stuck -d {}
./event_tool -p -t /hardware/error -e error_right_wheel_stuck -d {}
./event_tool -p -t /hardware/error -e error_kit_side_brush_err -d {}
./event_tool -p -t /hardware/error -e error_side_brush_stuck -d {}
./event_tool -p -t /hardware/error -e error_tilt_do_task -d {}
./event_tool -p -t /hardware/error -e error_collision_stuck -d {}
./event_tool -p -t /event/robot_monitor -e no_dust_box_water_box_do_task -d {}
./event_tool -p -t /hardware/error -e error_drop -d {}
./event_tool -p -t /hardware/error -e error_kit_middle_brush_err -d {}
./event_tool -p -t /hardware/error -e error_lidar_protective_cover -d {}
./event_tool -p -t /hardware/error -e error_kit_fan_err -d {}
./event_tool -p -t /hardware/error -e error_kit_lidar_err -d {}
./event_tool -p -t /event/onboard_ui -e base_station_air_flue_blocked -d {}
./event_tool -p -t /hardware/error -e error_kit_water_pump_err -d {}
./event_tool -p -t /hardware/error -e error_physical_trapped -d {}
./event_tool -p -t /hardware/error -e error_kit_lidar_obscured -d {}
./event_tool -p -t /hardware/error -e error_water_box_empty -d {}
./event_tool -p -t /event/onboard_ui -e start_form_forbid_area -d {}
./event_tool -p -t /hardware/error -e error_battery_disconnect -d {}
./event_tool -p -t /event/robot_monitor -e pickup -d {}
./event_tool -p -t /event/onboard_ui -e low_bat_poweroff -d {}
./event_tool -p -t /event/onboard_ui -e time_total_clean_start -d {}
./event_tool -p -t /event/onboard_ui -e time_total_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_total_clean_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_cur_point_clean_start -d {}
./event_tool -p -t /event/onboard_ui -e time_cur_point_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_cur_point_clean_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_point_clean_start -d {}
./event_tool -p -t /event/onboard_ui -e time_point_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_point_clean_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_area_clean_start -d {}
./event_tool -p -t /event/onboard_ui -e time_area_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_area_clean_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_auto_area_clean_start -d {}
./event_tool -p -t /event/onboard_ui -e time_auto_area_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_auto_area_clean_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_edge_clean_start -d {}
./event_tool -p -t /event/onboard_ui -e time_edge_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e time_edge_clean_mop_start -d {}
./event_tool -p -t /event/onboard_ui -e charge_ok_resume_clean -d {}
./event_tool -p -t /event/onboard_ui -e low_battery_find_charger -d {}
./event_tool -p -t /event/onboard_ui -e back_charger_fail -d {}
./event_tool -p -t /event/onboard_ui -e cannot_upgrade -d {}
./event_tool -p -t /event/onboard_ui -e clean_finish -d {}
./event_tool -p -t /event/onboard_ui -e firmware_upgrade_fail -d {}
./event_tool -p -t /event/onboard_ui -e firmware_upgrade_done -d {}
./event_tool -p -t /event/onboard_ui -e collect_dust_full -d {}
./event_tool -p -t /event/timer -e time_task_disable_in_silent_mode -d {}
./event_tool -p -t /event/onboard_ui -e collect_dust_start -d {}
./event_tool -p -t /event/robot_monitor -e low_bat_need_poweroff -d {}
./event_tool -p -t /event/onboard_ui -e opt_during_upgrade -d {}
./event_tool -p -t /event/robot_monitor -e mop_out -d {}
./event_tool -p -t /event/robot_monitor -e mop_in -d {}
"""
if __name__ == '__main__':
    """
    0. 更新请求header、cookies
    1. 更新故障DP点定义
    2. 更新消息DP点定义
    3. 新增故障、消息推送
    4. 新增故障、消息文案多语言
    """
    product_key = "z8arz33rah6vwq8b"

    message_report()
    # error_report()
    # update_fault_dp_content()
