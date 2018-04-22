	#!/usr/bin/env python3
#coding:utf-8

#mysql的简单应用

#导入mysql驱动
import mysql.connector

#1.通过python创建表
#连接mysql
conn = mysql.connector.connect(user='root',password='',database='test')
cursor = conn.cursor()

# #创建表test1
# # cursor.execute('create table test1 (id varchar(20) primary key,name varchar(20))')

# #增  //逗号加元组或列表都行，不能使用%，会报错
# # cursor.execute('insert into test1 (id,name) values(%s,%s)',['1','bob'])
# # cursor.execute('insert into test1 (id,name) values(%s,%s)',['2','haha'])
# # cursor.execute('insert into test1 (id,name) values(%s,%s)',('3','rose'))
# # cursor.execute('insert into test1 (id,name) values(%s,%s)',(4,'jack'))

# #删
# # cursor.execute('delete from test1 where name = %s',('haha2',))

# #改
# # cursor.execute('update test1 set name= %s where name= %s',('haha2','haha'))

# #查
# cursor.execute('select * from test1')

# values = cursor.fetchall()
# print(values)
# print(cursor.rowcount)

# #提交事务
# conn.commit()
# cursor.close()
# conn.close()

#2.通过数据库直接创建表,然后进行操作
# conn = mysql.connector.connect(user='root',password='',database='test')
# cursor = conn.cursor()

cursor.execute('select * from test2 where id = 3')

values = cursor.fetchall()

if not values:
	print('1')
else:
	print(2,type(values),len(values))
# print(values)






