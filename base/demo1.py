# f = open('1.txt', 'r')
# try:
#     f = open('1.txt', 'r')
#     try:
#         content = f.read()
#         print(content)
#         f.close()
#     except NameError as error:
#         print("名称未定义")
# except FileNotFoundError as error:
#     print("该文件不存在")
# else:
#     print("改程序没有异常")

class Imooc(object):
    __slots__ = ('name', 'age', 'run')

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        return "Imooc"

def run():
    print("run")

if __name__ == '__main__':
    imooc = Imooc('小梅', 20)
    imooc.run = run
    imooc.run()