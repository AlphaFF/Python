#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-10 11:09:58
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-10 11:45:47


import requests
from bs4 import BeautifulSoup
import time
from celery import Celery
import redis

host = 'localhost'
port = 6379

pool = redis.ConnectionPool(host=host, port=port, db=0)
r = redis.StrictRedis(connection_pool=pool)
set_key = 'crawl:douban'

app = Celery('crawl', broker='redis://{}:{}/1'.format(host, port), backend='redis://{}:{}/1'.format(host, port))

# 官方推荐使用json作为消息序列化方式
app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
)

headers = {
    'User-Agent': ''
}


@app.task
def crawl(url):
    res = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.select('.subject-list .subject-item .info h2 a')
    titles = [item['title'] for item in items]
    r.sadd(set_key, (url, titles, time.time()))
    print(titles)
    return (url, titles)
