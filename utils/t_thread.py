#!/usr/bin/env python3
#coding:utf-8

from threading import Thread
import time
import asyncio


async def _sum(x,y):
	print('compute {}+{}...'.format(x,y))
	await asyncio.sleep(2)
	return x+y

async def compute_sum(x,y):
	result = await _sum(x,y)
	print('{}+{}={}'.format(x,y,result))

# start = time.time()
# theads = [
# 		  Thread(target=compute_sum,args=(0,0)),
# 		  Thread(target=compute_sum,args=(1,1)),
# 		  Thread(target=compute_sum,args=(2,2)),
# 		 ]
# for t in theads:
# 	t.start()
# for t in theads:
# 	t.join()

# print('total elapsed time {} s'.format(time.time()-start))

#使用协程
# start = time.time()
# loop = asyncio.get_event_loop()
# tasks = [
# 	compute_sum(0,0),
# 	compute_sum(1,1),
# 	compute_sum(2,2),
# 	]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# print('total elasped time {}'.format(time.time()-start))




#do not use thread
# start = time.time()
# compute_sum(0,0)
# compute_sum(1,1)
# compute_sum(2,2)
# print('total elapsed time {} s'.format(time.time()-start))


#爬取了天猫某个商品的评论(南极人保暖内衣)
import requests
import re


# urls = ['https://rate.tmall.com/list_detail_rate.htm?itemId=521136254098&spuId=345965243&sellerId=2106525799&order=1&currentPage={}'.format(str(i)) for i in range(1,maxnum)]

# headers = {
# 	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
# }

# # json_dump = json.dumps(resp.text)
# # json_load = eval(resp.text)
# # results = json_load['rateList']
# # for result in results:
# # 	comment = result['rateContent']
# # 	print(comment)
# # print(resp.text)
# # soup = BeautifulSoup(resp.text,'lxml')
# for url in urls:
# 	resp = requests.get(url,headers=headers)
# 	results = re.findall(re.compile(r'"rateContent":"(.*?)","rateDate"'),resp.text)
# 	for result in results:
# 		print(result)


