# 协程  协同多任务 在一个进程或一个线程中执行 不需要锁机制
# 对多核cpu的利用 多进程+协程  yield 3.15前  3.15后 async await
# asyncio 模块  get_event_loop()获得事件循环队列   run_until_complete() 注册任务到队列 在事件循环中调度其执行前，协程对象不执行任何操作
import  asyncio
import random



def count_down(n):
    while n > 0:
        yield n
        n -= 1

def yield_test():
    while True:
        n = (yield )
        print(n)

async def async_f():  # 当被调用是，不执行里面的代码，而是返回一个协程对象 在事件循环调度执行前，协程对象不执行任何操作
    pass

async def do_sth(x):
    print('等待中：{0}'.format(x))
    await asyncio.sleep(x)

async def compute(x, y):
    print('compute %s + %s ....' % (x, y))
    await asyncio.sleep(1.0)
    return  x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s = %s = %s" % (x,y,result))

async def add(name,store):
    for i in range(5):
        await asyncio.sleep(random.randint(1, 5))
        num = '{0}-{1}'.format(name, i)
        await store.put(num)
        print('{2} add one ...{0},size:{1}'.format(num, store.qsize(), name))

async def reduce(name,store):
    for i in range(10):
        rest = await store.get()
        print('{2} reduce one ...{0},size:{1}'.format(rest, store.qsize(), name))


if __name__ == '__main__':
    store = asyncio.Queue(maxsize=5)
    a1 = add('test', store)
    a2 = add('test1', store)
    r1 = reduce('test2', store)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(a1, a2, r1))
    loop.close()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(print_sum(1, 2))
    # loop.close()


    # rest = count_down(5)
    # print(next(rest))
    # rest = yield_test()
    # next(rest)
    # rest.send('6666')


    # print(asyncio.iscoroutinefunction(do_sth))
    # coroutine = do_sth(5)
    # loop = asyncio.get_event_loop() #事件循环队列
    # task = loop.create_task(coroutine) #注册任务
    # print(task)
    # loop.run_until_complete(task) #等待协程任务执行结束
    # print(task)