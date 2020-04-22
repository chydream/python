# 1.进程  执行中的程序 拥有自己的地址空间
# multiprocessing 实现多进程 multiprocessing.Process创建进程 start() join()  os.getpid() 获取进程的ID
# ps -ef | grep python
import os
# print(os.getpid())
import time
from multiprocessing.context import Process


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(150)
    print('time is sleeping done.')

def use_process():
    print('parent process: %d' % os.getpid())
    p = Process(target = run_proc, args=['test'])
    print('child process will start.')
    p.start()
    p.join()
    print('child process end.')

class MyProcess(Process):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.my_name = name

    def run(self):
        print('Run child process %s (%s)...' % (self.my_name, os.getpid()))
        time.sleep(5)
        print('time is sleeping done.')

if __name__ == '__main__':
    # use_process()
    mp = MyProcess('test11')
    mp.start()
    mp.join()