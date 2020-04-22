# 1.装饰器
# def hello():
#     print("hello world")
#
# def log(func):
#     print('start')
#     func()
#     print('end')

# **********************************
# def log_in(func):
#     def wrapper():
#         print("start....")
#         func()
#         print('end...')
#     return wrapper
#
# def log_n(func):
#     def wraaper():
#         print("开始")
#         func()
#         print("结束")
#     return wraaper
#
# @log_n
# @log_in #使用装饰器
# def hello_wrapper():
#     print('hello wrapper')

# ***************************
# def log(text = None):
#     def decorator(func):
#         @wraps(func)
#         def wrapper（*args, **kwargs):
#             print("---start-----")
#             print('%s %s():' % (text,func.__name__))
#             rest = func(*args,**kwargs)
#             print("-----end------")
#             return rest
#         return wrapper
#     return decorator
from functools import wraps


def log(name=None):
    def decorator(func):
        @wraps(func)  #还原func属性方法
        def wrapper2(*args, **kwargs):
            """wrapper2"""
            print("{0}start....".format(name))
            print('wrapper:{0}'.format(func.__doc__))
            print('wrapper:{0}'.format(func.__name__))
            # print(args)
            # print(kwargs)
            res = func(*args, **kwargs)
            print('{0}end...'.format(name))
            return res
        # wrapper2.__doc__ = func.__doc__
        # wrapper2.__name__ = func.__name__
        return wrapper2
    return decorator

@log('from hello ')
def hello(a, b, *args, **kwargs):
    """hello"""
    res = a + b
    return res

#************************************************************
def f(self):
    print(111111)

def eat(cls):
    # cls.eat = lambda self: print('{0}我要吃东西'.format(self.name))
    cls.eat = f
    return cls

@eat
class Cat(object):
    """猫类"""
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    # log(hello)
    # hello_wrapper()
    # rest = hello(3, 5, k = 2, v = 6)
    # print(rest)
    # print('doc:{0}'.format(hello.__doc__))
    # print('name:{0}'.format(hello.__name__))
    # hello(2,3)
    cat = Cat('小黑')
    cat.eat()