#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing


def job(a, d):
    print(a + d)


def job1(x):
    global v
    v.value += x
    return x * x


def multicore():
    p = multiprocessing.Pool()
    res = p.map(job1, range(4))
    print(res)
    # res = p.apply_async(job1, (2, ))
    # print(res.get())
    print('v:', v.value)


v = multiprocessing.Value('i', 0)
print(v.value)
# v1 = multiprocessing.Array('i', [1, 2])
# v2 = deepcopy(list(v1))
# print(v2)

if __name__ == '__main__':
    # p1 = multiprocessing.Process(target=job, args=(1, 2))
    # p1.start()
    # p1.join()
    # print('ending')
    multicore()
    pass
