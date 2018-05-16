import time
import functools
import requests

def retries(func):
    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        for i in range(3):
            try:
                return func(*arg, **kwargs)
            except:
                print('重试出错了..')
    return wrapper


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


# print(target())
# print(target)

registry = []


def register(func):
    print('running registry(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


# if __name__ == '__main__':
#     main()

# 闭包
# 计算移动平均值
class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


# 高阶函数
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager1():
    total = 0
    count = 0

    def averager(new_value):
        nonlocal total, count
        count += 1
        total += new_value
        return total / count

    return averager


# 参数化装饰器
def retry(attempt):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            att = 0
            while att < attempt:
                try:
                    return func(*arg, **kw)
                except Exception as e:
                    att += 1
        return wrapper
    return decorator


@retry(attempt=3)
def get_response(url):
    r = requests.get(url)
    print(r.status_code, r.url)
    return r.status_code


url = 'https://www.baidu.com'
get_response(url)





