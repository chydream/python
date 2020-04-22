from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    pass
    f = open("test.txt", "r", encoding="utf-8")
    result = f.readlines()
    for one in result:
        l = one.split(',')
        if int(l[3]) >= 85 and int(l[4]) >= 85 and int(l[5]) >= 85:
            con.rpush('select', one)
    if con.exists('select'):
        res = con.lrange('select', 0, -1)
        for item in res:
            print(item.decode("utf-8"))
    f.close()
except Exception as e:
    print(e)
finally:
    del con