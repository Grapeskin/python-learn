# import os
# import shutil
# from datetime import datetime
#
#
# def retrieve_files(start_datetime, end_datetime, source_folder, destination_folder):
#     files = []
#     for root, _, filenames in os.walk(source_folder):
#         for filename in filenames:
#             file_path = os.path.join(root, filename)
#             modified_time = os.path.getmtime(file_path)
#             modified_datetime = datetime.fromtimestamp(modified_time)
#             if start_datetime <= modified_datetime <= end_datetime:
#                 files.append(file_path)
#
#     # 按照修改时间从旧到新对文件路径进行排序
#     sorted_files = sorted(files, key=lambda x: os.path.getmtime(x))
#
#     # 将文件复制到目标文件夹
#     for file in sorted_files:
#         print(file)
#         shutil.copy2(file, destination_folder)
#
#
# # 设置开始时间和结束时间
# start_datetime = datetime(2023, 10, 26, 16, 55)  # 根据需要设置分钟
# end_datetime = datetime(2023, 10, 26, 17, 00)  # 根据需要设置分钟
#
# # 指定共享文件夹路径和目标文件夹路径
# source_folder = r"\\192.168.160.11\ldrobot-team\P104\0000B8311750004C63A0900000127KCV\2023\10\26\AR-0.4.7_4631-0000B8311750004C63A0900000127KCV-C43960EE4224"
# destination_folder = r"D:\server_log"
#
# # 获取共享文件夹中在指定时间范围内的文件并拷贝到目标文件夹
# retrieve_files(start_datetime, end_datetime, source_folder, destination_folder)
import os

# from smb.SMBConnection import SMBConnection
#
# def retrieve_files(server_name, share_name, username, password, destination_folder):
#     conn = SMBConnection(username, password, '', server_name, use_ntlm_v2=True)
#     conn.connect(server_name, 445)  # 默认SMB端口为445
#     files = conn.listPath(share_name, r'\P104\0000B8311750004C63A0900000127KCV\2023\10\26\AR-0.4.7_4631-0000B8311750004C63A0900000127KCV-C43960EE4224')
#
#     for file in files:
#         if file.isDirectory:  # 只处理文件夹
#             continue
#
#         file_path = file.filename
#         # destination_path = os.path.join(destination_folder, file_path)
#         # with open(destination_path, 'wb') as f:
#         #     file_attributes, file_size = conn.retrieveFile(share_name, file_path, f)
#
# # 填入共享文件夹的相关信息
# server_name = '192.168.160.11'  # 共享文件夹所在的服务器的IP地址
# share_name = 'ldrobot-team'  # 共享文件夹的名称
# username = 'ldrobot-team'  # 访问共享文件夹的用户名
# password = 'ldrobotlog4110'  # 访问共享文件夹的密码
# destination_folder = r"D:\server_log"  # 将文件拷贝到本地的目录
#
# # 获取共享文件夹中的文件并拷贝到本地目录
# retrieve_files(server_name, share_name, username, password, destination_folder)


# import shutil
#
# def copy_shared_file(source_path, destination_path):
#     shutil.copy2(source_path, destination_path)
#
# # 指定共享文件夹中的文件路径和目标文件夹路径
# source_path = R"\\192.168.160.11\ldrobot-team\P104\0000B8311750004C63A0900000127KCV\2023\10\26\AR-0.4.7_4631-0000B8311750004C63A0900000127KCV-C43960EE4224\Record-786105_50_2023-10-26_08-56-28-FindChargerAndWash.drc.save.gz"
# destination_path = r"D:\Record-786105_50_2023-10-26_08-56-28-FindChargerAndWash.drc.save.gz"

# 拷贝共享文件夹中的文件到目标文件夹
# copy_shared_file(source_path, destination_path)

import os
from ftplib import FTP
from datetime import datetime

# 连接FTP服务器
ftp = FTP('192.168.160.11')
ftp.login('readlog', 'Ld2023102645')

ftp.cwd('/mnt/robot-log/P104/0000B8311750004C63A090000007257X/2023/10/27/AR-0.4.0_4623-0000B8311750004C63A090000007257X-C43960EE4219/')

# 获取文件列表
file_list = ftp.nlst()

# 设置时间范围（示例为从2022-01-01 00:00到2022-01-01 23:59）
start_time = datetime(2023, 10, 26, 16, 55)
end_time = datetime(2023, 10, 26, 17, 00)

# 迭代文件列表并下载满足时间范围的文件
# for file_name in file_list:
#     file_time = ftp.voidcmd('MDTM ' + file_name).split()[1]
#     file_datetime = datetime.strptime(file_time, '%Y%m%d%H%M%S')
#     if start_time <= file_datetime <= end_time:
#         local_file_path = os.path.join(r"D:\server_log", file_name)
#         with open(local_file_path, 'wb') as file:
#             ftp.retrbinary('RETR ' + file_name, file.write)
#         print(f"下载文件：{file_name}")

# 迭代文件列表并下载满足时间范围的文件
for file_name in file_list:
    local_file_path = os.path.join(r"D:/server_log/", file_name)
    with open(local_file_path, 'wb') as file:
        ftp.retrbinary('RETR ' + file_name, file.write)
    # 获取本地文件的修改时间
    file_datetime = datetime.fromtimestamp(os.path.getmtime(local_file_path))
    if start_time <= file_datetime <= end_time:
        print(f"下载文件：{file_name}")
    else:
        # 删除不满足时间范围的文件
        os.remove(local_file_path)
# 关闭FTP连接
ftp.quit()