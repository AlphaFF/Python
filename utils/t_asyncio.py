# !/usr/bin/env python
# coding:utf-8

import aiohttp
import asyncio
import async_timeout

# async def fetch(session, url):
#     with async_timeout.timeout(10):
#         async with session.get(url) as response:
#             return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, 'http://www.baidu.com')
#         print(html)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# # 处理http请求的
# async def fetch(session, url):
#     with async_timeout.timeout(10):
#         async with session.get(url) as response:
#             return await response.text()

# # 处理请求后的结果的
# async def main(url):
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, url)
#         print(html)

# urls = ['http://www.baidu.com','http://qiushibaike.com','http://www.zhihu.com']
# tasks = [main(url) for url in urls]

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

import asyncio
import requests
import time


async def download(url): # 通过async def定义的函数是原生的协程对象
    print("get %s" % url)    
    response = requests.get(url)
    print(response.status_code)
    return response.text


async def wait_download(url):
    html = await download(url) # 这里download(url)就是一个原生的协程对象
    print("get {} data complete.".format(url))
    print(html)
    return html



async def main():
    start = time.time()
    await asyncio.wait([
        wait_download("http://www.163.com"),
        wait_download("http://www.mi.com"),
        wait_download("http://www.baidu.com"),
    	# download("http://www.163.com"),
     #    download("http://www.mi.com"),
     #    download("http://www.baidu.com")
     ])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())



