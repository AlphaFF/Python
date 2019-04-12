#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2019-04-10 15:18:50
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2019-04-10 16:14:30

from functools import wraps


class My_Singleton:
    def foo(self):
        print('fooooo.')


my_singleton = My_Singleton()


class Singleton:
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class Singleton1:
    a = 1


a = Singleton()
b = Singleton()
c = Singleton()

print(a is b)
print(b is c)


a1 = Singleton1()
b1 = Singleton1()
c1 = Singleton1()
print(a1 is b1)


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        print(instances)
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance


@singleton
class MyClass:
    a = 1


a2 = MyClass()
b2 = MyClass()

print(a2 is b2)


class Singleton2(type):
    _instances = {}

    def __call__(cls, *args, **kw):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instances[cls]


class MyClass2(metaclass=Singleton2):
    pass


def test_hello(self, name):
    print('hello', name)


Hello = type('Hello', (object, ), dict(hello='hello world', test=test_hello))

h = Hello()
print(h.hello)
print(h.test('zhangsan'))
