import redis
# r = redis.Redis(
#     host="localhost",
#     port=6379,
#     password="123456",
#     db=0
# )
pool = redis.ConnectionPool(
    host="localhost",
    port=6379,
    password="123456",
    db=0,
    max_connections=20
)
r = redis.Redis(
    connection_pool=pool
)
del r