#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging


# type type是创建所有类的元类,type是Python中使用的内建元类，其实它也允许我们建立自己的元类
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def foo(self):
    return 'foo'


name = 'zhangsan'

B = type('Hello', (object,), {'name': name, 'foo': foo})
logger.info(B.name)
logger.info(B().foo())


# metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, vaule: self.append(vaule)
        return super(ListMetaclass, cls).__new__(cls, name, bases, attrs)


# python3中已经没有__metaclass__属性了
class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
l.add(2)
logger.info(l)