#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consuming %s'%n)
        r = '200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n+1
        print('producing %s'%n)
        r = c.send(n)
        print('consumer return %s'%r)
    c.close()

c = consumer()
produce(c)


import asyncio

@asyncio.coroutine
def hello():
    print('haha1')
    r = yield from asyncio.sleep(1)
    print('haha2')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
