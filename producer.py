import os
import time
import redis
from uuid import uuid4

num_messages = 10


hostname ="localhost"
port =  6379

redis_connection = redis.Redis(hostname, port, retry_on_timeout=True)
stream_key = "channel_1"

for i in range(num_messages):
    data = {
            "producer": "producer",
            "uuid": uuid4().hex,
            "message_idx": i
            }
    resp = redis_connection.xadd(stream_key, data)
    print(resp)
    time.sleep(2)

