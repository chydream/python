import datetime
from bson.objectid import ObjectId
from mongo_db import client
from gridfs import GridFS
# mongodb的文件存储
# GridFS是MongoDB的文件存储方案，使用2个集合来存储文件，chunks存放文件,files存储文件元数据
# GridFS会把文件分割成若干个chunks(256KB),然后在files记录他们
db = client.school
gfs = GridFS(db, collection="book")
# file = open("typescript-阮一峰.pdf", "rb")
# args = {"type": "PDF", "keyword": "typescript"}
# gfs.put(file, filename="typescript-阮一峰.pdf", **args)
# file.close()

# bk = gfs.find_one({"filename": "typescript-阮一峰.pdf"})
# print(bk.filename)
# print(bk.length/1024/1024)

books = gfs.find({"type": "PDF"})
for one in books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    uploadDate = uploadDate.strftime("%Y-%m-%d %H:%m:%S")
    print(datetime.timedelta())
    print(one._id, one.filename, uploadDate)

# exists函数可以判定GridFS是否存储某个文件
rs = gfs.exists(ObjectId("5ea26afac02a1ef6806e06e7"))
print(rs)
rs = gfs.exists(**{"type":"PDF"})
print(rs)

# document = gfs.get(ObjectId("5ea26afac02a1ef6806e06e7"))
# file = open("test.pdf", "wb")
# file.write(document.read())
# file.close()

gfs.delete(ObjectId("5ea26afac02a1ef6806e06e7"))