import json

import requests

# cookies = {
# }
#
# headers = {
# }


cookies = {
    'gTyPlatLang': 'zh',
    '_tpmGuid': 'TY-04cdd7cf42ebf998',
    'tz': '8',
    'operation_guide_flag': '1',
    '3fb1c6e6e8ffbb469817430dea4f80aa': '%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%5D',
    '__th_p_c': '1|1|1',
    'router-prefix': '',
    'csr-test-csrf-token': 'NnNlYidZ-61fDYsdvOCGOo2BK8JLvzUQb2BQ',
    'region': 'AY',
    'fast-sid': 'GcxlJWf3f2o5Q_mDCWuEpfrmJPKdbwXS',
    's-sid': 's:7a771995-8d16-4e82-bfd5-d181d23dd224.tYYKW/020HysPp/CfUjmG4Mrz9lgdYDYstEUHss5wxY',
    '_tpmSid': 'a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27',
    '_tpmSeqId': 'seq_id_4d39c76e70839d2a',
    '_iss_hist': '%5B%7B%223759e392f25da605e49643aa75517913%22%3A%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_subDeviceDetail%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceFirmwareManage%22%5D%7D%2C%7B%2279d9fc122aa5a50e9981cbb96d9fcd75%22%3A%5B%22smart_menu_product_dev%22%2C%22smart_menu_authorization%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_subDeviceDetail%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%5D%7D%2C%7B%22a02468cc451e615d22d9c07c6f702d32%22%3A%5B%22smart_menu_i18n_product%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_appserviceAppList%22%5D%7D%5D',
    'csrf-token': 'R5MDnVTQ-WVtltXi_3cD2UvLByjO8ZAeDuWo',
    'csrf-token.sig': 'gkPULtWAvFmDC2Y42i1devXjEBc',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'baggage': 'sentry-environment=prod,sentry-release=20240328-032443221-29f0495f9a,sentry-public_key=34661fc563c248d7a70360279b4206b0,sentry-trace_id=d55b4bd77eed4d9d869530caf21135b0,sentry-sample_rate=1,sentry-sampled=true',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'gTyPlatLang=zh; _tpmGuid=TY-04cdd7cf42ebf998; tz=8; operation_guide_flag=1; 3fb1c6e6e8ffbb469817430dea4f80aa=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%5D; __th_p_c=1|1|1; router-prefix=; csr-test-csrf-token=NnNlYidZ-61fDYsdvOCGOo2BK8JLvzUQb2BQ; region=AY; fast-sid=GcxlJWf3f2o5Q_mDCWuEpfrmJPKdbwXS; s-sid=s:7a771995-8d16-4e82-bfd5-d181d23dd224.tYYKW/020HysPp/CfUjmG4Mrz9lgdYDYstEUHss5wxY; _tpmSid=a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27; _tpmSeqId=seq_id_4d39c76e70839d2a; _iss_hist=%5B%7B%223759e392f25da605e49643aa75517913%22%3A%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_subDeviceDetail%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceFirmwareManage%22%5D%7D%2C%7B%2279d9fc122aa5a50e9981cbb96d9fcd75%22%3A%5B%22smart_menu_product_dev%22%2C%22smart_menu_authorization%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_subDeviceDetail%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%5D%7D%2C%7B%22a02468cc451e615d22d9c07c6f702d32%22%3A%5B%22smart_menu_i18n_product%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_appserviceAppList%22%5D%7D%5D; csrf-token=R5MDnVTQ-WVtltXi_3cD2UvLByjO8ZAeDuWo; csrf-token.sig=gkPULtWAvFmDC2Y42i1devXjEBc',
    'csrf-token': 'aa7CcGjY-2yFvqCNAEahlyrdMSU342idXwhU',
    'origin': 'https://iot.tuya.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://iot.tuya.com/device/equipment?tab=customer',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'd55b4bd77eed4d9d869530caf21135b0-b8e81d9e3f08999b-1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


# 32 （YX）
# event_notify_code = {
#     "time_total_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_total_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_total_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_cur_point_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_cur_point_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_cur_point_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_point_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_point_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_point_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_area_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_area_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_area_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_auto_area_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_auto_area_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_auto_area_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_edge_clean_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_edge_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#     # "time_edge_clean_mop_start": {"msg": {"cn": "开始预约清扫", "en": "Start Scheduled Cleaning"}, "code": 1},
#
#
#
#
#
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
# 32 （YX）20240112
# event_notify_code = {
#     "1": {"msg": {"cn": "开始预约清扫", "en": "Start scheduled cleaning"}, "code": 1},
#     "2": {"msg": {"cn": "充电完毕，继续清扫", "en": "After charging, continue cleaning"}, "code": 2},#charge_ok_resume_clean
#     "3": {"msg": {"cn": "电量不足，开始回充", "en": "Insufficient battery, start recharging"}, "code": 3},#low_battery_find_charger
#     "4": {"msg": {"cn": "找不到充电座，停止回充", "en": "Unable to find charging base."}, "code": 4},#back_charger_fail
#     "5": {"msg": {"cn": "请将机器放到充电座充电，并确保电量大于20%再升级", "en": "Please put the device on the charging stand to charge, and make sure the power is greater than 20% before upgrading"}, "code": 5},#cannot_upgrade
#     "6": {"msg": {"cn": "清扫结束，开始回充", "en": "After cleaning, start recharging"}, "code": 6},#clean_finish
#     "7": {"msg": {"cn": "升级失败，请重试", "en": "Upgrade failed, please try again."}, "code": 7},#firmware_upgrade_fail
#     "8": {"msg": {"cn": "升级成功", "en": "Update successed"}, "code": 8},#firmware_upgrade_done
#     "9": {"msg": {"cn": "请及时清理尘袋", "en": "Please clean the dust bag in time"}, "code": 9},#collect_dust_full
#     "10": {"msg": {"cn": "勿扰时间段内，断点续扫未执行", "en": "During the do not disturb time period, the breakpoint continuous scan is not executed"}, "code": 10},#forbid_mode_not_resume_clean
#     "11": {"msg": {"cn": "勿扰时间段内，预约清扫未执行", "en": "During the Do Not Disturb time period, scheduled cleaning has not been performed"}, "code": 11},#time_task_disable_in_silent_mode
#     "12": {"msg": {"cn": "机器人在工作中，预约未执行", "en": "Robot is working, schedule not implemented"}, "code": 12},#time_task_disable
#     # "13": {"msg": {"cn": "地图不完整，预约未执行", "en": "The map is incomplete, reservation not executed"}, "code": 13},#--不支持
#     "14": {"msg": {"cn": "电量不足，自动关机", "en": "Insufficient battery, automatic shutdown"}, "code": 14},#low_bat_need_poweroff
#     "15": {"msg": {"cn": "气压传感器失效，请注意清理尘袋", "en": "The dust bag is full. Please change it with a new one."}, "code": 15},#collect_dust_full
#     # "16": {"msg": {"cn": "重定位失败，停止工作", "en": "Relocation failed, stop working"}, "code": 16},--不支持
#     "17": {"msg": {"cn": "机器电量过低，无法启动", "en": "The machine's battery is too low to start"}, "code": 17}, #low_battery_to_clean #low_battery_to_clean_on_charger
#     # "18": {"msg": {"cn": "地图不完整，无法执行指哪扫哪。", "en": "Incomplete map, unable to perform Pin n Go"}, "code": 18}, --不支持
#     "19": {"msg": {"cn": "系统升级中，请耐心等待", "en": "Please wait patiently while upgrading"}, "code": 19},#opt_during_upgrade
#     "20": {"msg": {"cn": "集尘中", "en": "Dust collecting"}, "code": 20},#collect_dust_start
#     "25": {"msg": {"cn": "拖布支架已取下，退出拖地模式", "en": "The mop support has been removed"}, "code": 25},#mop_out
#     "26": {"msg": {"cn": "拖布支架已安装，进入拖地模式", "en": "The mop support has been installed"}, "code": 26}#mop_in
# }
# 公版
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

#--------YX故障-----------#
#23 故障推送（YX）
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
#     "dust_no_bag": {"msg": {"cn": "电量过低，系统即将自动关机", "en": "Low Battery. Please charge and try again later."},"code": 29},
# }
# extend_error_notify_code = {
#
# }
#23 故障推送（YX）20210112
error_notify_code = {
    "left_wheel_err": {"msg": {"cn": "轮子模组异常，请查阅说明书或APP。", "en": "Wheel Motor Error."}, "code":1 },#error_kit_left_wheel_err
    "middle_brush_stuck": {"msg": {"cn": "滚刷被卡住。", "en": "Main Brush Stuck."}, "code":2 },#error_middle_brush_stuck
    "drop": {"msg": {"cn": "检测到悬崖边，请放置到水平地面启动。", "en": "Cliff edge detected, please place to level ground to start."}, "code":3 },#error_drop
    "left_wheel_stuck": {"msg": {"cn": "轮子被卡住。", "en": "Wheel Stuck."}, "code":4 },#error_left_wheel_stuck
    "clean_cannot_arrive": {"msg": {"cn": "无法到达清扫区域，请检查", "en": "Unable to reach sweeping area, please check."}, "code":5 },#clean_cannot_arrive
    "side_brush_err": {"msg": {"cn": "错误3：边刷模组异常，请查阅说明书或APP。", "en": "Side Brush Error."}, "code":6 },#error_kit_side_brush_err
    "side_brush_stuck": {"msg": {"cn": "边刷被卡住。", "en": "Side Brush Stuck."}, "code":7 },#side_brush_stuck_message #error_side_brush_stuck
    "tilt_do_task": {"msg": {"cn": "机器倾斜，请将机器放到水平地面启动", "en": "Device Tilted."}, "code":8 },#error_tilt_do_task #error_kit_lidar_tilt
    "collision_stuck": {"msg": {"cn": "碰撞缓冲器被卡住。", "en": "Front Bumper Stuck."}, "code":9 },#error_collision_stuck
    "no_dust_box": {"msg": {"cn": "尘盒缺失", "en": "Dust box missing."}, "code":10 }, #no_dust_box_do_task #no_dust_box_water_box_do_task
    "no_water_box": {"msg": {"cn": "水箱缺失", "en": "Water tank or filler box missing."}, "code":11 },#no_water_box_do_task
    "12": {"msg": {"cn": "悬崖传感器被遮挡，请擦拭", "en": "Anti-drop sensor blocked, please wipe."}, "code":12 },#error_drop
    "middle_brush_err": {"msg": {"cn": "滚刷异常，请查阅说明书或APP。", "en": "Main Brush Error."}, "code":13 },#error_kit_middle_brush_err
    "lidar_err": {"msg": {"cn": "激光传感器被卡住或短路，请检查。", "en": "Laser Sensor Error,please check."}, "code":14 }, #error_kit_lidar_err
    "fan_err": {"msg": {"cn": "风机异常，请查阅说明书或APP。", "en": "Suction Motor Error.Please try cleaning the dust box and restarting the robot."}, "code":15 },#error_kit_fan_err
    "lidar_obscured": {"msg": {"cn": "激光传感器异常，请清理或将机器搬到新环境启动。", "en": "Laser Sensor Error.please clean the laser sensor."}, "code":16 },#error_kit_lidar_obscured
    "air_flue_blocked": {"msg": {"cn": "集尘座通道被堵住，请清理", "en": "The passage of the dust collector is blocked,please clean up."}, "code":17 }, #base_station_air_flue_blocked
    "water_pump_err": {"msg": {"cn": "水泵异常，请查阅说明书或APP", "en": "Water Pump Error.Please try reinstalling the water tank and restarting the machine."}, "code":18 },#error_kit_water_pump_err
    "physical_trapped": {"msg": {"cn": "机器被困，请移动到地面重新启动", "en": "The machine is trapped.Please put machine on the ground to restart."}, "code":19 },#error_physical_trapped
    "lidar_protective_cover": {"msg": {"cn": "激光传感器上盖被挤压。", "en": "Laser Cover Stuck."}, "code":20 },#error_lidar_protective_cover
    "no_bug_or_no_cover": {"msg": {"cn": "请检查盖子或尘袋是否正确安装", "en": "Please check the cover or dust bag of the dust collect station."}, "code":21 }, #collect_dust_no_bag #base_station_without_dust_cover
    "22": {"msg": {"cn": "无法出站，请移除充电桩周围的障碍物。", "en": "Unable to exit the station, remove obstacles around the charging station."}, "code":22 },
    "23": {"msg": {"cn": "水箱振动马达异常，请检查", "en": "Water Tank Vibration Motor Error."}, "code":23 },
    "forbid_area": {"msg": {"cn": "启动机器遇到禁区。", "en": "Restricted area detected,please move to a new location to start."}, "code":24 },#start_form_forbid_area
    "battery_disconnect": {"msg": {"cn": "电池异常，请查阅说明书或APP。", "en": "Battery Error.Please refer to rhe manual or APP."}, "code":25 },#error_battery_disconnect
    "pickup": {"msg": {"cn": "轮子悬空，请将机器放到地面启动", "en": "The wheel is suspended,please put the machine on the ground to start."}, "code":26 },#pickup
    "mop_stuck": {"msg": {"cn": "拖布被卡住。", "en": "Vibration Mop Stuck."}, "code":27 },#error_l_rotate_rag_motor_stuck #error_r_rotate_rag_motor_stuck
    "28": {"msg": {"cn": "前方避障传感器异常，请检查。", "en": "Front Sensor Error."}, "code":28 },
    "opt_during_upgrade": {"msg": {"cn": "请等待机器人升级完成后，再进行操作。", "en": "Please wait for the robot upgrade to complete before proceeding."}, "code":29 },#opt_during_upgrade
    "30": {"msg": {"cn": "二合一尘盒水箱缺失", "en": "Dust box or water tank missing"}, "code":30 },
}

extend_error_notify_code = {

}
#--------YX故障-----------#

#--------公版故障-----------#
# 普通故障
# error_notify_code = {
#     "low_power": {"msg": {"cn": "电量低启动回充", "en": "low battery find charger"}, "code": 1},
#     "poweroff": {"msg": {"cn": "低电关机", "en": "low bat power off"}, "code": 2},
#     "wheel_trap": {"msg": {"cn": "底盘通信异常", "en": "universal wheel stuck"}, "code": 3},
#     "cannot_upgrade": {"msg": {"cn": "不满足升级条件", "en": "cannot upgrade"}, "code": 4},
#     "collision_stuck": {"msg": {"cn": "前撞异常", "en": "collision stuck"}, "code": 5},
#     "dust_station_full": {"msg": {"cn": "集尘站满", "en": "dust station full"}, "code": 6},
#     "tile_error": {"msg": {"cn": "请勿倾斜面上启动", "en": "tilt do task error"}, "code": 7},
#     "lidar_speed_err": {"msg": {"cn": "雷达上盖异常", "en": "lidar protective cover error"}, "code": 8},
#     "lidar_cover": {"msg": {"cn": "请检查顶部雷达是否有被遮蔽或者卡住 雷达堵转", "en": "Please check if the top lidar is obstructed or stuck"}, "code": 9},
#     "lidar_point_err": {"msg": {"cn": "雷达被遮挡", "en": "kit lidar obscured"}, "code": 10},
#     "front_wall_dirty": {"msg": {"cn": "检测到正前方避障传感器脏", "en": "front wall dirty error"}, "code": 11},
#     "psd_dirty": {"msg": {"cn": "沿墙传感器异常", "en": "psd dirty error"}, "code": 12},
#     "middle_sweep": {"msg": {"cn": "中刷卡住", "en": "middle brush stuck"}, "code": 13},
#     "side_sweep": {"msg": {"cn": "边刷卡住", "en": "error side brush stuck"}, "code": 14},
#     "fan_speed": {"msg": {"cn": "风机卡住", "en": "fan stuck"}, "code": 15},
#     "dustbox_out": {"msg": {"cn": "尘盒水箱震动电机移除", "en": "dust box water box vibration motor out"}, "code": 16},
#     "dustbox_full": {"msg": {"cn": "尘盒已满", "en": "garbage box full"}, "code": 17},
#     "no_dust_box": {"msg": {"cn": "尘盒水箱震动电机未安装无法启动", "en": "no dust box water box vibration motor do task"}, "code": 18},
#     "dustbox_fullout": {"msg": {"cn": "取出已满尘盒", "en": "garbage box full out"}, "code": 19},
#     "trapped": {"msg": {"cn": "机器被困", "en": "physical trapped"}, "code": 20},
#     "pick_up": {"msg": {"cn": "离地检测异常", "en": "pick up"}, "code": 21},
#     "no_dust_water_box": {"msg": {"cn": "尘盒水箱未安装无法启动任务", "en": "no dust box water box do task"}, "code": 22},
#     "water_box_empty": {"msg": {"cn": "检测到水箱中水量不足事件", "en": "water box empty"}, "code": 23},
#     "forbid_area": {"msg": {"cn": "在禁区中无法启动工作", "en": "start form forbid area"}, "code": 24},
#     "land_check": {"msg": {"cn": "地检异常", "en": "error drop"}, "code": 25},
#     "findcharge_fail": {"msg": {"cn": "回充失败", "en": "back charger fail"}, "code": 26},
#     "battery_err": {"msg": {"cn": "电池未连接异常", "en": "error battery disconnect"}, "code": 27},
#     "kit_wheel": {"msg": {"cn": "主轮工作异常", "en": "kit universal wheel err"}, "code": 28},
#     "kit_lidar": {"msg": {"cn": "雷达异常", "en": "kit lidar err"}, "code": 29},
#     "kit_water_pump": {"msg": {"cn": "水泵异常", "en": "error kit water pump err"}, "code": 30},
# }
# # 扩展故障
# extend_error_notify_code = {
#     "1": {"code": 1},
#     "kit_middle_brush": {"msg": {"cn": "中刷短路", "en": "middle brush err"}, "code": 2},
#     "kit_side_brush": {"msg": {"cn": "边刷短路", "en": "side brush err"}, "code": 3},
#     "kit_fan": {"msg": {"cn": "风机短路", "en": "kit fan err"}, "code": 4},
#     "kit_vibration": {"msg": {"cn": "震动电机短路", "en": "kit vibration motor err"}, "code": 5},
#     "vibration_stuck": {"msg": {"cn": "震动电机卡住", "en": "vibration motor stuck"}, "code": 6},
#     "no_mop": {"msg": {"cn": "没有安装拖布无法启动任务", "en": "no mop do task"}, "code": 7},
#     "8": {"code": 8},
#     "rug_start": {"msg": {"cn": "地毯启动报错", "en": "rug start error"}, "code": 9},
#     "rocker_switch_off": {"msg": {"cn": "请打开船型开关", "en": "please open rocker switch"}, "code": 10},
#     "l_mop_err": {"msg": {"cn": "左拖布短路", "en": "left mop err"}, "code": 11},
#     "r_mop_err": {"msg": {"cn": "右拖布短路", "en": "right mop err"}, "code": 12},
#     "l_mop_stuck": {"msg": {"cn": "左拖布卡住", "en": "left mop stuck"}, "code": 13},
#     "r_mop_stuck": {"msg": {"cn": "右拖布卡住", "en": "right mop stuck"}, "code": 14},
#     "base_water_not_in": {"msg": {"cn": "基站没有清水箱", "en": "base station clean water tank not in"}, "code": 15},
#     "double_mop_stuck": {"msg": {"cn": "双旋转抹布电机卡住", "en": "double rotate rag motor stuck"}, "code": 16},
# }
#--------公版故障-----------#

# event_notify_code = {
#     "mop_in": {"msg": {"cn": "拖布支架已安装，进入拖地模式", "en": "The mop support has been installed"}, "code": 26}
# }
#
# error_notify_code = {
#     "low_bat_poweroff": {"msg": {"cn": "电量过低，系统即将自动关机", "en": "Low Battery. Please charge and try again later."}, "code": 27},
# }


def message_report(message_dp: int = 128):
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
                                    f'$dp{message_dp}',
                                    '==',
                                    f'{v.get("code")}',
                                    None,
                                ],
                            ],
                        ],
                        'entitySubIds': f'{message_dp}',
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
    code_map = error_notify_code if not is_extend else extend_error_notify_code
    for k, v in code_map.items():
        if v.get("msg") and not k.isdigit():
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


