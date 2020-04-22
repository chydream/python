# 1.迭代器 实现了方法__iter__的对象是可迭代的，实现方法__next__的对象是迭代器
class PowNum(object):
    """生成平方数"""
    value = 0
    def __next__(self):
        self.value += 1
        if self.value >= 10:
            raise StopIteration
        return self.value * self.value

    def __iter__(self):
        return self

if __name__ == '__main__':
    p = PowNum()
    # print(p.__next__())
    # print(p.__next__())
    # print(p.__next__())
    # print(next(p))
    # for i in p:
    #     print(i)
    l = [1, 2, 3] # 可迭代对象
    ll = iter(l) # 获取迭代器
    # print(next(ll))
    # print(next(ll))
    # print(next(ll))
    # print(next(ll))

# 2.生成器 用普通函数语法定义的迭代器 包含yield语句的函数
def pow():
    # yield 1
    # yield 2
    # yield 3
    # yield 4
    # return  (x * x for x in [1, 2, 3, 4, 5])
    for x in [1, 2, 3, 4, 5]:
        yield x * x

# 3.range
def use_range():
    for i in range(5, 10):
        print(i)

class IterRange(object):
    """迭代器模拟range"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self

class GenRange(object):
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end
    def get_num(self):
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start

def get_num(start, end):
    start -= 1
    while True:
        if start >= end - 1:
            break
        start += 1
        yield start

if __name__ == '__main__':
    rest = pow()
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(range(5,10))
    # use_range()
    print(list(get_num(1,10)))