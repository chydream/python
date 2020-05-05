from db.mongo_db import client
from gridfs import GridFS
from bson import ObjectId
import os

class MongoFileDao:
    # 插入文件
    def add_file(self, fileinfo):
        try:
            db = client.oa
            gfs = GridFS(db, collection="t_file")
            print(fileinfo['filePath'])
            file = open(fileinfo['filePath'], "rb")
            gfs.put(file, **fileinfo)
        except Exception as e:
            print(e)
        finally:
            file.close()

    # 获取文件
    def get_file(self, id):
        try:
            db = client.oa
            gfs = GridFS(db, collection="t_file")
            result = gfs.find_one({"_id", ObjectId(id)})
            return result
        except Exception as e:
            print(e)
        finally:
            pass

    # 获取文件id
    def get_file_id(self, fileinfo):
        try:
            db = client.oa
            gfs = GridFS(db, collection="t_file")
            result = gfs.find_one(fileinfo)
            return result._id
        except Exception as e:
            print(e)
        finally:
            pass

    #删除文件
    def delete_file(self, id):
        try:
            db = client.oa
            gfs = GridFS(db, collection="t_file")
            gfs.delete(ObjectId(id))
        except Exception as e:
            print(e)
        finally:
            pass

    #下载文件
    def download_file(self, id, new_path):
        try:
            db = client.oa
            gfs = GridFS(db, collection="t_file")
            down_file = gfs.get(ObjectId(id))
            # print(new_path+down_file.filename)
            file = open(new_path+down_file.filename, "wb")
            file.write(down_file.read())
        except Exception as e:
            print(e)
        finally:
            file.close()