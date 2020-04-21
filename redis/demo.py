from redis_db import pool
import redis
import time
con = redis.Redis(
    connection_pool=pool
)
try:
    # con.set("country", "英国")
    # con.set("city", "伦敦")
    # city = con.get("city").decode("utf-8")
    # con.expire("city", 5)
    # time.sleep(6)
    # print(con.get("city"))
    # con.delete("country", "city")
    # con.mset({"country": "德国", "city": "柏林"})
    # result =  con.mget("country", "city")
    # for one in result:
    #     print(one.decode("utf-8"))

    # con.rpush("dname", "董事会", "秘书处", "财务部", "技术部")
    # # print(con.get("dname").decode("utf-8"))
    # con.lpop("dname")
    # result = con.lrange("dname", 0, 0)
    # for one in result:
    #     print(one.decode("utf-8"))


    # con.sadd("employee", 8001,8002,8003)
    # con.srem("employee",8001)
    # result = con.smembers("employee")
    # for one in result:
    #     print(one.decode("utf-8"))

    # con.zadd("keyword", {"马云": 0, "张朝阳": 0, "丁磊": 0})
    # con.zincrby("keyword", "10", "马云")
    # result = con.zrevrange("keyword", 0, -1)
    # for one in result:
    #     print(one.decode("utf-8"))

    # con.hmset("9527", {"name": "scott", "sex": "male", "age": "35"})
    # con.hset("9527", "city", "纽约")
    # con.hdel("9527", "age")
    # print(con.hexists("9527", "name"))
    # result = con.hgetall("9527")
    # print(result)
    # for one, value in result.items():
    #     print(one.decode("utf-8"))
    #     print(value.decode("utf-8"))


    pipline = con.pipeline()
    pipline.watch("9527")
    pipline.multi()
    pipline.hset("9527", "name", "jack")
    pipline.hset("9527", "age", 23)
    pipline.execute()
except Exception as e:
    print(e)
finally:
    if "pipline" in dir():
        pipline.reset()
    del con