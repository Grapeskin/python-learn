#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : JiaYou
@Time    : 2022/1/23 10:49
"""
from minio import Minio


def put_file():
    # Make 'asiatrip' bucket if not exist.¥
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name, location='cn-north-1')
    else:
        print(f"Bucket '{bucket_name}' already exists")
    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        bucket_name, upload_obj_path, local_file_path,
    )
    print(
        f"'{local_file_path}' is successfully uploaded as object '{upload_obj_path}' to bucket '{bucket_name}'."
    )


def download_file():
    res = client.fget_object(bucket_name, upload_obj_path, download_file_path)
    print(res.__dict__)


if __name__ == '__main__':
    """Minio 学习
    References: http://docs.minio.org.cn/docs/master/minio-monitoring-guide
    """
    bucket_name = 'test-bucket'
    local_file_path = '/Users/youge/PycharmProjects/python-learn/test.txt'
    upload_obj_path = 'custom_test.txt'
    download_file_path = '/Users/youge/PycharmProjects/python-learn/d_test.txt'
    client = Minio('localhost:9000',
                   access_key='Q3AM3UQ867SPQQA43P2F',
                   secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                   secure=False)
    put_file()
    download_file()
