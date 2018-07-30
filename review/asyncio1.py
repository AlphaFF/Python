# -*- coding: utf-8 -*-
# __author__: AlphaFF

import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def execute(x):
    logger.info('Number %d', x)
    return x

coroutine = execute(1)  # 协程对象
# 一种封装为task的方法
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)  # 封装为task对象
# logger.info('Task: %s', task)
# loop.run_until_complete(task)
# logger.info('Task: %s', task)
# logger.info('After calling loop.')
# loop.close()

# 另外一种封装为task的方法
# task = asyncio.ensure_future(coroutine)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# loop.close()


# 绑定回调
def callback(task):
    logger.info('Result: %s', task.result())


tasks = [asyncio.ensure_future(execute(_)) for _ in range(5)]
# task.add_done_callback(callback)  # 跟直接调用task.result()一样
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    logger.info('Task Result: %s', task.result())
