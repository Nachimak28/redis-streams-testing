import os
import time
import redis


hostname ="localhost"
port =  6379


redis_connection = redis.Redis(hostname, port, retry_on_timeout=True)
stream_key = "channel_1"
sleep_ms = 100
last_id = 0

while True:
    try:
        resp = redis_connection.xread(
            {stream_key: last_id}, count=1, block=sleep_ms
        )
        if resp:
            key, messages = resp[0]
            last_id, data = messages[0]
            print("REDIS ID: ", last_id)
            print("      --> ", data)
    except Exception as e:
        print(e)