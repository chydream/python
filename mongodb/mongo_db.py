# https://api.mongodb.com/python/current/tutorial.html
from pymongo import MongoClient #客户端代理对象执行curd操作内置了连接池
client = MongoClient(host="localhost", port=27017)
client.admin.authenticate("admin","123456")

