#!/usr/bin/env python3
# coding=utf-8

# 单例模式
# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class MySingleton(Singleton):
#     pass
#
#
# a = MySingleton()
# b = MySingleton()

# print(a is b)

class G(float):
    def __new__(cls, kg):
        return float.__new__(cls,kg*2)

a = G(50)
print(a)

import scrapy


