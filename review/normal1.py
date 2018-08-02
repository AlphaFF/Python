#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__: AlphaFF

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 迭代器
class CountDown(object):
    """create a iterator class"""

    def __init__(self, step):
        self.step = step

    def __next__(self):
        """return the next element"""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """return the iterator itself"""
        return self


# for element in CountDown(4):
#     logger.info(element)


def test_send():
    """test generator send function"""

    logger.info('start test...')
    s = yield
    if s is not None:
        if s % 2 == 0:
            s += 2
        else:
            s += 1
        logger.info(s)


# 子类化内置类型
class DistinctError(ValueError):
    pass


class DistinctDict(dict):
    def __setitem__(self, key, value):
        if value in self.values():
            if (key in self and self[key] == value) or key not in self:
                raise DistinctError('This value already exists for different key')
        super(DistinctDict, self).__setitem__(key, value)


# 描述符
class RevealAccess:
    """一个数据描述符, 正常设定值并返回值, 同时打印出记录访问的信息
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        logger.info('Retrieving %s', self.name)
        return self.val

    def __set__(self, obj, val):
        logger.info('Updating %s', self.name)
        self.val = val


class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 5


# property
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        return self.x2 - self.x1

    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value


# 槽
class Frozen:
    __slots__ = ['ice', 'cream']


if __name__ == '__main__':
    # import tokenize
    # reader = open('copy1.py').readline
    # tokens = tokenize.generate_tokens(reader)
    # logger.info(next(tokens).string)
    # logger.info(type(tokens))
    # for i, token in enumerate(tokens):
    #     logger.info('%d is %s', i, token.string)

    # 迭代器
    # t = test_send()
    # next(t)
    # t.send(1)
    # t.send(2)
    # t.send(3)
    # t.send(4)

    # 子类化内置类型
    # my_dict = DistinctDict()
    # my_dict['key'] = 'value'
    # my_dict['other_key'] = 'value'

    # 描述符
    # m = MyClass()
    # logger.info(m.x)
    # m.x = 20
    # logger.info(m.x)

    # 槽
    frozen = Frozen()
    logger.info('__dict__' in dir(Frozen))
    logger.info('ice' in dir(Frozen))
    frozen.cream = None
    frozen.icy = None
