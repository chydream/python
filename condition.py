# 一. 条件语句
age = 25
if age < 20:
    print('111')
elif age > 20 and age < 30:
    print('222')
else:
    print('2222')

#数字0代表False, 非0代表True
print(1 == 1.0)
print(1 == int("1"))
#逻辑运算符 not  and or  not > and > or 英文
'''
weight = input('请输入您的体重（kg）:')
height = input('请输入您的身高（m）:')
bmi = int(weight)/pow(float(height), 2)
print(format(bmi, '0.2f'))
if bmi <= 18.4:
    print('偏瘦')
elif bmi > 18.4 and bmi <= 23.9:
    print('评测结果：正常')
elif bmi > 23.9 and bmi <=27.9:
    print('偏重')
else:
    print('肥胖')
'''

# 二.循环语句
# 阶乘
# i = 1
# sum = 1
# n = input("请输入阶乘数字")
# while i <= int(n):
#     sum = sum * i
#     if sum % 5 == 0:
#         print(sum)
#     print(sum)
#     i = i + 1

