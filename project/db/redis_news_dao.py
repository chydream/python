from db.redis_db import pool
import redis

class RedisNewsDao:
    #添加新闻缓存数据
    def insert_cache(self, id, title, username, type, content, is_top, create_time):
        try:
            con = redis.Redis(
                connection_pool=pool
            )
            con.hmset(id, {
                "title": title,
                "username": username,
                "type": type,
                "content": content,
                "is_top": is_top,
                "create_time": create_time
            })
            if is_top == 0:
                con.expire(id, 60*60*24)
        except Exception as e:
            print(e)
        finally:
            del con

    #删除新闻缓存数据
    def delete_cache(self, id):
        con = redis.Redis(
            connection_pool=pool
        )
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con