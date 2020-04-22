import  threading, time
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool as ThreadPool

def run(n):
    time.sleep(1)
    print(threading.current_thread().name, n)

def main():
    # t1 = time.time()
    # for n in range(10):
    #     run(n)
    # print(time.time() - t1)


    t1 = time.time()
    n_list = range(100)
    pool = ThreadPool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    print(time.time() - t1)


    # t1 = time.time()
    # ls = []
    # for count in range(10):
    #     for i in range(10):
    #         t = threading.Thread(target=run, args=(i,))
    #         ls.append(t)
    #         t.start()
    #
    #     for l in ls:
    #         l.join()
    # print(time.time() - t1)

def main1():
    t1 = time.time()
    n_list = range(100)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run, n_list)
    print(time.time() - t1)

if __name__ == '__main__':
    main1()
