# 进程之间的通信 Queue Pipes
# 多进程锁 Lock() Rlock() Condition()
from multiprocessing import Process, Queue, Lock, RLock
import os, time, random


class WriteProcessN(Process):
    def __init__(self, file_name, num, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.num = num
        self.lock = lock

    def run(self):
        with self.lock:
            for i in range(5):
                with open(self.file_name, 'a+', encoding='utf-8') as f:
                    content = "现在是{0}：{1}-{2} \n".format(self.name, self.pid, self.num)
                    f.write(content)
                    time.sleep(random.randint(1, 5))
                    print(content)


        # try:
        #     self.lock.acquire()
        #     for i in range(5):
        #         with open(self.file_name, 'a+', encoding='utf-8') as f:
        #             content = "现在是{0}：{1}-{2} \n".format(self.name, self.pid, self.num)
        #             f.write(content)
        #             time.sleep(random.randint(1,5))
        #             print(content)
        # finally:
        #     self.lock.release()

if __name__ == '__main__':
    file_name = 'test.txt'
    lock = RLock()
    for x in range(5):
        p = WriteProcessN(file_name, x, lock)
        p.start()



def write(q):
    print('Process to wirte: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(1)

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)



class WriteProcess(Process):
    def __init__(self, q, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.q = q

    def run(self):
        ls = ['第1行内容', '第2行内容', '第3行内容', '第4行内容']
        for line in ls:
            print('write %s from queue.' % line)
            self.q.put(line)
            time.sleep(random.randint(1, 5))

class ReadProcess(Process):
    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q

    def run(self):
        while True:
            value = self.q.get(True)
            print('Get %s from queue.' % value)

# if __name__ == '__main__':
#     q = Queue()
#     t_write = WriteProcess(q)
#     t_write.start()
#     t_read = ReadProcess(q)
#     t_read.start()
#     t_write.join()
#     t_read.join()
#     t_read.terminate()