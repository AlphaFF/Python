#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2019-04-10 16:15:40
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2019-04-12 17:26:56

"""
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例
u = User(id=1, name='john', email='test@google.com', password='123')

# 保存到数据库
u.save()
"""

from collections import abc


class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntergerField(Field):
    def __init__(self, name):
        super(IntergerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('found Model: ', name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('found mappings:', k, v)
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings


# 使list有add方法
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

    def __repr__(self):
        return 'hahaha'

    def __str__(self):
        return 'wahahah'


a = MyList()
print(a)
a.append('a')
print(a)
a.add('b')
print(a)


d = {
    'name': 'zs'
}

# print(d.name)


class FrozenJson:
    """一个只读接口,使用属性表示访问JSON类对象
    """

    def __init__(self, mapping):
        self._data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            return FrozenJson.build(self._data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


print(dict(d))

b = FrozenJson(d)
print(b.name)
b.name = 'lisi'
print(b._data, d)


class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            self._weight = value
        else:
            raise ValueError('value must be > 0')


class Test:
    data = 'abc'

    @property
    def prop(self):
        return 'the prop value'


obj = Test()
print(vars(obj))
print(obj.__dict__)

print(obj.data)
print(obj.prop)
obj.data = 'abcd'
print(obj.data, Test.data)
# obj.prop = 'hahaha'
obj.__dict__['prop'] = 'hahahaha'
print(vars(obj))
print(obj.data, obj.prop, Test.prop)
