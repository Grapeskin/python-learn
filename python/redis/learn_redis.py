import time

import redis
import uuid

if __name__ == '__main__':
    client = redis.Redis(host='192.168.199.20', port=6379, db=0)
    key = 'test_key'
    current_time = int(time.time())
    while True:
        client.zadd(key, {str(uuid.uuid4()): time.time()})
        # client.zadd(key, {
        #     'k0': current_time,
        #     'k1': current_time - 1,
        #     'k2': current_time - 3,
        #     'k3': current_time - 5,
        #     'k4': current_time - 10
        # })
    min_score = -1
    # 左闭右闭区间，区间-1
    max_score = current_time - 5 - 1
    # 左闭右闭区间
    range_res = client.zrangebyscore(name=key, min=min_score, max=max_score, withscores=True)
    for item in range_res:
        print(f"key={item[0]}, score={item[1]}")
    # 左闭右闭区间
    print(client.zremrangebyscore(key, min=min_score, max=max_score))
    """
    测试结果：
    key=b'k4', score=1648720573.0
    key=b'k3', score=1648720578.0
    2
    """
