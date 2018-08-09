#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-09 19:44:54
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-09 19:55:03


from celery import Celery

app = Celery(__name__,
             broker='redis://127.0.0.1:6379',
             backend='redis://127.0.0.1:6379')


@app.task
def add(x, y):
    print('执行一条任务...')
    return x + y
