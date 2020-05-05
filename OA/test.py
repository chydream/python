import os
from bson import ObjectId
from gridfs import GridFS
from pymongo import MongoClient
filePath = 'G:\python\OA\data1.txt'
# filePath1 = 'data.txt'
# fullpath = os.getcwd() + "\\" + filePath1
# print(fullpath)
# print(os.path.dirname(filePath))
# print(os.path.split(filePath1))
# print(os.path.basename(filePath))
# print(os.path.dirname(filePath))
# print(os.path.splitext(filePath))
# print(os.path.split(filePath))
# print(os.path.join(os.path.dirname(filePath), os.path.basename(filePath)))
# print(os.path.basename(os.path.join(os.path.dirname(filePath), os.path.basename(filePath))))
# print(os.path.getsize(filePath))
# f = open(filePath, "r", encoding="utf-8")
# file = f.read()
# print(file)
# f.close()

client = MongoClient(host="localhost", port=27017)
client.admin.authenticate("admin","123456")
db = client.oa
gfs = GridFS(db, collection="oa")
file = open(filePath, 'rb')
args = {}
args["type"] = os.path.splitext(filePath)[1]
args["name"] = os.path.basename(filePath)
gfs.put(file, filename=os.path.basename(filePath), **args)
# txt = gfs.find_one({"_id": ObjectId("5eac21f3ff46b1ca1c4419fb")})
# print(dir(txt))
# print(txt.filename)

# txt1 = client.oa.oa.files.find_one({"_id": ObjectId("5eac21f3ff46b1ca1c4419fb")})
# print(txt1)


# data_txt = gfs.get(ObjectId("5eac21f3ff46b1ca1c4419fb"))
# new_file = open("test1.txt", "wb")
# new_file.write(data_txt.read())
# new_file.close()
# for one in txt:
#     print(one.decode("utf-8"))

file.close()