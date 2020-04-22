# 进程池
import os
import random
import time
from multiprocessing.pool import Pool
from multiprocessing import current_process

def run(file_name, num):
    with open(file_name, 'a+', encoding='utf-8') as f:
        now_process = current_process()
        content = '{0}-{1}-{2}'.format(now_process.name, now_process.pid, num)
        f.write(content)
        f.write('\n')
        time.sleep(random.randint(1, 5))
        print(content)
    return 'ok'

if __name__ == '__main__':
    print(os.cpu_count())
    file_name = 'test_pool.txt'
    pool = Pool(2)
    rest_list = []
    for i in range(20):
        # rest = pool.apply(run, args=(file_name, i))
        rest = pool.apply_async(run, args=(file_name, i))
        rest_list.append(rest)
        # print('{0}----{1}'.format(i, rest.get()))
        print('{0}----{1}'.format(i, rest))
    pool.close()
    pool.join()
    print(rest_list[0].get())







def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.randint()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end -start)))

def use_pool():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print('Waiting for all subprocesses done....')
    p.close()
    p.join()
    print('All subprocesses done.')