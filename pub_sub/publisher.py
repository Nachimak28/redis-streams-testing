import os
import time
import redis
import random
from uuid import uuid4

hostname = "localhost"
port =  6379

redis_connection = redis.Redis(hostname, port, retry_on_timeout=True)

# keep publishing continuously
while True:
    message = {"random_no": random.random()}
    redis_connection.publish('channel', message)
    time.sleep(1)
