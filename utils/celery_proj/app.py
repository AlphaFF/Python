#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-10 10:38:54
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-10 10:51:48

# from __future__ import absolute_import
from celery import Celery

app = Celery(__name__, include=['tasks'])
app.config_from_object('config')


if __name__ == '__main__':
    app.start()
