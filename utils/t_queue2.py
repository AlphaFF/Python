#!/usr/bin/env python3
# coding=utf-8

import queue
import threading
import time
import random


# exitFlag = 0
#
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#
#     def run(self):
#         print('开启线程:' + self.name)
#         process_data(self.name, self.q)
#         print('退出线程:' + self.name)
#
#
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print('%s processing %s' % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
#
# threadList = ['thread-1', 'thread-2', 'thread-3']
# nameList = ['one', 'two', 'three', 'four']
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for _ in threadList:
#     thread = myThread(threadID, _, workQueue)
#     thread.start()
#     print('启动了：' + _)
#     thread.join()
#     print('结束了：' + _)
#     threads.append(thread)
#     threadID += 1
#     print(threadID)
#
# # 填充队列
# queueLock.acquire()
# for _ in nameList:
#     workQueue.put(_)
# queueLock.release()
#
# while not workQueue.empty():
#     pass
#
# exitFlag = 1
#
# print(threads)
#
# # for _ in threads:
# #     _.join()
#
# print('退出主线程...')

class Producer(threading.Thread):
    '''
    生产者线程
    '''

    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.queue = queue

    def run(self):
        for i in range(10):
            print('%s is producing %d to the queue' % (self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10) / 5)
        print('%s finished' % self.getName())


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(5):
            val = self.queue.get()
            print('%s is consuming. %d in the queue is consumed!' % (self.getName(), val))
            time.sleep(random.randrange(10))
        print('%s finished!' % self.getName())


def main():
    q = queue.Queue()
    producer = Producer('producer', q)
    consumer = Consumer('consumer', q)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print('ended...')


if __name__ == '__main__':
    main()


# class ConsumeEven(threading.Thread):
#     def __init__(self, t_name, queue):
#         threading.Thread.__init__(self, t_name)
#         self.name = t_name
#
#     def run(self):
#         while True:
#             try:
#                 queue_val = self.queue.get(1, 3)
#             except Exception as e:
#                 print(e)
#                 break
#             if queue_val % 2 == 0:
#                 print('get even num {queue_val}'.format(str(queue_val)))
#             else:
#                 self.queue.put(queue_val)



# 线程代码
# class TaksThread(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self, name=name)
#
#     def run(self):
#         print('thread %s is running...' % self.getName())
#
#         for i in range(6):
#             print('thread %s >>> %s' % (self.getName(), i))
#             time.sleep(1)
#         print('thread %s finished...' % self.getName())
#
# taskThread = TaksThread('taskThread')
# taskThread.start()
# taskThread.join()
#
# print('task ended...')