# {"dp": {"id": 28, "name": "故障告警", "code": "fault", "desc": "故障含义见 银星 故障事件协议文档和多语言配置.", "mode": "rw",
#         "property": {"type": "bitmap", "maxlen": 29,
#                      "label": ["left_wheel_err", "middle_brush_stuck", "right_wheel_err", "left_wheel_stuck",
#                                "right_wheel_stuck", "side_brush_err", "side_brush_stuck", "tilt_do_task",
#                                "collision_stuck", "no_dust_water_box", "11", "drop", "middle_brush_err",
#                                "lidar_protective_cover", "fan_err", "lidar_err", "air_flue_blocked", "water_pump_err",
#                                "physical_trapped", "20", "21", "lidar_obscured", "water_box_empty", "forbid_area",
#                                "battery_disconnect", "pickup", "low_bat_poweroff", "28", "collect_dust_no_bag"]},
#         "type": "obj", "scope": "fault", "attr": 1728, "triggerEnable": false, "passiveEnable": false, "routeType": 0,
#         "cloudlessEnable": false}, "productId": "ttutentcei6x0c26"}


def update_fault_dp_content(desc: str, name: str, code: str = "fault", dp_id: int = 28):

    # dp_id = 28
    json_data = {
        'dp': {
            'id': dp_id,
            'name': name,
            'code': code,
            'desc': desc,
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



def get_message_list():
    json_data = {
        'param': {
            'productId': product_key,
            'startTime': None,
            'endTime': None,
            'pageIndex': 1,
            'pageSize': 100,
            'searchValue': '',
            'searchKey': 'name',
            'type': 'customer',
        },
    }

    response = requests.post('https://iot.tuya.com/micro-app/device/api/v4/equipment/list', cookies=cookies,
                             headers=headers, json=json_data)
    # print(json.dumps(response.json(), indent=2))
    result = []
    for item in response.json().get("result", {}).get("dataList", []):
        product_id = item.get("productInfoVO", {}).get("id", "")
        rule_id = item.get("linkageRuleVO", {}).get("id", "")
        result.append({"ruleId": rule_id, "productId": product_id})
    print(result)
    return result


def delete_messages(message_list: list):
    for item in message_list:
        print(f"delete: {item}")
        response = requests.post('https://iot.tuya.com/micro-app/device/api/v1/alarm/remove', cookies=cookies,
                                 headers=headers, json=item)

if __name__ == '__main__':
    """
    0. 更新请求header、cookies
    1. 更新故障DP点定义
    2. 更新消息DP点定义
    3. 新增故障、消息推送
    4. 新增故障、消息文案多语言
    """
    product_key = "ubtwts9fo1ommfbo"

    #一键清空消息
    # msg_list = get_message_list()
    # delete_messages(msg_list)


    # # error_dp_id = 156
    # error_dp_id = 28
    # # error_dp_id = 101
    # is_extend = True
    # # 消息推送128
    message_report(message_dp=128)
    # # 扩展故障101
    # update_fault_dp_content(101)
    # error_report(101, True)
    # # 普通故障28
    # update_fault_dp_content(desc="SEB-银星定制故障协议", name="故障告警", code="fault", dp_id=28)
    # error_report(28, False)

    
