# from datetime import time
# a = set((1, 2, 3))
# print(a)
# # print "123"
# t = time(9,0)
# print(t)

# f = open('read.txt', 'r')
# text = f.readline()
# print('读取的数据是：', text)
# f.close()

# from functools import reduce
# def fn(x, y):
#     return x*10 +y
# def charToNum(s):
#     dict = {'0':0, '1':1, '2':2, '3':3, '4':4}
#     return dict[s]
# r1 = reduce(fn,map(charToNum,"23443"))
# print(r1)
# print(type(r1))


# class Vehicle(object):
#     # 自定义Vehicle类属性
#     trans_type = 'SUV'
#
#     # 自定义实例的初始化方法
#     def __init__(self, speed, size):
#         self.speed = speed
#         self.size = size
#
#     # 自定义实例方法show_info，打印实例的速度和体积
#     def show_info(self):
#         print("我的所属类型为：{0}，速度：{1}km/h,体积：{2}".format(Vehicle.trans_type, self.speed, self.size))
#
#     # 自定义实例方法move,打印“我已向前移动了50米”
#     def move(self):
#         print("我已向前移动了50米")
#
#     # 自定义实例方法set_speed，设置对应的速度值
#     def set_speed(self, new_speed):
#         self.speed = new_speed
#
#     # 自定义实例方法get_speed，打印当前的速度值
#     def get_speed(self):
#         print("我的时速为：设置的速度值 {0}km/h".format(self.speed))
#
#     # 自定义实例方法speed_up，实现对实例的加速
#     def speed_up(self):
#         print("我的速度由{0} km/提升到了{1} km/h".format(self.speed, self.speed + 10))
#         self.speed += 10
#
#     # 自定义实例方法speed_down，实现对实例的减速
#     def speed_down(self):
#         print("我的速度由{0} km/下降到了{1} km/h”".format(self.speed, self.speed - 15))
#         self.speed -= 15
#
#
# # 自定义实例方法transport_identify，实现对实例所属类型的判断
# def transport_identify(ast, bst):
#     if isinstance(ast, bst):
#         print('类型匹配')
#     else:
#         print('类型不匹配')
#
#
# if __name__ == "__main__":
#     tool_1 = Vehicle(20, (3.6, 1.9, 1.75))
#
#     # 调用实例方法 打印实例的速度和体积
#     tool_1.show_info()
#     # 调用实例方法 实现实例的前移
#     tool_1.move()
#     tool_1.set_speed(40)
#     # 调用实例方法 打印当前速度
#     tool_1.get_speed()
#     # 调用实例方法 对实例进行加速
#     tool_1.speed_up()
#     # 调用实例方法 对实例进行减速
#     tool_1.speed_down()
#     # 调用实例方法 判断当前实例的类型
#     transport_identify(tool_1, Vehicle)




# class Car(object):
#     # Car类的基本车型设置，列表形式
#     description = ['大众', '丰田', '广本', '沃尔沃', '凯迪拉克']
#     # 重写该类的构造方法，并将参数l、w、h、brand赋值给实例对象属性
#     def __init__(self,l,w,h,brand):
#         self.L = l
#         self.W = w
#         self.H = h
#         self.brand = brand
#     # 自定义该类的基本车型检索方法
#     def modify_des(self):
#         if hasattr(self, 'description'):
#             return True
#         else:
#             print('请输入您的车辆描述')
#             return False
#     # 自定义静态方法 提示用户：‘已完成车辆基本参数信息的录入！’
#     @staticmethod
#     def basic_parameters():
#         print("已完成车辆基本参数信息的录入！")
#     # 自定义类方法 根据用户车辆的品牌给出相应的合理保养建议
#     def upkeep(self,desc):
#         if desc in self.description:
#             print("根据汽车保养的相关经验，{0}品牌的车应于5000km/次的频率进行专业性保养".format(desc))
#         else:
#             print("非常抱歉！{0}品牌不在我们的保养范围内".format(desc))
# car_1 = Car(4.2, 1.8, 1.5, '大众')
#
# # 调用实例方法：basic_parameters（）
# car_1.basic_parameters()
# # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
# if  car_1.modify_des():
#     # 若if判断条件成立 则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc
#     car_1.upkeep('大众')
# # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
# else:
#     print('请正确填写相关的车辆信息')
# car_2 = Car(4.2, 1.8, 1.5, '保时捷')
#
# # 调用实例方法：basic_parameters（）
# car_2.basic_parameters()
# # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
# if car_2.modify_des():
#     # 若if判断条件成立，则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc
#     car_2.upkeep('什么')
# # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
# else:
#     print('请正确填写相关的车辆信息')

import re
pattern = re.compile(r'i.*?n,', re.I)
rest = pattern.match('I like python, i must learn python well')
print(rest)