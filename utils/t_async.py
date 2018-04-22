#!/usr/bin/python3
# coding:utf-8

import requests
from multiprocessing import Pool, Queue
from bs4 import BeautifulSoup
import asyncio
import time

# 使用协程异步爬取了糗事百科的热门笑话里的所有笑话内容

urls = ['http://www.qiushibaike.com/8hr/page/{}'.format(str(i)) for i in range(1, 36)]


# for url in urls:
# 	print(url)

# 这个多进程会出问题，进程间没有通信，会造成紊乱,暂时不能解决
# def fun(url):
# 	num = url.split('/')[-1]
# 	print('将要爬取第%s页'% num)
# 	headers = {
# 		'Referer':'http://www.qiushibaike.com/',
# 		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
# 	}
# 	resp = requests.get(url,headers=headers)
# 	soup = BeautifulSoup(resp.text,'lxml')
# 	results = soup.find_all('div',{'class':'content'})
# 	print('将要打印第%s页的所有笑话'%num)
# 	for result in results:
# 		content = result.get_text()
# 		print(resp.url,content)
# 	time.sleep(4)

# p = Pool(3)
# for url in urls:
# 	p.apply_async(fun,args=(url,))
# p.close()
# p.join()


# 实现了异步爬取的功能
async def fun(url):
    headers = {
        'Referer': 'http://www.qiushibaike.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
    num = url.split('/')[-1]
    print('即将爬取第%s页' % num)
    await asyncio.sleep(3)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    results = soup.find_all('div', {'class': 'content'})
    print('将要打印第%s页的所有笑话' % num)
    time.sleep(3)
    for result in results:
        content = result.get_text()
        print(content)


loop = asyncio.get_event_loop()
tasks = [fun(url) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

from concurrent.futures import ThreadPoolExecutor

# 使用进程池,executor传入一个方法名和一个可迭代对象,是传入的参数
s = []


def func():
    return s


with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(func, s)
