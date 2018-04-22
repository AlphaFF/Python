#! /usr/bin/env python3
# coding:utf-8

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except Exception as e:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


def test():
    return 'test'


def deco(func):
    def inner():
        print('running inner()')
        return func()

    return inner


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


@deco
def target():
    print('running target()')


import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)->%r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


# from queue import Queue

# q = Queue()
# q.put(1)
# q.put((2,3))
# q.put((4,5,6))

# print(q.get())
# print(q.qsize())
# print(q.get())
# print(q.qsize())
# print(q.get())
# print(q.qsize())

class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # self.passengers = list(passengers)
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# baskeball_team = ['sue', 'tina', 'maya', 'diana', 'pat']
# bus = TwilightBus(baskeball_team)
# bus.drop('tina')
# bus.drop('pat')
# print(baskeball_team)
# print(id(baskeball_team))
# print(id(bus.passengers))

# 符合python风格的对象
from array import array
import math


class Vector2d:
	# 告诉解释器:这个类中的所有实例属性都在这了
	# 使用类似元祖的结构存储实例变量,从而避免使用消耗内存的__dict__属性
	__slots__ = ('__x','__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
    	return self.__x

    @property
    def y(self):
    	return self.__y

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    # 这个还不太懂
    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
    	return math.atan2(self.y,self.x)

    def __format__(self,fmt_spec=''):
    	if fmt_spec.endswith('p'):
    		fmt_spec = fmt_spec[:-1]
    		coords = (abs(self),self.angle())
    		outer_fmt = '<{}, {}>'
    	else:
    		coords = self
    		outer_fmt = '({}, {})'
    	components = (format(c,fmt_spec) for c in coords)

    	return outer_fmt.format(*components)

   	# 让对象可散列,使用异或
    def __hash__(self):
    	return hash(self.x)^hash(self.y)

class Vector:
	typecode = 'd'

	def __init__(self,components):
		self._components = array(self.typecode,components)

	def __iter__(self):
		return iter(self._components)


	def __repr__(self):
		components = reprlib.repr(self._components)
		components = components[components.find('['):-1]
		return 'Vector({})'.format(components)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (bytes(ord(self.typecode))) + bytes(self._components)

	def __eq__(self,other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))

	def __bool__(self):
		return bool(abs(self))

	@classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self,index):
        cls = type(self)
        if isinstance(index,slice):
            return cls(self._components[index])
        elif isinstance(index,numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'
    def __getattr__(self,name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{cls.__name__ !r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls,name))        





# v1 = Vector2d(3, 4)
# print(v1)
# print(abs(v1))
# print(v1.__abs__())
# print(v1.angle())

# print(v1.__dict__)




# if __name__ == '__main__':
# bingo = BingoCage('abc')
# bingo()
# print(bingo._items)
# print(globals())
# target()
# print(target)
# avg = make_averager()
# print(avg(10))
# print(avg(11))
# print(avg(12))
# print(factorial.__name__)

def simple_coroutine():
	print('-> coroutine started')
	x = yield
	print('-> coroutine received:',x)

def simple_coro2(a):
	print('-> Started:a = ',a)
	b = yield a
	print('-> received:b = ',b)
	c = yield a+b
	print('-> received:c =',c)


def averager():
	total = 0.0
	count = 0
	averager = None
	while True:
		term = yield averager
		total += term
		count+=1
		averager = total / count

def coroutine(func):
	from functools import wraps
	@wraps(func)
	def primer(*arg,**kwargs):
		gen = func(*arg,**kwargs)
		next(gen)
		return gen
	return primer

@coroutine
def averager1():
	total = 0.0
	count = 0
	averager = None
	while True:
		term = yield averager
		total += term
		count+=1
		averager = total / count

def averager2():
	total = 0.0
	count = 0
	averager = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count+=1
		averager = total / count
	return (count,averager)




