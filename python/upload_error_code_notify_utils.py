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
    '9f53cc1f59328e4c644eed5fa7ff64bc': '%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D',
    'fast-sid': '40apeiVpewKnSJv0poTEUKKBfLnXvpgr',
    '3b0beffbab3dcc336bd263560ac7939a': '%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsgCtrl%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%5D',
    'navbarShowExpand': '1',
    'router-prefix': '',
    'e7078bd3ea5ed1f8e61b84d686fb92bf': '%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_i18n_product%22%5D',
    '3fd2fb499694a20ff69bb874ff51ba6a': '%5B%22smart_menu_i18n_product%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_product_dev%22%5D',
    '9b1a6dd057338832b7c1452c9614ea87': '%5B%22smart_menu_product_dev%22%5D',
    '_tpmSeqId': 'seq_id_9f000751877e873b',
    '_tpmSid': 'a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27',
    's-sid': 's:9965a899-31f9-4e96-98e6-3b870481bf65.MpDHxu2NGQaTQcGozM9e/1Rrl6W2SC4II/SmmkXCXk4',
    'csr-test-csrf-token': 'OfBQ4kwK-hI4deRyNT4S61zw9NLmBg3sDwRE',
    '3759e392f25da605e49643aa75517913': '%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_account%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_developer_platform_home%22%2C%22smart_menu_cloud_develop_data_message%22%5D',
    'csrf-token': 'G1guddi4-_c1uYJqltN0CC-5hzaYuM87Pk7A',
    'csrf-token.sig': 'n00dIVyxk8eC-6Jj47949NYkyvE',
}

