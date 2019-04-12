#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wangfeng1
# @Date:   2019-02-15 14:31:39
# @Email: liushahedi@gmail.com
# @Last Modified by:   wangfeng1
# @Last Modified time: 2019-02-15 17:17:50
import inspect
from functools import wraps
from collections import namedtuple


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()

print(my_coro)
print(inspect.getgeneratorstate(my_coro))
print(next(my_coro))
print(inspect.getgeneratorstate(my_coro))
# print(my_coro.send(42))


def simple_coro2(a):
    print('-> started: a =', a)
    b = yield a
    print('-> received: b =', b)
    c = yield a + b
    print('-> received: c =', c)


# my_coro2 = simple_coro2(14)
# print(my_coro2)
# print(next(my_coro2))
# print(my_coro2.send(28))
# print(my_coro2.send(99))


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(4))
print(coro_avg.send(8))
print(coro_avg.send(12))


def averager1():
    total = 0
    count = 0

    def avg(new_value):
        nonlocal total, count
        total += new_value
        count += 1
        return total / count
    return avg


avg = averager1()
print(avg(4))
print(avg(5))
print(avg(7))


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager1():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


avg = averager1()
print(avg.send(6))
print(avg.send(12))


def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


print(list(gen()))


def gen1():
    yield from 'AB'
    yield from range(1, 3)


print(list(gen1()))


Result = namedtuple('Result', 'count average')


# 子生成器
def averager2():
    total = 0
    count = 0
    while True:
        term = yield
        if not term:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# 委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager2()
        print('----', results)


# 调用方
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3],
    'girls;m': [1.6, 1.51, 1.4],
    'boys;kg': [39.0, 40.8, 43.2],
    'boys;m': [1.38, 1.5, 1.32]
}


if __name__ == '__main__':
    main(data)
