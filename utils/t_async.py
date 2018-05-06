#!/usr/bin/python3
# coding:utf-8

# import requests
# from multiprocessing import Pool, Queue
# from bs4 import BeautifulSoup
# import asyncio
# import time

# # 使用协程异步爬取了糗事百科的热门笑话里的所有笑话内容

# urls = ['http://www.qiushibaike.com/8hr/page/{}'.format(str(i)) for i in range(1, 36)]


# # for url in urls:
# # 	print(url)

# # 这个多进程会出问题，进程间没有通信，会造成紊乱,暂时不能解决
# # def fun(url):
# # 	num = url.split('/')[-1]
# # 	print('将要爬取第%s页'% num)
# # 	headers = {
# # 		'Referer':'http://www.qiushibaike.com/',
# # 		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
# # 	}
# # 	resp = requests.get(url,headers=headers)
# # 	soup = BeautifulSoup(resp.text,'lxml')
# # 	results = soup.find_all('div',{'class':'content'})
# # 	print('将要打印第%s页的所有笑话'%num)
# # 	for result in results:
# # 		content = result.get_text()
# # 		print(resp.url,content)
# # 	time.sleep(4)

# # p = Pool(3)
# # for url in urls:
# # 	p.apply_async(fun,args=(url,))
# # p.close()
# # p.join()


# # 实现了异步爬取的功能
# async def fun(url):
#     headers = {
#         'Referer': 'http://www.qiushibaike.com/',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
#     }
#     num = url.split('/')[-1]
#     print('即将爬取第%s页' % num)
#     await asyncio.sleep(3)
#     resp = requests.get(url, headers=headers)
#     soup = BeautifulSoup(resp.text, 'lxml')
#     results = soup.find_all('div', {'class': 'content'})
#     print('将要打印第%s页的所有笑话' % num)
#     time.sleep(3)
#     for result in results:
#         content = result.get_text()
#         print(content)


# loop = asyncio.get_event_loop()
# tasks = [fun(url) for url in urls]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# from concurrent.futures import ThreadPoolExecutor

# # 使用进程池,executor传入一个方法名和一个可迭代对象,是传入的参数
# s = []


# def func():
#     return s


# with ThreadPoolExecutor(max_workers=10) as executor:
#     executor.map(func, s)


# no async
# import time 


# def job(t):
#     print('start job', t)
#     time.sleep(t)
#     print('job {} takes {}s'.format(t, t))


# def main():
#     [job(i) for i in range(1, 3)]


# t1 = time.time()
# main()
# print('no async total time: {}'.format(time.time() - t1))

"""
start job 1
job 1 takes 1s
start job 2
job 2 takes 2s
no async total time: 3.0078461170196533
"""


# asyncio
# import asyncio
# import time


# async def job(t):
#     print('start job {}'.format(t))
#     await asyncio.sleep(t)
#     print('job {} takes {} s'.format(t, t))


# async def main(loop):
#     tasks = [loop.create_task(job(t)) for t in range(1,3)]  # 创建任务,但是不执行
#     await asyncio.wait(tasks)  # 执行并等待所有任务完成


# t1 = time.time() 
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(loop))
# loop.close()
# print('async total time: {}'.format(time.time() - t1))
"""
start job 1
start job 2
job 1 takes 1 s
job 2 takes 2 s
async total time: 2.0025479793548584
"""


# requests
# import time
# import requests


# URL = 'https://morvanzhou.github.io/'


# def normal():
#     for i in range(3):
#         r = requests.get(URL)
#         print(r.url)


# t1 = time.time()
# normal()
# print('requests needs time: {}'.format(time.time() - t1))
"""
https://morvanzhou.github.io/
https://morvanzhou.github.io/
https://morvanzhou.github.io/
requests needs time: 1.3428850173950195
"""


import time
import asyncio
import aiohttp


URL = 'https://www.baidu.com'


async def job(session):
    res = await session.get(URL)  # 等待并切换
    return str(res.url), res.status

"""
我们可以在 job() 中 return 个结果出来, 然后再在 finished, unfinished = await asyncio.wait(tasks) 收集完成的结果, 
这里它会返回完成的和没完成的, 我们关心的都是完成的, 而且 await 也确实是等待都完成了才返回. 真正的结果被存放在了 result() 里面
"""
async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        finished, _ = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]  # 获取所有的结果 
        print(all_results)
        

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
# asyncio.ensure_future(main(loop))
loop.close()
print('async total time:{}'.format(time.time() - t1))







