from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao:
    #保存新闻正文内容
    def insert(self, title, content):
        try:
            client.vega.news.insert_one({"title": title, "content": content})
        except Exception as e:
            print(e)

    #获取新闻正文id
    def search_content_id(self,title):
        try:
            result = client.vega.news.find_one({"title": title})
            # print(result["_id"])
            return result["_id"]
        except Exception as e:
            print(e)

    #修改新闻正文
    def update_content(self, id, title, content):
        try:
            client.vega.news.update_one({"_id": ObjectId(id)}, {"$set": {"title": title, "content": content}})
        except Exception as e:
            print(e)

        # 获取新闻正文id

    #获取新闻正文内容
    def search_content(self, id):
        try:
            result = client.vega.news.find_one({"_id": ObjectId(id)})
            return result["content"]
        except Exception as e:
            print(e)

    # 获取新闻正文内容
    def delete(self, id):
        try:
            client.vega.news.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            print(e)