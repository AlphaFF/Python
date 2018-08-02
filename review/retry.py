#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__: AlphaFF

import functools


# 不带参数
def _retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        return func(*args, **kw)
    return wrapper


# 带参数
def retry(retries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            index = 0
            while index <= 3:
                res = func(*args, **kw)
                if res.status_codr == 200:
                    return res
                index += 1
        return decorator()
    return retry


# 类装饰器
class DecoratorAsClass(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kw):
        result = self.function(*args, **kw)
        return result
