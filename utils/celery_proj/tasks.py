#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-10 10:38:48
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-10 10:53:59

# from __future__ import absolute_import
from app import app


@app.task
def add(x, y):
    print('..计算一次两个值的和...')
    return x + y
