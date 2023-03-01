import os
import time
import redis
import json

hostname = "localhost"
port =  6379

redis_connection = redis.Redis(hostname, port, retry_on_timeout=True)



ps = redis_connection.pubsub()
ps.subscribe(["channel"])
for raw_message in ps.listen():
    message = json.loads(raw_message["data"])
    print(message)