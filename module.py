# cd dir cls exit
# python exit()  quit()  python test.py
# python标准模块  第三方模块pypi.org    自定义模块
# 模块就是程序，模块名是不含.py后缀的文件名
# 包 - 标准库内置函数 - sys.path
# dir - 列出对象属性和方法
# help
#__name__  __file__
import  moduleDemo
moduleDemo.func()
print(dir(moduleDemo))
print(moduleDemo.__doc__)
# help(moduleDemo)
print(moduleDemo.__name__)
print(moduleDemo.__file__)
help(moduleDemo.func)

#包：可以用来组织模块 目录必须包含文件 __init__.py,解决模块重名问题    PEP8
# imort顺序 1.标准库 2.第三方库包 3.自定义的包   包导入是包下面的__init__.py
# 包是一个文件夹，可以包含多个文件/模块，模块是一个文件。
import pay
# from pay.alipay import tools
# from pay.alipay.tools import pay
from pay.alipay import tools as tl
# from pay.alipay.tools import *
# def funct():
#     import  pay #局部引入
def func2():
    pay.alipay.tools.pay()
    tl.pay()
func2()