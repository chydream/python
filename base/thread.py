# 线程 进程 协程
# 1.进程  执行中的程序 拥有自己的地址空间
# 2.线程  同一个进程下执行并共享相同的上下文 包括开始、执行顺序和结束 可以被抢占中断和临时挂起睡眠 让步
# 3.并发  程序 算法或问题的属性，只是并发问题的可能方法之一，如果两个事件互不影响，则两个事件是并发的
# 单核cpu系统中，不存在真正的并发   GIL 全局解释器锁 只是强制在任何时候只有一个线程可以执行python代码
# I/O密集型应用于cpu密集型应用
# GIL执行顺序，
# 1.设置GIL
# 2.切换一个线程去运行
# 3.执行下面操作之一：
# 指定数量的字节码指令
# 线程主动让出控制权(time.sleep(0))
# 4.把线程设置回睡眠状态
# 5.解锁GIL

#一、线程  用threading模块代替thread模块  threading.Tread创建线程  start()启动线程  join()挂起线程
# Thread 对象属性 name ident  daemon
# 多线程中的锁  Lock()  Rlock()  Condition()

import threading, time
def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def test_loop():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    print('t.name', t.name)
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


class LoopThread(threading.Thread):
    n = 0
    def run(self):
        while self.n < 5:
            self.n = self.n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, self.n))
            time.sleep(1)


balance = 0
lock = threading.Lock()  #不可以重复锁定 死锁
r_lock = threading.RLock() #可以重复锁定
def change_it(n):
    global balance
    balance = balance + n
    time.sleep(2)
    balance = balance - n
    time.sleep(1)
    print(">>>>>>>>n:%d %s" % (n, balance))

def run_thread(n):
    for i in range(10):
        # print(i)

        with r_lock:
            change_it(n)

        # lock.acquire() #获取锁
        # r_lock.acquire()
        # try:
        #     change_it(n)
        # finally:
        #     lock.release() #改完了释放锁
        #     r_lock.release()

t1 = threading.Thread(target=run_thread, args=(5,),name='t1')
t2 = threading.Thread(target=run_thread, args=(8,),name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# test_loop()
# t = LoopThread(name='LoopThread')
# t.start()
# t.join()
