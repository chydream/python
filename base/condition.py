# 一. 条件语句
# age = 25
# if age < 20:
#     print('111')
# elif age > 20 and age < 30:
#     print('222')
# else:
#     print('2222')

#数字0代表False, 非0代表True
# print(1 == 1.0)
# print(1 == int("1"))
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

# continue break
# continue和break都是在循环中使用，continue用于跳出本次循环执行下一次循环，break在单循环中，结束循环且程序终止。在多层循环嵌套中，break只结束当前循环
# start = 101
# end = 183
# i = 100
# while i <= 182:
#    i = i + 1
#    # if i % 13 != 0:
#    #     continue
#    if i % 14 == 0:
#        break
#    print(i)


# j = 0
# while j < 4:
#     i = 0
#     while i < 4:
#         print("口", end="") #结尾不换行
#         i = i +1
#     j = j + 1
#     print("")



# n = 1
# while n <= 4:
#     x = 1
#     while x <= 4 - n:
#         print(" ", end="")
#         x = x + 1
#     y = 1
#     while y <= (2*n - 1):
#         print("*", end="")
#         y = y + 1
#     n = n + 1
#     print("")

# 求质数
j = 1
jNum = 20
while j <= jNum:
    num = j
    i = 2
    isPrime = True
    while i < j:
        if j % i == 0:
            isPrime = False
            break
        i = i + 1
    if isPrime:
        print("{} 是质数".format(j))
    j = j + 1
