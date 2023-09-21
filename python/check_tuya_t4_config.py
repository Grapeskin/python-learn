import argparse
import functools
import json
import logging
import os
from enum import Enum
from json import JSONDecodeError
from sys import stdout
from typing import List

import requests
from requests import Response

parser = argparse.ArgumentParser(description="manual to this script")
parser.add_argument("--config", type=str, required=True, help="配置文件路径")
# parser.add_argument("--csrf_token", type=str, required=True, help="指定空间的页面获取的token")
# parser.add_argument("--cookie", type=str, required=True, help="指定空间的页面获取的cookie")
# parser.add_argument("--pid_and_type", type=str, required=True, help="产品及类型，例：um5wfxjed8em2t0p,")
args = parser.parse_args()
if not os.path.exists(args.config):
    logging.error("配置文件不存在")
with open(args.config, "r", encoding="utf-8") as f:
    config = json.load(f)
    request_log_level = config.get("log_level", 20)
    request_csrf_token = config.get("csrf_token")
    request_cookie = config.get("cookie")
    request_products = config.get("config", [])

_formatter = logging.Formatter(
    "%(levelname)s %(asctime)s %(filename)s[line:%(lineno)d] %(message)s"
)
logger = logging.root
logger.name = "autopack"
logger.setLevel(request_log_level)
stdout_handler = logging.StreamHandler(stdout)
stdout_handler.setFormatter(_formatter)
stdout_handler.setLevel(request_log_level)
logger.addHandler(stdout_handler)


# request_csrf_token = "HC5qt4Yp-G-n6bd__0Q4xuWHKqcwXWt24-wo"
# request_cookie = "gTyPlatLang=zh; _tpmGuid=TY-a439153cfa8f6057; locale=zh; tz=8; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; operation_guide_flag=1; Hm_lvt_3be32b3bb5351c17025006d025cf42e7=1670223638; projectCode=; d41d8cd98f00b204e9800998ecf8427e=%5B%5D; 9f53cc1f59328e4c644eed5fa7ff64bc=%5B%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsg%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_ReportStatistics%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_ReportTest%22%5D; fast-sid=40apeiVpewKnSJv0poTEUKKBfLnXvpgr; 3b0beffbab3dcc336bd263560ac7939a=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceMsgCtrl%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_menu_product_deviceDebugging%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_product_deviceDetail%22%5D; e7078bd3ea5ed1f8e61b84d686fb92bf=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_i18n_product%22%5D; 3fd2fb499694a20ff69bb874ff51ba6a=%5B%22smart_menu_i18n_product%22%2C%22smart_page_exp_intro%22%2C%22smart_menu_product_dev%22%5D; 9b1a6dd057338832b7c1452c9614ea87=%5B%22smart_menu_product_dev%22%5D; navbarShowExpand=1; router-prefix=; s-sid=s:6d3c8fe4-2346-4036-8d3d-6d04075cabcd.CiB4KR3k5OffIbLT3/9McyD07WMjh5jtFomdpslOL7g; _tpmSid=a01c9214d2190eae6f0a218b2970671ae0d7aebd2c5799d056e7cc70d74f3a27; csr-test-csrf-token=uZJQmWoz-T9dbmLRYZ5k3dZqjhMGEPYXf0Sw; 3759e392f25da605e49643aa75517913=%5B%22smart_menu_product_deviceMsg%22%2C%22smart_menu_product_dev%22%2C%22smart_menu_product_deviceFirmwareManage%22%2C%22smart_menu_appserviceAppList%22%2C%22smart_menu_i18n_product%22%2C%22smart_menu_product_deviceDetail%22%2C%22smart_menu_product_deviceLog%22%2C%22smart_page_exp_intro%22%5D; _tpmSeqId=seq_id_bf7b0dd637782983; csrf-token=EtfxHQdl-dPonKeq0dHKatzeJ1KDPFHd0Dv4; csrf-token.sig=queoFyadCLwBnmheVN47d47NTgw"
# request_csrf_token = args.csrf_token
# request_cookie = args.cookie


class HttpMethod(Enum):
    GET = "get"
    POST = "post"


class TUYAHeader:
    def __init__(self, csrf_token: str, cookie: str):
        self.csrf_token = csrf_token
        self.cookie = cookie

    def to_json(self) -> dict:
        return {
            "csrf-token": self.csrf_token,
            "cookie": self.cookie
        }


