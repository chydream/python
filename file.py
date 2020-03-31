# open() close()
# r 读 w 写 a 追加 b 二进制模式 x独占写入模式 t文本模式 +读写模式
# r w a x只能选一种读写模式 不可以联合用  b t d应联合
f = open('tool.py')
# dir(f)
# help(f)
# print(f)
f.close()

# 自动关闭
with open('base.py') as b:
    print(123)

# read()
def read_file():
    file_name = 'read.txt'
    file_path = 'G:\\python\\python\\read.txt'
    file_path2 = 'G:/python/python/read.txt'
    f = open(file_name, encoding='utf-8')
    # rest = f.read()
    # rest = f.read(4)
    # print(rest)
    # print(f.read(4))
    # f.seek(2) #英文
    # print(f.read(4))
    # print(f.readline())
    # print(f.readline())
    print(f.readlines())
    f.close()

read_file()

# write()
def write_file():
    file_name="read.txt"
    f = open(file_name, 'a', encoding='utf-8')
    f.write('\n')
    f.write('hello')
    f.write('\n')   # \n \r  \r\n
    f.write('world')
    l = ['第一行', '\n', '第二行', '\n',  '第三行']
    f.writelines("hell1233")
    f.writelines(l)
    f.close()
write_file()

def read_and_write():
    file_name = 'read.txt'
    with open(file_name,'r+',encoding='utf-8') as f:
        read_rest = f.read()
        if '1' in read_rest:
            f.write('bbb')
        else:
            f.write('aaa')
        f.write('\n')
read_and_write()