#!/usr/bin/python3
# -*- coingd: utf-8 -*-

import threading
import time
from queue import Queue

print(threading.active_count())  # 获取已激活的线程数
print(threading.enumerate())    # 查看所有线程信息
print(threading.current_thread())   # 查看现在正在运行的线程


def thread_job():
    print('current_thread is {}'.format(threading.current_thread()))


def main():
    thread = threading.Thread(target=thread_job,)   # 定义线程
    thread.start()  # 让后线程开始工作
    print(threading.active_count())


def T1_job():
    print('T1 start')
    for i in range(10):
        time.sleep(.1)
    print('T1 end')


def T2_job():
    print('T2 start')
    print('T2 end')


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    datas = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(datas[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for i in range(4):
        results.append(q.get())
    print(results)


def job1():
    global A, lock
    for i in range(10):
        A += 1
        print('job1', A)


def job2():
    global A, lock
    for i in range(10):
        A += 10
        print('job2', A)


if __name__ == '__main__':
    # for i in range(3):
    #     main()
    # print(threading.active_count())
    # t1 = threading.Thread(target=T1_job, name='T1')
    # t2 = threading.Thread(target=T2_job, name='T2')
    # t1.start()
    # t2.start()
    # t1.join()   # join函数会使得主调线程阻塞，直到被调用线程运行结束
    # t2.join()
    # print('all done')
    # multithreading()
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
