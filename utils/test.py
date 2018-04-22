#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 异步协程review
# import asyncio

# async def task(n):
# 	print(n)
# 	await asyncio.sleep(3)
# 	print(n*n)

# loop = asyncio.get_event_loop()
# tasks = [task(i) for i in range(10)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 数据库连接review
# import mysql.connector

# conn = mysql.connector.connect(host='127.0.0.1',user='root',password='',database='test')
# cursor = conn.cursor()


# # # sql1 = 'select * from test1 '
# # # sql2 ='insert into test1 (id,name) values(%d,%s)'
# # # cursor.execute('insert into test2 (id,name,age,class) values(%s,%s,%s,%s)',('6','alpha',30,4))
# # cursor.execute('insert into test1 (id,name) values(%s,%s)',(5,'alphafeng'))
# # conn.commit()
#
# # cursor.execute('select * from test1 ')
# # values = cursor.fetchall()
# # print(values)
#
# # cursor.close()
# # conn.close()
#
# # 图片处理
#
# # from PIL import Image
# #
# # im = Image.open('/Users/alpha/Desktop/logo.png')
# # w,h = im.size
# # print(w,h)
# #
# # im.thumbnail((w//2,h//2))
# # im.save('thumbnail.jpg','jpeg')
#
# # from selenium import webdriver
# # #
# # # url = 'http://www.mtime.com/'
# # # driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
# # # driver.execute_script()
# # driver = webdriver.Chrome()
# # driver.get('http://www.baidu.com')
# # print(driver.page_source)
#
# # import mysql.connector
# #
# # conn = mysql.connector.connect(user='root',password='',database='test')
# # cursor = conn.cursor()
# #
# # # cursor.execute('insert ignore into test1 (id,name) values(%s,%s)',(7,'哈哈'))
# #
# # sql = 'insert into test3 (name,age) values(%s,%s)'
# # cursor.execute(sql,('haha',15))
# #
# # cursor.execute('select * from test3')
# # values = cursor.fetchall()
# # print(values)
# #
# # conn.commit()
# # cursor.close()
# # conn.close()
#
# # import pymysql
# #
# # conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='test')
# # cursor = conn.cursor()
# #
# # cursor.execute('insert into test3 (name,age) values(%s,%s)',('haha1',30))
# #
# # conn.commit()
# # cursor.close()
# # conn.close()
#
# # 可变参数,会把参数组成一个tuple
# # def f(*x):
# #     print(x)
# # f(1,2,'num')
#
# # 关键字参数，会把参数组成一个dict
# # def g(name,age,**kw):
# #     print('name: %s age: %s other:%s'%(name,age,kw))
# #
# # g('haha',40,city='hangzhou')
#
# # def person(name,age,*,city,job):
# # 	print(name,age,city,job)
#
# # # person('wang',20,city='zhejiang',job='worker')
# # person('wang',24,'zhejiang','worker')
# # def person(name,age,*arg,**kw):
# # 	print(name,age,arg,kw)
#
# # person('wang',25,172,45,63,city='hangzhou',job='major')
# # 对于任意的函数都可以通过类似的形式调动它
# # def func(*arg,**kw):
# # 	pass
#
# # 递归函数
# # def fact(n):
# # 	if n == 1:
# # 		return 1
# # 	return n*fact(n-1)
#
# # 尾递归，即返回的是函数本身，不带函数表达式
# # def fact(m,n):
# # 	if m == 1:
# # 		return n
# # 	return fact(m-1,m*n)
#
# # map的用法,传入2个,Iterator是惰性序列，因此通过list,可以把整个序列都计算出来并返回一个list
# # f = map(lambda x:x*x,[1,2,3,4])
# # print(list(f))
#
# # reduce,必须接受2个参数，然后把结果作用于下一个元素，做累计运算
# # from functools import reduce
# # f = reduce(lambda x,y:x*10+y,[1])
# # print(f)
#
# # import json
# # from flask import Flask, jsonify,render_template
# # from flask_sqlalchemy import SQLAlchemy
# # import requests
# # from flask_cors import *
# # import logging
# #
# # app = Flask(__name__)
# # CORS(app, supports_credentials=True)
# #
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/test'
# # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #
# # db = SQLAlchemy(app)
# #
# #
# # class Book(db.Model):
# #     __tablename__ = 'test_books'
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(255))
# #     author = db.Column(db.String(255))
# #     category = db.Column(db.String(255))
# #     status = db.Column(db.String(255))
# #     count_num = db.Column(db.String(255))
# #     address_url = db.Column(db.String(255))
# #     chapters = db.relationship('Chapter', backref='bookname')
# #
# #     def __repr__(self):
# #         return self.name
# #
# #     def to_json(self):
# #         json_book = {
# #             'id': self.id,
# #             'name': self.name,
# #             'author': self.author,
# #             'category': self.category,
# #         }
# #         return json_book
# #
# #
# # class Chapter(db.Model):
# #     __tablename__ = 'test_chapters'
# #     id = db.Column(db.Integer, primary_key=True)
# #     num = db.Column(db.String(255))
# #     title = db.Column(db.String(255))
# #     content = db.Column(db.String(255))
# #     book = db.Column(db.Integer, db.ForeignKey('test_books.id'))
# #
# #     def __repr__(self):
# #         return self.content
# #
# #     def to_json(self):
# #         json_chapter = {
# #             'id': self.id,
# #             'num': self.num,
# #             'title': str(self.title),
# #             'content': str(self.content),
# #             'book': self.book,
# #         }
# #         return json_chapter
# #
# #
# # @app.route('/')
# # def index():
# #     return render_template('index.html')
# #
# #
# # @app.route('/api/books/')
# # def get():
# #     books = Book.query.all()
# #     return jsonify({'books': [book.to_json() for book in books]})
# #
# #
# # @app.route('/api/books/<int:book_id>')
# # def get_chapters(book_id):
# #     # chapters = Chapter.query.filter_by(book_id=id).all()
# #     # return jsonify({'chapters':[chapter.to_json() for chapter in chapters]})
# #     book = Book.query.filter_by(id=book_id).first()
# #     chapters = book.chapters
# #     logging.warning(type(chapters))
# #     # for chapter in chapters:
# #     #     logging.warning(chapter.to_json())
# #     # return jsonify({'chapters':[chapter.to_json() for chapter in chapters]})
# #     return jsonify({'chapters': [chapter.to_json() for chapter in chapters], 'book': book.name, 'author': book.author})
# #
# #
# # @app.route('/api/books/<int:book_id>/chapters/<int:chapter_id>')
# # def get_chapter(book_id, chapter_id):
# #     chapter = Chapter.query.filter_by(book=book_id, num=chapter_id).first()
# #     return json.loads(json.dumps(chapter))
# #
# #
# # if __name__ == '__main__':
# #     app.run(debug=True, port=5656)
#
#
# # import requests
# # url = 'https://jc.yscredit.com/query/queryResultList?range=all&keyword=%E6%9D%AD%E5%B7%9E%E6%9C%89%E6%95%B0'
#
# # !/usr/bin/env python
# # encoding: utf-8
#
# # from selenium import webdriver
# # from time import sleep
#
# # # global driver
#
# # driver = webdriver.Chrome()
# # driver.get("https://jc.yscredit.com/")
# # # driver.get("http://jc.cchcredit.com/")
# # elem = driver.find_element_by_xpath('//*[@class="toggle-btn-box"]/div[2]').click()
# # driver.find_element_by_id('username').clear()
# # driver.find_element_by_id("username").send_keys("xieyk")
# # driver.find_element_by_id('password').clear()
# # driver.find_element_by_id("password").send_keys("xyk1234")
# # driver.find_element_by_id("login_btn").click()
# # print("登录成功")
# # sleep(2)
#
# # driver.find_element_by_id('queryInput').clear()
# # driver.find_element_by_id('queryInput').send_keys('杭州有数')
# # driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/button').click()
# # print("返回搜索结果")
# # sleep(5)
#
# # total = driver.find_element_by_xpath('//div[@class="result-num rel"]/span[1]/span[1]').text
# # print(total)
#
# # def get_ent_names(query_ent,isContinue,page,driver):
# #     titles = driver.find_elements_by_xpath("//div[@class='result-list ng-scope']")
# #     print(page)
#
# #     for ent in titles:
# #         ele = ent.find_element_by_xpath('./div[1]/span[2]/div[1]/span[1]')
# #         ent_name = ele.text
# #         print(ent_name)
# #         if ent_name == query_ent:
# #             isContinue = False
# #             print('已经找到了企业,不用再找了...')
# #             ele.click()
# #             sleep(5)
# #             return isContinue
# #     # sleep(5)
# #     driver.find_element_by_xpath("//a[@class='nextPage']").click()
# #     sleep(10)
# #     return isContinue
#
# # pages = int(total) // 10 if int(total) % 10 == 0 else int(total) // 10 + 1
# # print(pages)
#
# # page = 1
# # isContinue = True
# # query_ent = '杭州星数科技有限公司'
#
# # while page <= pages and isContinue:
# #     isContinue= get_ent_names(query_ent,isContinue,page,driver)
# #     page += 1
#
#
# # if __name__ == '__main__':
# #     get_ent_names()
#
# # import os
#
# # base_dir = os.path.abspath(os.path.dirname(__file__))
# # print(base_dir)
# # file_dir = os.path.join(base_dir,'ids.txt')
#
# # # with open(file_dir,'w') as f:
# # # 	for i in range(3):
# # # 		f.write(str(i)+' '+'1' + '\n')
#
# # with open(file_dir,'r') as f:
# # 	for line in f.readlines():
# # 		num,status = line.strip().split()
# # 		print(num,status)
#
#
# # import re
# # import logging
# # from datetime import datetime
# #
# # def get_court_date(court_time):
# #     if not court_time:
# #         return court_time
# #     court_date = re.findall(r'(.{4}[-年].{1,2}[-月].{1,2}?)[号日\s]{0,1}', court_time)[0] if re.findall(r'(.{4}[-年].{1,2}[-月].{1,2}?)[号日\s]{0,1}', court_time) else ''
# #     logging.warning(court_date)
# #     special_str = '〇一二三四五六七八九十'
# #     pos = 0
# #     while 1 and pos < len(court_date):
# #         if court_date[pos] in special_str:
# #             print(court_date)
# #             return court_date
# #         else:
# #             pos += 1
# #     if '-' in court_date:
# #         court_date = datetime.strptime(
# #             court_date, "%Y-%m-%d").strftime('%Y-%m-%dT00:00:00+08:00')
# #     else:
# #         court_date = datetime.strptime(
# #             court_date, "%Y年%m月%d").strftime('%Y-%m-%dT00:00:00+08:00')
# #     return court_date
# #
# # s = '2〇一0年一月1日上午8:40'
# # t = get_court_date(s)
# # print(t)
#
# # import redis
# # from hashlib import md5
#
# # class SimpleHash:
# #     def __init__(self,cap,seed):
# #         self.cap = cap
# #         self.seed = seed
#
# #     def hash(self,value):
# #         ret = 0
# #         for i in range(len(value)):
# #             ret += self.seed + ret + ord(value[i])
# #         return (self.cap - 1) & ret
#
# # class BloomFilter:
# #     def __init__(self,host='localhost',port=6379,db=0,blockNum=1,key='bloomFilter'):
# #         self.server = redis.Redis(host=host,port=port,db=db)
# #         self.bit_size = 1 << 31
# #         self.seeds = [5,7,11,13,31,37,61]
# #         self.key = key
# #         self.blockNum = blockNum
# #         self.hashfunc = []
# #         for seed in self.seeds:
# #             self.hashfunc.append(SimpleHash(self.bit_size,seed))
#
# #     def isContains(self,string):
# #         if not string:
# #             return False
# #         m5 = md5()
# #         m5.update(string.encode('utf8'))
# #         string = m5.hexdigest()
# #         ret = True
# #         name = self.key + str(int(string[0:2],16)%self.blockNum)
# #         for f in self.hashfunc:
# #             loc = f.hash(string)
# #             ret = ret & self.server.getbit(name,loc)
# #         return ret
#
# #     def insert(self,string):
# #         m5 = md5()
# #         m5.update(string.encode('utf8'))
# #         string = m5.hexdigest()
# #         name = self.key + str(int(string[0:2],16)%self.blockNum)
# #         for f in self.hashfunc:
# #             loc = f.hash(string)
# #             self.server.setbit(name,loc,1)
#
# # if __name__ == '__main__':
# #     from pybloomfilter import BloomFilter
#
# #     bf = BloomFilter(10000000, 0.01, 'filter.bloom')
# #     bf = BloomFilter()
# #     if bf.isContains('http://www.baidu.com'):
# #         print('exists')
# #     else:
# #         print('not exists')
# #         bf.insert('http://www.baidu.com')
#
# import re
# from datetime import datetime
#
# s = '二○一七年十一月二十日'
#
# def parse_time(self,t):
#     t = list(t)
#     d = {
#         '零': '0',
#         '一': '1',
#         '二': '2',
#         '三': '3',
#         '四': '4',
#         '五': '5',
#         '六': '6',
#         '七': '7',
#         '八': '8',
#         '九': '9',
#         '○': '0',
#         '年': '-',
#         '月': '-',
#         '日': '-',
#         '元': '1'
#     }
#     for i in range(len(t)):
#         if t[i] in d.keys():
#             t[i] = d[t[i]]
#     # 处理汉字为十的情况
#     if '十' in t:
#         for i in range(len(t)):
#             if t[i] == '十':
#                 if (i - 1) >= 0 and t[i - 1].isalnum():
#                     t[i] = '0'
#                 if (i + 1) < len(t) and t[i + 1].isalnum():
#                     t[i] = '1'
#                 if (i - 1) >= 0 and (i + 1) < len(t) and t[i - 1] == '-' and t[i + 1] == '-':
#                     t[i] = '10'
#     t = ''.join(t)
#     t = re.findall(r'(.{4}[-年\.].{1,2}[-月\.].{1,3}?)[-上下日号\s]', t)[0]
#     t = datetime.strptime(t, "%Y-%m-%d").strftime('%Y-%m-%dT00:00:00+08:00')
#     return t
#
# t = parse_time(s)
# print(t)
#
# import redis
#
# class RedisClient(object):
#     # 数据库的连接
#     def __init__(self, name, host, port):
#         self.name = name
#         self.__conn = redis.Redis(host=host, port=port, db=0)
#
#     def push(self,name,values):
#         self.__conn.lpush(self,self.name,values)

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
from functools import reduce

# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     tmp = list(nums)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, '0.0')

# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))


# def outer():
#     num = 10
#     def inner():
#         # nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)

# outer()

for i in range(2, 101):
    fg = 0
    for j in range(2, i-1):
        if i % j == 0:
            fg = 1
            break
    if fg == 0:
        print(i)

import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

# if __name__ == '__main__':
unittest.main()


