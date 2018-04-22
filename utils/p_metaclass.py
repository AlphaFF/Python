#!/usr/bin/env python3
# coding=utf-8

# class ListMetaClass(type):
#     def __new__(cls, *args, **kwargs):
#         return type.__new__(cls, *args, **kwargs)
#         pass


class ListMetaClass(type):  # 元类继承type,元类控制类的创建行为
    """
    :cls 当前准备创建的类的对象
    :name 类的名字
    :类继承的父类对象
    :类的方法集合
    """

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


l = MyList()
l.add(1)
print(l)


class Person:
    """silly person"""

    def __new__(cls, *args, **kwargs):  # python3的new模块已经移除
        print('__new__ called.')
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':
    p = Person('zhangsan',23)
    print(p)


