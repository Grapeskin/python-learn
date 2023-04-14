import pandas as pd
import datetime

# 读取数据
df = pd.read_excel("副本3.8.xls", usecols=["姓名", "日期", "时间", "工时"])

# 定义班次时间段
shifts = [
    {"shifts": ["08:00", "12:00", "13:30", "17:30", "18:30", "20:30"], "work_time": 10},
    {
        "shifts": ["08:00", "12:00", "12:30", "17:30", "18:00", "20:30"],
        "work_time": 11.5,
    },
    {
        "shifts": ["20:30", "00:00", "01:30", "08:00"],
        "work_time": 10,
    },
    {
        "shifts": ["20:30", "00:00", "00:30", "08:00"],
        "work_time": 11,
    },
]


columns = df.columns.values.tolist()  ### 获取excel 表头 ，第一行


def calc_work_time(time_arr: list) -> int:
    # 校验打卡长度
    standard = False
    for item in shifts:
        if len(time_arr) == len(item.get("shifts", [])):
            standard = True
            break
    if not standard:
        return -1

    # 完全符合
    for item in shifts:
        i = 0
        delta_hour = 0
        while i < len(item.get("shifts", [])) and i < len(time_arr):
            if not (
                datetime.datetime.strptime(item.get("shifts", [])[i], "%H:%M")
                + datetime.timedelta(minutes=-60)
                <= datetime.datetime.strptime(time_arr[i], "%H:%M")
                <= datetime.datetime.strptime(item.get("shifts", [])[i], "%H:%M")
            ):
                break

            if not (
                datetime.datetime.strptime(item.get("shifts", [])[i + 1], "%H:%M")
                <= datetime.datetime.strptime(time_arr[i + 1], "%H:%M")
                <= datetime.datetime.strptime(item.get("shifts", [])[i + 1], "%H:%M")
                + datetime.timedelta(minutes=60)
            ):
                if datetime.datetime.strptime(
                    time_arr[i + 1], "%H:%M"
                ) >= datetime.datetime.strptime(item.get("shifts", [])[i + 1], "%H:%M"):
                    if i + 1 == len(item.get("shifts", [])) - 1:
                        # 最后一班
                        delta = datetime.datetime.strptime(
                            time_arr[i + 1], "%H:%M"
                        ) - datetime.datetime.strptime(
                            item.get("shifts", [])[i + 1], "%H:%M"
                        )
                        delta_hour = (
                            (delta.seconds / 60) - (delta.seconds / 60) % 30
                        ) / 60

                    else:
                        break
                else:
                    break

            i = i + 2
        if i == len(item.get("shifts", [])):
            # 符合条件
            return (
                delta_hour + item.get("work_time")
                if delta_hour
                else item.get("work_time")
            )

    return -1


for idx, row in df.iterrows():  ### 迭代数据 以键值对的形式 获取 每行的数据
    time_col = row["时间"]
    if not pd.isnull(time_col):
        time_arr = time_col.split(" ")
        work_time = calc_work_time(time_arr)
        if work_time < 0:
            continue
        df.iloc[idx, 3] = work_time

print(df)
df.to_excel("output.xlsx", index=False)