def log(description=None):
    """日志切面"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Params >>> {kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"Result >>> {result}")
            return result

        return wrapper

    return decorator


class TUYAHttpExecutor:
    header = TUYAHeader(request_csrf_token, request_cookie).to_json()
    dp_ids = []
    dp_id_configs = []
    message_notify_configs = []

    # def __init__(self, header: TUYAHeader):
    #     TUYAHttpExecutor.header = header.to_json()

    @staticmethod
    # @log()
    def execute(url: str, json_data: dict, method: HttpMethod = HttpMethod.POST) -> Response:
        return requests.request(method=method.value, url=url, headers=TUYAHttpExecutor.header, json=json_data)

    @staticmethod
    def get_message_notify_configs(pid: str):
        if TUYAHttpExecutor.message_notify_configs:
            return TUYAHttpExecutor.message_notify_configs
        response: Response = TUYAHttpExecutor.execute(
            url="https://iot.tuya.com/micro-app/device/api/v4/equipment/list",
            json_data={
                "param": {
                    "productId": pid,
                    # "startTime": null,
                    # "endTime": null,
                    "pageIndex": 1,
                    "pageSize": 200,
                    "searchValue": "",
                    "searchKey": "name",
                    "type": "customer"
                }
            })
        if response.status_code != 200:
            return []
        # logging.info(response.json())
        try:
            data: dict = response.json()
            for item in data.get("result", {}).get("dataList", []):
                link_age_rule_vo = item.get("linkageRuleVO", {})
                i18n_data = link_age_rule_vo.get("i18nData", {})
                TUYAHttpExecutor.message_notify_configs.append({
                    "cn_content": i18n_data.get("content", {}).get("1"),
                    "en_content": i18n_data.get("content", {}).get("4"),
                    "dp_id": int(link_age_rule_vo.get("conditions", [])[0].get("entitySubIds", 0)),
                    "enum_code": link_age_rule_vo.get("conditions", [])[0].get("expr", [])[0][0][2],
                    "enabled": link_age_rule_vo.get("enabled"),
                })
            # logging.info(
            #     f"message_notify_configs: {json.dumps(TUYAHttpExecutor.message_notify_configs, indent=4, ensure_ascii=False)}")
            return TUYAHttpExecutor.message_notify_configs
        except JSONDecodeError as e:
            logging.error("Response data is invalid json format. ", e.msg)
            return []

    @staticmethod
    def get_dp_ids(pid: str, dp_id: int = 0) -> list:
        # data: dict = {}

        response: Response = TUYAHttpExecutor.execute(
            url="https://iot.tuya.com/micro-app/pmg/api/product/schemaGetStd/V2",
            json_data={
                "productId": pid
            })
        if response.status_code != 200:
            return []
        try:
            res_json = response.json()
            data = res_json.get("result", {}).get("dps", [])
            # logging.info(data)
        except JSONDecodeError as e:
            logging.error("Response data is invalid json format. ", e.msg)
            return []

        for item in data:
            if item.get("id"):
                if item.get("id") not in TUYAHttpExecutor.dp_ids:
                    TUYAHttpExecutor.dp_ids.append(item.get("id"))
                if dp_id == int(item.get("id")):
                    if item.get("property", {}).get("type") == "enum":
                        TUYAHttpExecutor.dp_id_configs.append(
                            {item.get("id"): item.get("property", {}).get("range", [])})
                    elif item.get("property", {}).get("type") == "bitmap":
                        TUYAHttpExecutor.dp_id_configs.append(
                            {item.get("id"): [i for i in
                                              range(int(item.get("property", {}).get("maxlen")))]})
        # logging.info(f"dp_ids: {TUYAHttpExecutor.dp_ids}")
        # logging.info(f"dp_id_configs: {TUYAHttpExecutor.dp_id_configs}")
        return TUYAHttpExecutor.dp_ids


class BaseNotificationCode:
    def __init__(self, pid: str, dp_id: int):
        self.pid = pid
        self.dp_id = dp_id

        self.message_notifies = []

        if not self.check_dp_id_exist():
            raise RuntimeError("dp id is not exist")

    def check_dp_id_exist(self) -> bool:
        dp_ids = TUYAHttpExecutor.get_dp_ids(self.pid, self.dp_id)

        logging.info(
            f"Step 1. 校验DP点是否存在. pid={self.pid}, result={self.dp_id in dp_ids} ")
        logging.debug(f"dp_id={self.dp_id}, dp_ids={dp_ids}")
        logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        if self.dp_id not in dp_ids:
            return False
        return True

    def check_dp_id_config(self) -> bool:
        result = False
        for item in TUYAHttpExecutor.dp_id_configs:
            if set([message.code for message in self.message_notifies]) == set(item.get(self.dp_id, [])):
                result = True
                break
        if not result:
            logging.warning(
                f"expect={sorted(set([message.code for message in self.message_notifies]), key=lambda x: int(x))}, actual={sorted(set([dp_id for item in TUYAHttpExecutor.dp_id_configs if item.get(self.dp_id) for dp_id in item.get(self.dp_id, [])]), key=lambda x: int(x))}")
        logging.info(
            f"Step 2. 校验DP点的参数设置是否正确. pid={self.pid}, dp_id={self.dp_id}, result={result}")
        logging.debug(
            f"expect={[message.code for message in self.message_notifies]}, actual={TUYAHttpExecutor.dp_id_configs}")
        logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return result

    def check_dp_id_notification_config(self) -> bool:
        result = True
        for message in self.message_notifies:
            find = False
            enabled = None
            enum_code = None
            for item in TUYAHttpExecutor.get_message_notify_configs(self.pid):
                # TODO 校验文本
                if item.get("dp_id") == self.dp_id and item.get("enum_code") == message.code and item.get("enabled"):
                    find = True
                    break
                enabled = item.get("enabled")
                enum_code = item.get("enum_code")
                # logging.debug(f"message_code={message.code}, enum_code={enum_code},enabled={enabled}")
                # enabled = item.get("enabled")
            if not find:
                logging.error(
                    f"未配置消息推送或已配置未开启. dp_id={self.dp_id}, message_code={message.code}, find={find}")
            result &= find
        logging.info(f"Step 3. 校验DP点的消息推送是否正确. pid={self.pid}, dp_id={self.dp_id}, result={result} ")
        logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return result


class MessageContent:
    def __init__(self, cn: str, en: str = ""):
        self.cn = cn
        self.en = en


class BitMapMessageContent(MessageContent):
    def __init__(self, code: int, cn: str, en: str = ""):
        super().__init__(cn, en)
        self.code = code


class EnumMessageContent(MessageContent):
    def __init__(self, code: str, cn: str, en: str = ""):
        super().__init__(cn, en)
        self.code = code


# class NotificationErrorCode(BaseNotificationCode):
#     def check_dp_id_notification_config(self):
#         result = True
#         for message in self.message_notifies:
#             find = False
#             enabled = None
#             for item in TUYAHttpExecutor.get_message_notify_configs(self.pid):
#                 # TODO 校验文本
#                 if item.get("dp_id") == self.dp_id and item.get("enum_code") == message.code:
#                     find = True
#                     enabled = item.get("enabled")
#             if not find or not enabled:
#                 logging.info(f"dp_id={self.dp_id}, code={message.code}, enabled={enabled} find={find}")
#             result &= find
#         logging.info(f"check_dp_id_notification_config. dp_id={self.dp_id}, result={result}")
#         return result
#
#
# class NotificationMessageCode(BaseNotificationCode):
#     def check_dp_id_notification_config(self):
#         result = True
#         for message in self.message_notifies:
#             find = False
#             enabled = None
#             for item in TUYAHttpExecutor.get_message_notify_configs(self.pid):
#                 # TODO 校验文本
#                 if item.get("dp_id") == self.dp_id and item.get("enum_code") == message.code:
#                     find = True
#                     enabled = item.get("enabled")
#             if not find or not enabled:
#                 logging.info(f"dp_id={self.dp_id}, code={message.code}, enabled={enabled} find={find}")
#             result &= find
#         logging.info(f"check_dp_id_notification_config. dp_id={self.dp_id}, result={result}")
#         return result

class ProductType(Enum):
    PUBLIC = "public"
    CUSTOM_YINXING = "custom_yinxing"


class Product:
    def __init__(self, pid: str, product_type: str = ProductType.PUBLIC.value):
        logging.info(f"【开始校验产品配置. pid={pid}】")
        logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.pid = pid
        self.check_config = []
        if product_type == ProductType.PUBLIC.value:
            self.check_config.append(TUYAT4PublicStandardErrorCode(pid))
            self.check_config.append(TUYAT4PublicExtendErrorCode(pid))
            self.check_config.append(TUYAT4PublicMessageCode(pid))
        elif product_type == ProductType.CUSTOM_YINXING.value:
            self.check_config.append(TUYAT4CustomYinXingStandardErrorCode(pid))
            self.check_config.append(TUYAT4CustomYinXingExtendErrorCode(pid))
            self.check_config.append(TUYAT4CustomYinXingMessageCode(pid))
        else:
            logging.error("Not support")

    def check(self) -> bool:
        result = False
        for item in self.check_config:
            result &= item.check_dp_id_config()
            result &= item.check_dp_id_notification_config()
        return result


class Main:
    def __init__(self, products: List[Product]):
        self.products = products

    def check(self):
        check_result = []
        for product in self.products:
            result = product.check()
            logging.info(f"【结束校验产品配置. pid={product.pid}, result={result}】")
            logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            check_result.append({
                product.pid: result
            })
        logging.info(f"测试结果：{json.dumps(check_result, indent=4)}")


class TUYAT4PublicStandardErrorCode(BaseNotificationCode):

    def __init__(self, pid: str):
        super().__init__(pid, 28)

        self.message_notifies.append(BitMapMessageContent(0, "电量低启动回充", ))
        self.message_notifies.append(BitMapMessageContent(1, "低电关机", ))
        self.message_notifies.append(BitMapMessageContent(2, "底盘通信异常", ))
        self.message_notifies.append(BitMapMessageContent(3, "不满足升级条件", ))
        self.message_notifies.append(BitMapMessageContent(4, "前撞异常", ))
        self.message_notifies.append(BitMapMessageContent(5, "集尘站满", ))
        self.message_notifies.append(BitMapMessageContent(6, "请勿倾斜面上启动", ))
        self.message_notifies.append(BitMapMessageContent(7, "雷达上盖异常", ))
        self.message_notifies.append(BitMapMessageContent(8, "请检查顶部雷达是否有被遮蔽或者卡住", ))
        self.message_notifies.append(BitMapMessageContent(9, "雷达被遮挡", ))
        self.message_notifies.append(BitMapMessageContent(10, "检测到正前方避障传感器脏", ))
        self.message_notifies.append(BitMapMessageContent(11, "沿墙传感器异常", ))
        self.message_notifies.append(BitMapMessageContent(12, "中刷卡住", ))
        self.message_notifies.append(BitMapMessageContent(13, "边刷卡住", ))
        self.message_notifies.append(BitMapMessageContent(14, "风机卡住", ))
        self.message_notifies.append(BitMapMessageContent(15, "尘盒水箱震动电机移除", ))
        self.message_notifies.append(BitMapMessageContent(16, "尘盒已满", ))
        self.message_notifies.append(BitMapMessageContent(17, "尘盒水箱震动电机未安装无法启动", ))
        self.message_notifies.append(BitMapMessageContent(18, "取出已满尘盒", ))
        self.message_notifies.append(BitMapMessageContent(19, "机器被困", ))
        self.message_notifies.append(BitMapMessageContent(20, "离地检测异常", ))
        self.message_notifies.append(BitMapMessageContent(21, "尘盒水箱未安装无法启动任务", ))
        self.message_notifies.append(BitMapMessageContent(22, "检测到水箱中水量不足事件", ))
        self.message_notifies.append(BitMapMessageContent(23, "在禁区中无法启动工作", ))
        self.message_notifies.append(BitMapMessageContent(24, "地检异常", ))
        self.message_notifies.append(BitMapMessageContent(25, "回充失败", ))
        self.message_notifies.append(BitMapMessageContent(26, "电池未连接异常", ))
        self.message_notifies.append(BitMapMessageContent(27, "主轮工作异常", ))
        self.message_notifies.append(BitMapMessageContent(28, "雷达异常", ))
        self.message_notifies.append(BitMapMessageContent(29, "水泵异常", ))


class TUYAT4PublicExtendErrorCode(BaseNotificationCode):

    def __init__(self, pid: str):
        super().__init__(pid, 101)

        self.message_notifies.append(BitMapMessageContent(0, "", ))
        self.message_notifies.append(BitMapMessageContent(1, "中刷短路", ))
        self.message_notifies.append(BitMapMessageContent(2, "边刷短路", ))
        self.message_notifies.append(BitMapMessageContent(3, "风机短路", ))
        self.message_notifies.append(BitMapMessageContent(4, "震动电机短路", ))
        self.message_notifies.append(BitMapMessageContent(5, "震动电机卡住", ))
        self.message_notifies.append(BitMapMessageContent(6, "没有安装拖布无法启动任务", ))
        self.message_notifies.append(BitMapMessageContent(7, "", ))
        self.message_notifies.append(BitMapMessageContent(8, "地毯启动报错", ))
        self.message_notifies.append(BitMapMessageContent(9, "请打开船型开关", ))
        self.message_notifies.append(BitMapMessageContent(10, "左拖布短路", ))
        self.message_notifies.append(BitMapMessageContent(11, "右拖布短路", ))
        self.message_notifies.append(BitMapMessageContent(12, "左拖布卡住", ))
        self.message_notifies.append(BitMapMessageContent(13, "右拖布卡住", ))
        self.message_notifies.append(BitMapMessageContent(14, "基站没有清水箱", ))
        self.message_notifies.append(BitMapMessageContent(15, "双旋转抹布电机卡住", ))


class TUYAT4PublicMessageCode(BaseNotificationCode):

    def __init__(self, pid: str):
        super().__init__(pid, 128)

        # id为枚举字符串
        self.message_notifies.append(EnumMessageContent("1", "低电清扫", ))
        self.message_notifies.append(EnumMessageContent("2", "定位失败", ))
        self.message_notifies.append(EnumMessageContent("3", "充电桩上无法关机", ))
        self.message_notifies.append(EnumMessageContent("4", "进入勿扰模式", ))
        self.message_notifies.append(EnumMessageContent("5", "预约清扫开始", ))
        self.message_notifies.append(EnumMessageContent("6", "清扫完成", ))
        self.message_notifies.append(EnumMessageContent("7", "回充定位失败", ))
        self.message_notifies.append(EnumMessageContent("8", "充电已完成继续清扫", ))
        self.message_notifies.append(EnumMessageContent("9", "当前有清扫任务预约启动失败", ))
        self.message_notifies.append(EnumMessageContent("10", "清扫定位失败", ))
        self.message_notifies.append(EnumMessageContent("11", "低电需要回充", ))
        self.message_notifies.append(EnumMessageContent("12", "清扫区域无法到达", ))

        self.message_notifies.append(EnumMessageContent("14", "工作站尘袋已满", ))
        self.message_notifies.append(EnumMessageContent("15", "工作站未安装尘袋", ))
        self.message_notifies.append(EnumMessageContent("16", "勿扰模式下定时任务不执行", ))

        self.message_notifies.append(EnumMessageContent("18", "工作站风机异常", ))
        self.message_notifies.append(EnumMessageContent("19", "拖布移除事件", ))
        self.message_notifies.append(EnumMessageContent("20", "集尘完成", ))
        self.message_notifies.append(EnumMessageContent("21", "基站压力过高", ))
        self.message_notifies.append(EnumMessageContent("22", "基站压力过低", ))
        self.message_notifies.append(EnumMessageContent("23", "边刷卡住", ))


class TUYAT4CustomYinXingStandardErrorCode(BaseNotificationCode):

    def __init__(self, pid: str):
        super().__init__(pid, 28)

        self.message_notifies.append(BitMapMessageContent(0, "错误2：轮子模组异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(1, "滚刷被卡住。", ))
        self.message_notifies.append(BitMapMessageContent(2, "错误2：轮子模组异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(3, "轮子被卡住。", ))
        self.message_notifies.append(BitMapMessageContent(4, "轮子被卡住。", ))
        self.message_notifies.append(BitMapMessageContent(5, "错误3：边刷模组异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(6, "边刷被卡住。", ))
        self.message_notifies.append(BitMapMessageContent(7, "机器倾斜，请将机器放到水平地面启动", ))
        self.message_notifies.append(BitMapMessageContent(8, "碰撞缓冲器被卡住。", ))
        self.message_notifies.append(BitMapMessageContent(9, "二合一尘盒水箱缺失", ))
        self.message_notifies.append(BitMapMessageContent(10, "NA", ))
        self.message_notifies.append(BitMapMessageContent(11, "悬崖传感器被遮挡，请擦拭", ))
        self.message_notifies.append(BitMapMessageContent(12, "错误5：滚刷异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(13, "激光传感器被卡住或缠绕，请检查", ))
        self.message_notifies.append(BitMapMessageContent(14, "错误4：风机异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(15, "错误7：点激光传感器异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(16, "错误12：集尘座通道被堵住，请清理", ))
        self.message_notifies.append(BitMapMessageContent(17, "错误6：水泵异常，请查阅说明书或APP", ))
        self.message_notifies.append(BitMapMessageContent(18, "机器被困，请移动到地面重新启动", ))
        self.message_notifies.append(BitMapMessageContent(19, "请将主机放至新位置启动", ))
        self.message_notifies.append(BitMapMessageContent(20, "NA", ))
        self.message_notifies.append(BitMapMessageContent(21, "点激光传感器被遮挡，请擦拭", ))
        self.message_notifies.append(BitMapMessageContent(22, "错误15：水箱水量不足，请加水。", ))
        self.message_notifies.append(BitMapMessageContent(23, "启动机器遇到禁区。", ))
        self.message_notifies.append(BitMapMessageContent(24, "错误1：电池异常，请查阅说明书或APP。", ))
        self.message_notifies.append(BitMapMessageContent(25, "轮子悬空，请将机器放到地面启动", ))
        self.message_notifies.append(BitMapMessageContent(26, "电量过低，系统即将自动关机", ))
        self.message_notifies.append(BitMapMessageContent(27, "操作异常，请检查主开关是否开启", ))
        self.message_notifies.append(BitMapMessageContent(28, "NA", ))
        self.message_notifies.append(BitMapMessageContent(29, "NA", ))


class TUYAT4CustomYinXingExtendErrorCode(BaseNotificationCode):

    def __init__(self, pid: str):
        super().__init__(pid, 101)


class TUYAT4CustomYinXingMessageCode(BaseNotificationCode):

    def __init__(self, pid: str):
        super().__init__(pid, 128)

        self.message_notifies.append(EnumMessageContent("1", "开始预约清扫", ))
        self.message_notifies.append(EnumMessageContent("2", "充电完毕，继续清扫", ))
        self.message_notifies.append(EnumMessageContent("3", "电量不足，开始回充", ))
        self.message_notifies.append(EnumMessageContent("4", "找不到回充座，停止回充", ))
        self.message_notifies.append(EnumMessageContent("5", "请将机器放到充电座充电，并确保电量大于20%再升级", ))
        self.message_notifies.append(EnumMessageContent("6", "清扫结束，开始回充", ))
        self.message_notifies.append(EnumMessageContent("7", "升级失败，请重试", ))
        self.message_notifies.append(EnumMessageContent("8", "升级成功", ))
        self.message_notifies.append(EnumMessageContent("9", "请及时清理尘袋", ))
        self.message_notifies.append(EnumMessageContent("10", "勿扰时间段内，断点续扫未执行", ))
        self.message_notifies.append(EnumMessageContent("11", "勿扰时间段内，预约清扫未执行", ))
        self.message_notifies.append(EnumMessageContent("12", "机器人在工作中，预约未执行", ))
        self.message_notifies.append(EnumMessageContent("13", "集尘中", ))
        self.message_notifies.append(EnumMessageContent("14", "电量不足，自动关机", ))
        self.message_notifies.append(EnumMessageContent("15", "断点续扫中，预约未执行", ))
        self.message_notifies.append(EnumMessageContent("16", "重定位失败，预约未执行", ))
        self.message_notifies.append(EnumMessageContent("17", "系统升级中，请耐心等待", ))
        self.message_notifies.append(EnumMessageContent("18", "充电中，请充电完毕再操作", ))
        self.message_notifies.append(EnumMessageContent("19", "查看地图是否被更改，请重新设置预约清扫", ))
        self.message_notifies.append(EnumMessageContent("20", "本地地图已满，请手动删除不必要的地图，以免地图丢失", ))
        self.message_notifies.append(EnumMessageContent("21", "电量不足请充电，稍后再试", ))
        self.message_notifies.append(EnumMessageContent("22", "气压传感器失效，请注意清理尘袋", ))
        self.message_notifies.append(EnumMessageContent("23", "NA", ))
        self.message_notifies.append(EnumMessageContent("24", "NA", ))
        self.message_notifies.append(EnumMessageContent("25", "拖布支架已取下，退出拖地模式", ))
        self.message_notifies.append(EnumMessageContent("26", "拖布支架已安装，进入拖地模式", ))
        self.message_notifies.append(EnumMessageContent("27", "NA", ))
        self.message_notifies.append(EnumMessageContent("28", "NA", ))
        self.message_notifies.append(EnumMessageContent("29", "NA", ))


main = Main([
    Product(pid=item.get("pid"), product_type=item.get("type")) for item in request_products
    # Product(pid="oizjibugnumjjkd0", product_type=ProductType.CUSTOM_YINXING.value),
    # Product(pid="rctih3aredueiuea"),
    # Product(pid="acipudgmgguhivne"),
    # Product(pid="djmprawazc46ef5i"),
    # Product(pid="qfpljn93jqq9loyx"),
    # Product(pid="dmkv0kjlykfih7ah"),
    # Product(pid="um5wfxjed8em2t0p"),
])
main.check()
