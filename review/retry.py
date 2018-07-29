#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
