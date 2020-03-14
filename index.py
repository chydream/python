#一.基本知识
# 这行是注释
"""块注释"""
print("hello")
print(3+2)
name = "毛主席"
salary = 1938.8
is_weekend = True
print(name)
isType = type(salary) == float
print(isType)
print(2**3)
print(78//10)
# str int float bool 4种数据类型
# print() type()  input()函数
# int() float() str() bool()  类型转换函数
# name = input("请输入您的姓名：")
# print(name)
print(name + str(1223))
#二.字符串
#1.拼接 +， str.lower() str.upper() str.title() str.capitalize() str.swapcase() str.format()
mo = 1234.568
str = "{} {} you {:0,.2f}"
strNew = str.format("i", "love", mo)
print(strNew)
# format(1234.567,0.2f)  保留2位小数
# format(1234.567,',') 千分位分隔符
# format(1234.568,0,.3f)  千分位 保留2位小数
name = "张三"
age = 25
weight = 83.5
print(" %s years old %d %.1f"%(name,age,weight))
# 特殊字符 \t 制表符 \n 换行符  str.lstrip()  str.rstrip()  str.strip()  删除空格  len()长度