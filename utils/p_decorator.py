"""装饰器的使用."""

import time
import functools

# def deco(func):
# 	def inner():
# 		print('running inner()')
# 	return inner


# @deco
# def target():
# 	print('running target()')


# target()
# print(target)


# registry = []


# def register(func):
# 	print('running register(%s)' % func)
# 	registry.append(func)
# 	return func


# @register
# def f1():
# 	print('running f1() ')


# @register
# def f2():
# 	print('running f2() ')


# def f3():
# 	print('running f3() ')


# def main():
# 	print('running main()')
# 	print('registry ->', registry)
# 	f1()
# 	f2()
# 	f3()


# if __name__ == '__main__':
# 	main()

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount


promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """为积分为1000或以上的顾客提供5%的折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """单个商品为20个或以上时提供10%的折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%的折扣"""
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """选择最佳的可用折扣"""
    return max(promo(order) for promo in promos)


class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()  # Averager的实例是可调用对象,既可以当做函数来使用
print(avg(10))
print(avg(11))
print(avg(12))


def make_averager():  # 高阶函数的实现
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)


def make_averager1():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager1()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)


# 实现一个简单的装饰器


def clock(func):
    """不支持关键字参数,而且遮盖了被装饰函数的 __name__ 和 __doc__ 属 性。"""

    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


def clock1(func):
    """支持关键字参数,而且遮盖了被装饰函数的 __name__ 和 __doc__ 属 性。"""

    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s-%r' % (k, w) for k, w in sorted(kwargs.items)]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@functools.lru_cache()
@clock
def fibonacii(n):
    if n < 2:
        return n
    return fibonacii(n - 2) + fibonacii(n - 1)


if __name__ == '__main__':
    # print('*' * 40, 'calling snooze(.123)')
    # print(snooze)
    # snooze(.123)
    # print('*' * 40, 'calling factorial(6)')
    # factorial(6)
    fibonacii(6)
