#!/usr/bin python3
# coding:utf-8

from datetime import datetime

# def now():
#     t = datetime.now()
#     return t
#
# f = now
# print(type(f))
# print(f.__name__)

# 在代码运行期间动态增加功能的方式，被称之为装饰器，decorator就是一个返回函数的高阶函数

# 不带参数的装饰器
# def log(func):
#     def wrapper(*arg,**kw):
#         print('call %s'%func.__name__)
#         return func(*arg,**kw)
#     print('-----')
#     return wrapper
#
# @log
# def now():
#     t = datetime.now()
#     print(t)
#
# # now()
#
# a = log(now)
# print(a())

# now()

import functools

def log(func):

    @functools.wraps(func)
    def wrapper(*arg,**kw):
        print('begin call...')
        _func = func(*arg,**kw)
        print('end call')
        return _func
    return wrapper


@log
def test():
    print('hahaha')


test()

# test = log(test)


# 带参数的装饰器
# import functools
#
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*arg, **kw):
#             print('%s %s :' % (text, func.__name__))
#             return func(*arg, **kw)
#
#         return wrapper
#
#     return decorator
#
#
# @log('excute')
# def now():
#     t = datetime.now()
#     print(t)
#
#
# # a = log('execute')(now)
# # print(a)
# # print(a.__name__)
#
# now()
#
#
# # property的使用
# class Student():
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, score):
#         self._score = score
#
#
# s = Student()
# s.score = 90
# print(s.score)

# import requests
# from redis import Redis
# from rq import Queue
#
# def count_words_at_url(url):
#     resp = requests.get(url)
#     return len(resp.text.split())
#
# q = Queue(connection=Redis())
#
# result = q.enqueue(count_words_at_url,'http://nvie.com')


# 伪造user-agent
# from fake_useragent import FakeUserAgent
#
# ua = FakeUserAgent()
# print(ua.random)


##xpath测试

# from lxml import etree
#
# text = '''
# <?xml version="1.0" encoding="ISO-8859-1"?>
#
# <bookstore>
#
# <book category="COOKING">
#   <title lang="en">Everyday Italian</title>
#   <author>Giada De Laurentiis</author>
#   <year>2005</year>
#   <price>30.00</price>
# </book>
#
# <book category="CHILDREN">
#   <title lang="en">Harry Potter</title>
#   <author>J K. Rowling</author>
#   <year>2005</year>
#   <price>29.99</price>
# </book>
#
# <book category="WEB">
#   <title lang="en">XQuery Kick Start</title>
#   <author>James McGovern</author>
#   <author>Per Bothner</author>
#   <author>Kurt Cagle</author>
#   <author>James Linn</author>
#   <author>Vaidyanathan Nagarajan</author>
#   <year>2003</year>
#   <price>49.99</price>
# </book>
#
# <book category="WEB">
#   <title lang="en">Learning XML</title>
#   <author>Erik T. Ray</author>
#   <year>2003</year>
#   <price>39.95</price>
# </book>
#
# </bookstore>
# '''

# html = etree.HTML(text)
# print(html)
# # result = etree.tounicode(html)
# # print(result)
# # print(type(result))
# result1 = html.xpath('//li/a[@href="link1.html"]/@href')
# print(result1)
#
# result2 = html.xpath('//li//span')[0]
# print(result2)
#
# result3 = html.xpath('//li[last()]/a/@href')
# print(result3)
#
# result4 = html.xpath('//*[@class="bold"]')
# print(result4)

# html = etree.HTML(text)
# result = etree.tounicode(html)
# print(result)

# result1 = html.xpath('//bookstore//title')
# print(result1)
#
# result2 = html.xpath('*')
# print(result2)
#
# result3 = html.xpath('//bookstore/book/title | //bookstore/book/price')
# print(result3)
#
# result4 = html.xpath('//bookstore')
# print(result4)

# result1 = html.xpath('//title')
# print(len(result1))
#
#
# result2 = html.xpath('//book[1]/title')
# print(len(result2))
#
#
# result3 = html.xpath('//book/price/text()')
# print(result3)
#
#
# result4 = html.xpath('//book[price>35]/price/text()')
# print(result4)
#
# result5 = html.xpath('//book[price<35]/title/text()')
# print(result5)



































