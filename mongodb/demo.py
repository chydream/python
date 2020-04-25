from mongo_db import client

#数据写入
# client.school.teacher.insert_one({"name": "李璐"})
# client.school.teacher.insert_many([
#     {"name": "陈刚"},
#     {"name": "郭丽丽"}
# ])
#数据查询
# teachers = client.school.teacher.find({})
# for one in teachers:
#     pass
#     # print(one)
# teacher = client.school.teacher.find_one({"name": "李璐"})
# print(teacher)
#数据修改
# client.school.teacher.update_many({}, {"$set": {"role": ["班主任"]}})
# client.school.teacher.update_one({"name": "李璐"}, {"$set": {"sex": "男"}})
# client.school.teacher.update_one({"name": "李璐"}, {"$push": {"role": "年级主任"}})
# 数据删除
# client.school.teacher.delete_one({"name":"李璐"})
# client.school.teacher.delete_many({})
# 其他操作
client.school.teacher.find({}).skip(0).limit(10)
client.school.teacher.count()
client.school.teacher.distinct("name")
client.school.teacher.find().sort([("name", -1)])