headers = {
    'authority': 'iot.tuya.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'gTyPlatLang=zh; _tpmGuid=TY-a439153cfa8f6057; locale=zh; tz=8; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; operation_guide_flag=1; Hm_lvt_3be32b3bb5351c17025006d025cf42e7=1670223638; projectCode=; d41d8cd98f00b204e9800998ecf8427e=%5B%5D; 9f53cc1f59328e4c644eed5fa7ff64bc=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D; fast-sid=40apeiVpewKnSJv0poTEUKKBfLnXvpgr; 3b0beffbab3dcc336bd263560ac7939a=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsgCtrl%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%5D; navbarShowExpand=1; router-prefix=; e7078bd3ea5ed1f8e61b84d686fb92bf=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_i18n_product%22%5D; 3fd2fb499694a20ff69bb874ff51ba6a=%5B%22smart_menu_i18n_product%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_product_dev%22%5D; 9b1a6dd057338832b7c1452c9614ea87=%5B%22smart_menu_product_dev%22%5D; _tpmSeqId=seq_id_9f000751877e873b; _tpmSid=a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27; s-sid=s:9965a899-31f9-4e96-98e6-3b870481bf65.MpDHxu2NGQaTQcGozM9e/1Rrl6W2SC4II/SmmkXCXk4; csr-test-csrf-token=OfBQ4kwK-hI4deRyNT4S61zw9NLmBg3sDwRE; 3759e392f25da605e49643aa75517913=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_account%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_developer_platform_home%22%2C%22smart_menu_cloud_develop_data_message%22%5D; csrf-token=G1guddi4-_c1uYJqltN0CC-5hzaYuM87Pk7A; csrf-token.sig=n00dIVyxk8eC-6Jj47949NYkyvE',
    'csrf-token': 'S7TiC7Oc-Ywfrmaw33jY0czNrJwu62gGNJgs',
    'origin': 'https://iot.tuya.com',
    'pragma': 'no-cache',
    'referer': 'https://iot.tuya.com/pmg/step?id=rctih3aredueiuea',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
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
# event_notify_code = {
#     "low_battery_to_clean": {"msg": {"cn": "低电清扫", "en": "clean cannot arrive"}, "code": 1},
#     "restart_work_and_build_map": {"msg": {"cn": "定位失败,重新建图", "en": "restart work and build map"}, "code": 2},
#     "try_poweroff_on_charger": {"msg": {"cn": "充电桩上无法关机", "en": "try power off on charger"}, "code": 3},
#     "enter_silent_mode": {"msg": {"cn": "进入勿扰模式", "en": "enter silent mode"}, "code": 4},
#     "time_to_work_start": {"msg": {"cn": "预约清扫开始", "en": "time to work start"}, "code": 5},
#     "clean_finish": {"msg": {"cn": "清扫完成", "en": "clean finish"}, "code": 6},
#     "back_charger_lost_pose": {"msg": {"cn": "回充定位失败", "en": "back charger lost pose"}, "code": 7},
#     "charge_ok_resume_clean": {"msg": {"cn": "充电已完成继续清扫", "en": "charge ok resume clean"}, "code": 8},
#     "time_task_disable": {"msg": {"cn": "当前有清扫任务预约启动失败", "en": "time task disable"}, "code": 9},
#     "clean_lost_pose": {"msg": {"cn": "清扫定位失败", "en": "clean lost pose"}, "code": 10},
#     "low_bat_need_recharge": {"msg": {"cn": "低电需要回充", "en": "low bat need recharge"}, "code": 11},
#     "clean_cannot_arrive": {"msg": {"cn": "清扫区域无法到达", "en": "clean cannot arrive"}, "code": 12},
#     "collect_dust_full": {"msg": {"cn": "工作站尘袋已满", "en": "collect dust full"}, "code": 14},
#     "collect_dust_no_bag": {"msg": {"cn": "工作站未安装尘袋", "en": "collect dust no bag"}, "code": 15},
#     "time_task_disable_in_silent_mode": {"msg": {"cn": "勿扰模式下定时任务不执行", "en": "time task disable in silent mode"},
#                                          "code": 16},
#     "collect_dust_no_fan": {"msg": {"cn": "工作站风机异常", "en": "collect dust no fan"}, "code": 18},
#     "mop_out": {"msg": {"cn": "拖布移除事件", "en": "mop out"}, "code": 19},
#     "collect_dust_done": {"msg": {"cn": "集尘完成", "en": "collect dust done"}, "code": 20},
#     "pressure_too_high": {"msg": {"cn": "基站压力过高", "en": "pressure too high"}, "code": 21},
#     "pressure_too_low": {"msg": {"cn": "基站压力过低", "en": "pressure too low"}, "code": 22},
# }

#消息推送（公版）
event_notify_code = {
    "low_battery_to_clean": {"msg": {"cn": "低电清扫", "en": "low battery to clean"}, "code": 1},
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
    "side_brush_stuck": {"msg": {"cn": "边刷卡住", "en": "side brush stuck"}, "code": 23},
}

#23 消息推送（YX）
# error_notify_code = {
#     "left_wheel_err": {"msg": {"cn": "错误2：轮子模组异常，请查阅说明书或APP。", "en": "Error 2: Wheel Module Error. Please refer to the manual or APP."}, "code": 1},
#     "middle_brush_stuck": {"msg": {"cn": "滚刷被卡住。", "en": "Rolling Brush Stuck"}, "code": 2},
#     "right_wheel_err": {"msg": {"cn": "错误2：轮子模组异常，请查阅说明书或APP。", "en": "Error 2: Wheel Module Error. Please refer to the manual or APP."}, "code": 3},
#     "left_wheel_stuck": {"msg": {"cn": "轮子被卡住。", "en": "Wheel Stuck"}, "code": 4},
#     "right_wheel_stuck": {"msg": {"cn": "轮子被卡住。", "en": "Wheel Stuck"}, "code": 5},
#     "side_brush_err": {"msg": {"cn": "错误3：边刷模组异常，请查阅说明书或APP。", "en": "Error 3: Side Brush Error. Please refer to the manual or APP."}, "code": 6},
#     "side_brush_stuck": {"msg": {"cn": "边刷被卡住。", "en": "Side Brush Error"}, "code": 7},
#     "tilt_do_task": {"msg": {"cn": "机器倾斜，请将机器放到水平地面启动", "en": "The machine tilts, please put the machine on the level ground to start it"}, "code": 8},
#     "collision_stuck": {"msg": {"cn": "碰撞缓冲器被卡住。", "en": "Front Bumper Stuck"}, "code": 9},
#     "no_dust_water_box": {"msg": {"cn": "二合一尘盒水箱缺失", "en": "Please replace the two in one dust box water tank"}, "code": 10},
#     "11": {"code": 11},
#     "drop": {"msg": {"cn": "悬崖传感器被遮挡，请擦拭", "en": "Anti-drop sensor blocked, please wipe"}, "code": 12},
#     "middle_brush_err": {"msg": {"cn": "错误5：滚刷异常，请查阅说明书或APP。", "en": "Error 5: Rolling Brush Error. Please refer to the manual or APP."}, "code": 13},
#     "lidar_protective_cover": {"msg": {"cn": "激光传感器被卡住或缠绕，请检查", "en": "The laser sensor is stuck or entangled, please check"}, "code": 14},
#     "fan_err": {"msg": {"cn": "错误4：风机异常，请查阅说明书或APP。", "en": "Error 4: Suction Fan Error. Please refer to the manual or APP."}, "code": 15},
#     "lidar_err": {"msg": {"cn": "错误7：点激光传感器异常，请查阅说明书或APP。", "en": "Error 7: Laser Sensor Error. Please refer to the manual or APP."}, "code": 16},
#     "air_flue_blocked": {"msg": {"cn": "错误12：集尘座通道被堵住，请清理", "en": "Error 12: The passage of the dust collector is blocked, please clean up"}, "code": 17},
#     "water_pump_err": {"msg": {"cn": "错误6：水泵异常，请查阅说明书或APP", "en": "Error 6: Water Pump Error"}, "code": 18},
#     "physical_trapped": {"msg": {"cn": "机器被困，请移动到地面重新启动", "en": "The machine is trapped. Please put the machine on the ground to restart"}, "code": 19},
#     "20": {"code": 20},
#     "21": {"code": 21},
#     "lidar_obscured": {"msg": {"cn": "点激光传感器被遮挡，请擦拭", "en": "Laser sensor blocked, please wipe"}, "code": 22},
#     "water_box_empty": {"msg": {"cn": "错误15：水箱水量不足，请加水。", "en": "Error 15: Insufficient water. Add WaterInsufficient water. Add Water"}, "code": 23},
#     "forbid_area": {"msg": {"cn": "启动机器遇到禁区。", "en": "Restricted area detected, please move to a new location to start"}, "code": 24},
#     "battery_disconnect": {"msg": {"cn": "错误1：电池异常，请查阅说明书或APP。", "en": "Error 1: Battery Error. Please refer to the manual or APP."}, "code": 25},
#     "pickup": {"msg": {"cn": "轮子悬空，请将机器放到地面启动", "en": "The wheel is suspended, please put the machine on the ground to start"}, "code": 26},
#     "low_bat_poweroff": {"msg": {"cn": "电量过低，系统即将自动关机", "en": "Low Battery. Please charge and try again later."}, "code": 27},
#     "28": {"code": 28},
#     "29": {"code": 29},
# }
# 普通故障
normal_error_notify_code = {
    "low_power": {"msg": {"cn": "电量低启动回充", "en": "low battery find charger"}, "code": 1},
    "poweroff": {"msg": {"cn": "低电关机", "en": "low bat power off"}, "code": 2},
    "wheel_trap": {"msg": {"cn": "底盘通信异常", "en": "universal wheel stuck"}, "code": 3},
    "cannot_upgrade": {"msg": {"cn": "不满足升级条件", "en": "cannot upgrade"}, "code": 4},
    "collision_stuck": {"msg": {"cn": "前撞异常", "en": "collision stuck"}, "code": 5},
    "dust_station_full": {"msg": {"cn": "集尘站满", "en": "dust station full"}, "code": 6},
    "tile_error": {"msg": {"cn": "请勿倾斜面上启动", "en": "tilt do task error"}, "code": 7},
    "lidar_speed_err": {"msg": {"cn": "雷达上盖异常", "en": "lidar protective cover error"}, "code": 8},
    "lidar_cover": {"msg": {"cn": "请检查顶部雷达是否有被遮蔽或者卡住 雷达堵转", "en": "Please check if the top lidar is obstructed or stuck"}, "code": 9},
    "lidar_point_err": {"msg": {"cn": "雷达被遮挡", "en": "kit lidar obscured"}, "code": 10},
    "front_wall_dirty": {"msg": {"cn": "检测到正前方避障传感器脏", "en": "front wall dirty error"}, "code": 11},
    "psd_dirty": {"msg": {"cn": "沿墙传感器异常", "en": "psd dirty error"}, "code": 12},
    "middle_sweep": {"msg": {"cn": "中刷卡住", "en": "middle brush stuck"}, "code": 13},
    "side_sweep": {"msg": {"cn": "边刷卡住", "en": "error side brush stuck"}, "code": 14},
    "fan_speed": {"msg": {"cn": "风机卡住", "en": "fan stuck"}, "code": 15},
    "dustbox_out": {"msg": {"cn": "尘盒水箱震动电机移除", "en": "dust box water box vibration motor out"}, "code": 16},
    "dustbox_full": {"msg": {"cn": "尘盒已满", "en": "garbage box full"}, "code": 17},
    "no_dust_box": {"msg": {"cn": "尘盒水箱震动电机未安装无法启动", "en": "no dust box water box vibration motor do task"}, "code": 18},
    "dustbox_fullout": {"msg": {"cn": "取出已满尘盒", "en": "garbage box full out"}, "code": 19},
    "trapped": {"msg": {"cn": "机器被困", "en": "physical trapped"}, "code": 20},
    "pick_up": {"msg": {"cn": "离地检测异常", "en": "pick up"}, "code": 21},
    "no_dust_water_box": {"msg": {"cn": "尘盒水箱未安装无法启动任务", "en": "no dust box water box do task"}, "code": 22},
    "water_box_empty": {"msg": {"cn": "检测到水箱中水量不足事件", "en": "water box empty"}, "code": 23},
    "forbid_area": {"msg": {"cn": "在禁区中无法启动工作", "en": "start form forbid area"}, "code": 24},
    "land_check": {"msg": {"cn": "地检异常", "en": "error drop"}, "code": 25},
    "findcharge_fail": {"msg": {"cn": "回充失败", "en": "back charger fail"}, "code": 26},
    "battery_err": {"msg": {"cn": "电池未连接异常", "en": "error battery disconnect"}, "code": 27},
    "kit_wheel": {"msg": {"cn": "主轮工作异常", "en": "kit universal wheel err"}, "code": 28},
    "kit_lidar": {"msg": {"cn": "雷达异常", "en": "kit lidar err"}, "code": 29},
    "kit_water_pump": {"msg": {"cn": "水泵异常", "en": "error kit water pump err"}, "code": 30},
}
# 扩展故障
error_notify_code = {
    "1": {"code": 1},
    "kit_middle_brush": {"msg": {"cn": "中刷短路", "en": "middle brush err"}, "code": 2},
    "kit_side_brush": {"msg": {"cn": "边刷短路", "en": "side brush err"}, "code": 3},
    "kit_fan": {"msg": {"cn": "风机短路", "en": "kit fan err"}, "code": 4},
    "kit_vibration": {"msg": {"cn": "震动电机短路", "en": "kit vibration motor err"}, "code": 5},
    "vibration_stuck": {"msg": {"cn": "震动电机卡住", "en": "vibration motor stuck"}, "code": 6},
    "no_mop": {"msg": {"cn": "没有安装拖布无法启动任务", "en": "no mop do task"}, "code": 7},
    "8": {"code": 8},
    "rug_start": {"msg": {"cn": "地毯启动报错", "en": "rug start error"}, "code": 9},
    "rocker_switch_off": {"msg": {"cn": "请打开船型开关", "en": "please open rocker switch"}, "code": 10},
    "l_mop_err": {"msg": {"cn": "左拖布短路", "en": "left mop err"}, "code": 11},
    "r_mop_err": {"msg": {"cn": "右拖布短路", "en": "right mop err"}, "code": 12},
    "l_mop_stuck": {"msg": {"cn": "左拖布卡住", "en": "left mop stuck"}, "code": 13},
    "r_mop_stuck": {"msg": {"cn": "右拖布卡住", "en": "right mop stuck"}, "code": 14},
    "base_water_not_in": {"msg": {"cn": "基站没有清水箱", "en": "base station clean water tank not in"}, "code": 15},
    "double_mop_stuck": {"msg": {"cn": "双旋转抹布电机卡住", "en": "double rotate rag motor stuck"}, "code": 16},
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


def error_report(dp_int: int = 28, is_extend: bool = False):
    # 故障推送
    code_map = normal_error_notify_code if not is_extend else error_notify_code
    for k, v in code_map.items():
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
                                        f'$dp{dp_int}',
                                        'bitEq',
                                        int(f'{v.get("code") - 1}'),
                                        None,
                                    ],
                                ],
                            ],
                            'entitySubIds': f'{dp_int}',
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


def update_fault_dp_content(dp_id: int = 28):
    # dp_id = 28
    json_data = {
        'dp': {
            'id': dp_id,
            'name': '扩展故障上报',
            'code': 'fault_extend_1',
            'desc': '',
            'mode': 'ro',
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

def get_protocol_list():
    json_data = {
        'productId': 'rctih3aredueiuea',
    }

    response = requests.post('https://iot.tuya.com/micro-app/pmg/api/product/schemaGetStd/V2', cookies=cookies,
                             headers=headers, json=json_data)



if __name__ == '__main__':
    """
    0. 更新请求header、cookies
    1. 更新故障DP点定义
    2. 更新消息DP点定义
    3. 新增故障、消息推送
    4. 新增故障、消息文案多语言
    """
    product_key = "ayvpa76vrvcpqm4r"
    # # error_dp_id = 156
    # error_dp_id = 28
    # # error_dp_id = 101
    # is_extend = True
    # # 消息推送128
    # message_report()
    # # 扩展故障101
    # update_fault_dp_content(101)
    # error_report(101, True)
    # # 普通故障28
    # # update_fault_dp_content(28)
    # error_report(28, False)

    
