#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-10 10:38:40
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-10 11:00:12

from datetime import timedelta

# 使用Redis作为消息代理
BROKER_URL = 'redis://localhost:6379/0'
# 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
# 任务序列化和反序列化使用JSON方案
CELERY_TASK_SERIALIZER = 'json'
# 读取任务结果使用JSON
CELERY_RESULT_SERIALIZER = 'json'
# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 指定接受的内容类型，是个数组，可以写多个
CELERY_ACCEPT_CONTENT = ['json']

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    }
}
