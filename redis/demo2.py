import random
from redis_db import pool
import redis
con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete("bid")
    l = ["马云", "丁磊", "张朝阳", "马化腾", "李彦宏"]
    con.zadd("bid", {"马云": 0, "丁磊": 0, "张朝阳": 0, "马化腾": 0, "李彦宏": 0})
    for i in range(0, 300):
        # print(i)
        index = random.randint(0, 4)
        con.zincrby("bid", 1, l[index])
    result = con.zrevrange("bid", 0, -1, "WITHSCORES")
    for one in result:
        print(one[0].decode("utf-8"), int(one[1]))
except Exception as e:
    print(e)
finally:
    del con