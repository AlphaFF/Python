#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-15 20:48:22
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-15 22:13:28


import asyncio
import logging
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import aiohttp


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# async def execute(x):
#     logging.info('Number of %s', x)
#     return x * x

# # 通过loop创建task
# # loop = asyncio.get_event_loop()
# # tasks = [loop.create_task(execute(_)) for _ in range(10)]
# # for task in tasks:
# #     logger.info(task)
# # loop.run_until_complete(asyncio.wait(tasks))
# # for task in tasks:
# #     logger.info(task)
# #     logger.info(task.result())
# # loop.close()
# # logger.info('loog closed...')


# # 通过asyncio创建task
# tasks = [asyncio.ensure_future(execute(_)) for _ in range(5)]
# for task in tasks:
#     logger.info(task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# for task in tasks:
#     logger.info(task)
# loop.close()

# 并发哪家强
# requests + ThreadPoolExecutor

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'


def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']


# t0 = time.time()

# with ThreadPoolExecutor(max_workers=3) as executor:
#     for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
#         logger.info('fetch(%s) = %s', num, result)
# t1 = time.time()
# logger.info('requests + ThreadPoolExecutor cost: %s', t1 - t0)

"""
INFO:__main__:requests + ThreadPoolExecutor cost: 2.4631810188293457
"""

# asyncio + requests + ThreadPoolExecutor

# async def run_scraper_tasks(executor):
#     loop = asyncio.get_event_loop()

#     blocking_tasks = []
#     for num in NUMBERS:
#         task = loop.run_in_executor(executor, fetch, num)
#         task.__num = num
#         blocking_tasks.append(task)

#     completed, pending = await asyncio.wait(blocking_tasks)
#     results = {t.__num: t.result() for t in completed}
#     for num, result in sorted(results.items(), key=lambda x: x[0]):
#         logger.info('fetch(%s) = %s', num, result)


# t0 = time.time()
# executor = ThreadPoolExecutor(3)
# event_loop = asyncio.get_event_loop()
# event_loop.run_until_complete(run_scraper_tasks(executor))
# t1 = time.time()
# logger.info('asyncio + requests + ThreadPoolExecutor cost: %s', t1 - t0)

"""
INFO:__main__:asyncio + requests + ThreadPoolExecutor cost: 3.689368963241577
"""

# asyncio + aiohttp


async def fetch_async(session, a):
    async with session.get(URL.format(a)) as r:
        res = await r.json()
        return res['args']['a']


async def main():
    async with aiohttp.ClientSession() as session:
        for num in NUMBERS:
            res_a = await fetch_async(session, num)
            logger.info('a is %s and res is %s ', num, res_a)


t0 = time.time()
loop = asyncio.get_event_loop()
# tasks = [fetch_async(session, num) for num in NUMBERS]
# results = loop.run_until_complete(asyncio.gather(*tasks))
loop.run_until_complete(main())
loop.close()

# for num, result in zip(NUMBERS, results):
#     logger.info('fetch(%s) = %s', num, result)

t1 = time.time()
logger.info('asyncio + aiohttp cost: %s', t1 - t0)
