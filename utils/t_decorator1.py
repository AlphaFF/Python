import time 
from functools import wraps


def retries(func):
    @wraps.func
    def wrapper(*arg, **kwargs):
        for i in range(3):
            try:
                return func(*arg, **kwargs)
            except:
                print('重试出错了..')
    return wrapper
