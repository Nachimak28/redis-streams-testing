import os
import time
import redis
import threading
from uuid import uuid4

hostname = "localhost"
port =  6379

redis_connection = redis.Redis(hostname, port, retry_on_timeout=True)

n = 50

def publisher(n):
    time.sleep(1)
    for i in range(n):
        redis_connection.publish('channel', i)
        time.sleep(1)

def run_pubsub():
    threading.Thread(target=publisher, args=(3, )).start()
    pubsub = redis_connection.pubsub()
    pubsub.subscribe(['channel'])
    count = 0
    for item in pubsub.listen():
        print(item)
        count+=1
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break

run_pubsub()
