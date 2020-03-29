import os
# os.environ
# os.system('calc')
print(os.sep)
os.chdir('desktop')
os.getcwd()  # 当前所在目录
os.listdir()
os.mkdir('hello')
os.rename('hello', 'world')
os.rmdir('world')
os.path() #文件目录相关操作
os.path.isdir('py_learn') #是否文件夹
os.path.isfile('py_learn') #是否文件
os.path.exists('you')
os.path.dirname()
os.path.split()
os.path.basename()
os.path.splitext()
os.makedirs()
os.path.join()