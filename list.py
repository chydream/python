# 列表与字典 可变类型的数据集合
#一、列表 List  按顺序排列 正序和倒序索引  任意类型 允许重复  多维列表
a = ['str', 1, 'a', 2]
b = []
print(a)
print(a[0])
print(len(a))
list1 = a[0:2]  #左闭右开 返回列表
print(list1)
i = a.index(2)
print(i)
for x in a:
    print(a.index(x))
a.reverse()
print(a)
numbers = [28, 32, 14, 12, 53, 42]
numbers.sort()  #升序
numbers.sort(reverse=True) #降序
numbers.append(50)
numbers.insert(0,10)
numbers.remove(32)
print(numbers)
numbers.pop(4)
print(numbers)
numbers[3:5] = []
numbers.count(12)  #统计出现次数
numbers.append([1, 2, 3])
numbers.extend([4, 5])
bool = 4 in numbers
n = numbers.copy()
n.clear()


#二、元组 Tuple  不可变的列表 () 元组数据不可变
tup1 = ('physics', 'chemistry',  1997, 2000)
# (5, 6, 7) + (8, 9, 10) = (5, 6, 7, 8, 9, 10)  适用所有列表
# ('see', 'you') * 2 = ('see', 'you', 'see', 'you') 适用所有列表
t = ('a', 'b', 'c', 1, 2, 3)   # 'a', 'b', 'c', 1, 2, 3
print(t[3])
print(t[1:4])
print('b' in t)
# 如果元组内持有列表，列表内容允许被修改
([1, 2, 3], [4, 5, 6])
t4 = ('see',)*2  #只有一个元素 加逗号 元组
t5 = (10,)*10


#三、字典 Dictionary  key不能重复 value可以重复  dict
dict1 = {
    "key": "value",
    "key1": "value1"
}
print(dict1.get('key', 222))
print(dict1['key'])
print('key' in dict1)
dict3 = dict(name='汪峰', sex='男', birthdate='1997-10-20')
dict4 = dict.fromkeys(['name', 'sex', 'birthdate'], 'N/A')
for key in dict1:
    print(key)
for key,value in dict1.items():
    print(value)
dict1.update(key='222', key1='333')
dict1.pop('key1')
dict1.popitem()
dict1.clear()

emp1 = {'name': 'Jacky', 'grade': 'B'}
emp2 = {'name': 'Lily'}
if 'grade' not in emp2:
    emp2['grade'] = 'C'
emp2.setdefault('grade', 'C')  #存在则忽略，不存在则设置
emp2.keys()
emp2.values()
emp2.items()
# emp_str = "姓名：%(name)s,评级：%(grade)s,入职时间：%(hiredate)s" %emp1
# emp_str1 = "姓名：{name},评级：{grade},入职时间：{hiredate}".format_map(emp1)
# 字典也称为"哈希（Hash）",对应散列值
h1 = hash('abc')
h2 = hash(88888846)


#四、集合 Set。  无序，不能重复，可变，允许数学运算，分散存储
{'张三', '李四', '王五', '赵六'}
college1 = {"哲学", "经济学", "法学", "教育学"}
college2 = set(["金融学", "哲学", "经济学", "文学"])
college3 = set("中国经济学")
college4 = set()
# 交集 并集 差集
college5 = college1.intersection(college2)
college6 = college1.intersection_update(college2) # 更新原始集合
college7 = college1.union(college2)
college8 = college1.difference(college2)
college8 = college1.difference_update(college2)
college9 = college1.symmetric_difference(college2)
college9 = college1.symmetric_difference_update(college2)
s1 = {1, 2, 3}
s2 = {3, 2, 1, 7, 9, 8}
print(s1 == s2)
print(s1.issubset(s2))  # 子集
print(s2.issuperset(s1)) # 超集
print(s1.isdisjoint(s2))  # 是否存在重复元素  True是不存在 False 存在
#集合增 删 改 查
#遍历
for c in college1:
    print(c)
print("数学" in college1)
college1.add("数学")
college1.update(["语文", "英语"])
college1.remove("数学") #删除不存在的元素会报错
college1.discard("数学") #删除不存在会忽略

#生成式语法 [被追加的数据 循环语句 循环或者判断语句]|{}
lst = [i*10 for i in range(10, 20) if i % 2 == 0]
lst5 = ['张三', '李四', '王五']
dict1 = {i+1: lst5[i] for i in range(0, len(lst5))}
set1 = {i*j for i in range(1,4) for j in range(1,4) if i == j}


#五、序列  Str List  元组 数字序列 range，数据结构的统称
r1 = range(10, 20, 2) #左闭右开
print(r1)
print(type(r1))
print(r1[3:5])
print(11 in r1)
c="abcdefg"
for i in range(0,len(c)):
    print(c[i])

# list() 转换为列表
# tuple() #转换为元组
# join() str() #转换为字符串
l1 = ['a', 'b', 'c']
t1 = ('d', 'e', 'f')
s1 = 'abc123'
s2 = 'abc,123'
r1 = range(1, 4)
" ".join(l1)  #join 必须所有元素都是字符串



# 斐波那契数列
# 1 1 2 3 5 8
result = []
for i in range(0, 50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i-2] + result[i-1])
print(result)