#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-08 22:12:35
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-08 22:19:02


class Singleton:
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


a = Singleton()
b = Singleton()

print(a)
print(b)
print(a is b)
