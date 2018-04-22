#!/usr/bin/env python3
# coding=utf-8

from queue import Queue
import threading
import time

q = Queue()
lock = threading.Lock()
hosts = ['http1','http2','http3']

def printMsg(msg):
    global lock
    if lock.acquire():
        print(msg)
        lock.release()

class ThreadUrl(threading.Thread):
    def __init__(self,q,htint):
        super(ThreadUrl,self).__init__()
        self.q = q
        self.htint = htint

    def run(self):
        while True:
            host = self.q.get()
            print(self.q.qsize())
            if self.q.empty():
                printMsg('msg')
            self.q.task_done()

def main():
    for i in range(5):
        t = ThreadUrl(q,i)
        t.setDaemon(True)
        t.start()
        for host in hosts:
            printMsg('queue put')
            q.put(host)
        q.join()

if __name__ == '__main__':
    start = time.time()
    main()
    time.sleep(1)
    costTime = time.time() - start - 1
    print('elapsed time:%s'%costTime)
