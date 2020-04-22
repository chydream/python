# 内存机制
# 以引用计数为主，分代收集为辅，引用数为0，就会回收这个对象内存，引用计数的缺陷是循环引用的问题
# 查看某个对象的引用计数 sys.getrefcount()  del 删除引用
# 满足特定条件，自动回收
# python运行时，会记录其中分配对象和取消分配对象的次数
# 当两者的差值高于某个阈值时，会启动垃圾回收
# 查看阈值 gc.get_threshold() 分代回收
# python将所有的对象分为0,1,2三代
# 所有新建对象都是0带对象
# 当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象
# gc.collect() 手动回收 0， 1， 2
# objgraph 模块中的count()记录当前类产生的实例对象的个数
# 内存管理机制 内存池机制  Pymalloc
import sys
import gc
import objgraph

# print(gc.get_threshold())
class Person(object):
    pass

class Cat(object):
    pass

p1 = Person()
# p2 = Person()
c1 = Cat()
# c2 = Cat()
p1.name = 'susan'
p1.pet = c1
c1.master = p1

print(sys.getrefcount(p1))
print(sys.getrefcount(c1))

del p1
del c1

gc.collect()
print(objgraph.count('Person'))
print(objgraph.count('Cat'))

t = []
t2 = t
t3 = t
t4 = t3
del t4
i = 5
# print(sys.getrefcount(i))
k = i
# print(sys.getrefcount(t))
# print(sys.getrefcount(i))
# print(t4)


l = [123]
d = id(l)
# print(d)
a = 5
b = 5
# print(id(a))
# print(id(b))
# print(a == b) #值比较
# print(a is b) #内存地址比较

def extend_list(val, l=[]):
    l.append(val)
    return l
list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')
# print(id(list1))
# print(id(list2))
# print(id(list3))
# print(list1)
# print(list3)

class ClassGc():
    def __init__(self):
        print('对象产生：{0}'.format(id(self)))
    def __del__(self):
        print('对象删除：{0}'.format(id(self)))

def f0():
    while True:
        c1 = ClassGc()

def f1():
    l = []
    while True:
        c1 = ClassGc()
        l.append(c1)
        print(len(l))

if __name__ == '__main__':
    a = ''
    # f0()