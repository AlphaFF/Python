# !/usr/bin/env python3
# coding:utf-8

import numpy

# #创建一维数组
# x = numpy.array(['a','b',8,123])
# print(x)
# reshape时,当有-1的时候代表当前维度的个数不确定,根据另外一维度的个数可以确定当前维度个数,不能所有的个数都为-1

# #创建二维数组
y = numpy.array([['a','b'],['c','d'],[3,2]])
y.reshape(-1,6)
print(y)

# #排序
# x.sort()
# print(x)

# x1 = numpy.array([1,5,23,12])
# print(x1.max(),x1.min())

# #这一块会报错，待解决
# # x2 = numpy.array(['1','5'])
# # print(x2.max())

# #切片
# print(x[-2:],x[:3])

# import numpy as np
# from numpy import *

# a = np.array([1,2,3])
# print(a)

# # 数学计算
# b = a + 1
# print(b)

# # c = np.array([2,3,4,5])

# # print(a+c)
# print(a**b)
# # print(a*c)

# # 数组形状
# a.shape 
# shape(a)
# # 数组中的数据类型
# a.dtype

# # 查看每个元素所占的字节
# a.itemsize

# # 查看元素数目
# a.size

# # 查看所有元素所占的空间
# a.nbytes

# # 查看数组维数
# a.ndim

# # 多维数组
# b = np.array([1,2,3,4])
# b.shape = 2,2
# print(b)

# #转换其type
# arr.astype(np.float64)  # 当将浮点型数据转为整形时,会将小数点截去

# np.arange(10)  类似于range(10)的用法
# np.empty((8,4)) 

# np.where(cond,xarr,yarr)  可以根据cond中的值选取xarr和yarr

# mean 算术平均数,零长度的数组的mean为NaN
# std/var 分别为标准差和方差,自由度可调
# min/max 最小值/最大值
# argmin/argmax 分别为最大和最小元素的索引
# cumsum 所有元素的累计和
# cumprod 所有元素的累计积
# 使用上面方法时,布尔值会被强制转换为1(True)和0(False)

# any/all 它们对布尔型数组非常有用.any用于测试数组中是否存在一个或多True,而all则检测数组中所有值是否都是True

# 数组切片是原始数组的视图,这就意味着数据不会被复制,视图上的任何修改都会直接反应到源数据
# 如果需要得到ndarray切片的一份副本而非视图,就需要显示地进行复制操作,例如arr[5:8].copy()

# 通过布尔型索引选取数组中的数据,将总是创建数据的副本,即时返回一模一样的数组也是如此
# 花式索引,指的是利用整数数组进行索引
# np.sort() 返回的是数组的已排序副本

# 一维数组的基本运算
# np.unique(arr) 用于找出数组中的唯一值并返回已排序的结果
# np.in1d(arr1,arr2) 用于测试一个数组中的值在另一个数组中的成员资格,返回一个布尔值数组 

# # 乘法仍然是对应元素的乘积，并不是按照矩阵乘法来计算
# print(b*b)

# # 画图
# # linspace 线性间隔 用来生成一组等间隔的数据
# # precision 精度
# a = np.linspace(0,2*pi,21)
# # %precision 3 

# b = sin(a)
# # %matplotlib
# # plot(a,b)

# # 从数组中选择元素
# b >= 0

# plot(b) 只给定y值，默认以下标为x轴



# import pandas as pda

# #创建索引（一维数组）
# a = pda.Series([18,2,10])
# print(a)

# import numpy as np
# import pandas as pd
# # s = pd.Series([1,2,3,4,5,6])
# # print(s)

# # #创建数据框
# # b = pda.DataFrame([[1,2],[3,4],[7,2]])
# # print(b)
# dates = pd.date_range('20130101',periods=6)
# # print(dates)

# print(np.random.randn(6,4))

# df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# # print(df)
# # print(df.head(4)) #头数据，默认5行
# # print(df.tail())	#尾数据，默认5行

# # print(df.index) # 查看下标
# # print(df.columns) # 查看列标
# # print(df.values) # 查看数据

# # print(df.describe()) # 查看简单的统计数据

# print(df.T) # 转置
# print(df.sort_index(ascending=False))


# #取头部数据，默认取前五行
# print(b.head(2))

# #取尾部数据，也是默认后5位
# print(b.tail(2))

# #显示数据的基本统计信息,count数据条数，mean平均数，std标准差，（25%/50%/75%）前中后分位数
# print(b.describe())

# #转置数据，就是横竖颠倒
# print(b.T)

# #导入csv数据
# # c = pda.read_csv(path1)

# # #导入excel数据
# # d = pda.read_excel(path2)

# #导入mysql数据
# import pymysql
# conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='test')
# sql = 'select * from taob'
# e = pda.read_sql(sql,conn)
# # print(e.T)
# #取第几行的数据
# # print(e.T.values[2])

# x = e.T.values[2]
# y = e.T.values[3]
# #导入html数据，读取表格
# # f = pda.read_html('https://book.douban.com/')
# # print(f)



# #导入文本数据
# # g = pda.read_table()

# #数据可视化分析

# #折线图
# import matplotlib.pylab as pyl
# import numpy as npy
# # x = [1,2,3,4,5]
# # y = [4,1,12,2,6]

# #plot(x轴数据,y轴数据，展现形式(默认是折线图，如果带上第三个参数‘o’，则是散点图))
# pyl.plot(x,y)
# pyl.plot(x,y,'o')
# #c-青色 r-红色 m-品红 k-黑色
# # pyl.plot(x,y,'or')
# #‘-’直线  ‘--’虚线  ‘-.’ -.形式  ':'细小虚线
# # pyl.plot(x,y,'r--')
# #'s'方形 '*' 星形 'p' 五角形 '^' 三角形

#scatter 散点图
# 生成0-1之间的200个数
# x = rand(200)
# scatter(x,y,size,color)

## colorbar() 显示颜色条
## 使用figure()命令产生新的图像
## 默认多次 plot 会叠加
## 可以跟Matlab类似用 hold(False)关掉，这样新图会将原图覆盖,之后需要hold(True)来恢复
## 可以在 plot 中加入 label ，使用 legend 加上图例 plot(x,label='sin')
## 可以设置坐标轴的标签和标题 xlabel('sin') ylabel('cos',fontsize='large')  用 grid() 来显示网格  title()来显示title
## clf() 清楚已有的图像  close() 关闭当前图像  close('all') 关闭所有图像


# #设置标题、x标签，y标签
# # pyl.title('show')
# pyl.xlabel('price')
# pyl.ylabel('comments')
# # pyl.xlim(0,20)
# # pyl.plot(x,y,'s')
# pyl.show()

# #随机数(3个参数，最小值、最大值、以及个数)
# # data1 = npy.random.random_integers(1,30,20)
# # #正态分布
# # data2 = npy.random.normal(5.0,2.0,1000)

# #绘制直方图hist
# # pyl.hist(data2)
# # pyl.show()

# # sty = npy.arange(1,30,2)
# # #取消轮廓
# # pyl.hist(data2,histtype='stepfilled')
# # pyl.show()

# #子图subplot(行、列、当前区域)
# # pyl.subplot(2,2,1)
# # pyl.plot(x,y)
# # pyl.subplot(2,1,2)
# # pyl.plot(x,y)
# # pyl.show()

# import numpy as np

# a = np.linspace(0,10,9)
# print(a)
# a.shape = 3,3
# print(a)

# print(a[1:2,[2]])



# 数据清洗(脏数据) 可以查找缺失值、画图分析发现异常值、缺失值处理：均值、中位数插补、固定值、临近插补、回归分析、插值法(拉格朗日插值，牛顿插值)、异常值处理：视为缺失、平均值修正、不处理
# 数据离散化,就是把数据分成几个离散的点,类似于0-60不及格,60-70良,这种类型的
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pylab as pyl

# conn = pymysql.connect('127.0.0.1','root','','test',charset='utf8')
# cursor = conn.cursor()
#
# sql = 'select price,comment from taob'
# data = pd.read_sql(sql,conn)
# # print(data)
#
# # print(data.columns)
#
# # print(data['price'])
# for i in range(len(data['price'])):
# 	if not data['price'][i] or data['price'][i] > 520:
# 		data['price'][i] = 64
#
#
# for i in range(len(data)):
# 	if data['comment'][i] > 26000:
# 		data['comment'][i] = 562
#
# print(data.describe())
#
# # print(data.T)
# data2 = data.T
# print(data2.values[0])
# print(data2.describe())
# price = data2.values[0]
# print(type(price))
# comment = data2.values[1]
# pyl.plot(price,comment,'o')
# pyl.show()

# 绘制直方图
# 1.求最值 2.计算组距 3.极差/组数 4.绘制直方图
# price_max = data2.values[0].max()
# price_min = data2.values[0].min()

# price_columns = (price_max-price_min) / 5
# print(price_columns)
# price_np = np.arange(price_min,price_max,price_columns)
# print(price_np)
# pyl.hist(data2.values[0],price_np)
# pyl.show()  

# comment_max = data2.values[1].max()
# comment_min = data2.values[1].min()
# comment_columns = (comment_max - comment_min) / 5
# comment_np = np.arange(comment_min,comment_max,comment_columns)


# 花式索引不同于切片,实现的是拷贝功能,新生成的数组改变不影响元数据
# for _ in data['price'][data['price'] == 0].index:
# 	data['price'][data['price'] == 0][_] = 64

	
# print(data.describe())



# print(b)

# print(data['price'][data['price'] == 0])
# print(data)

# b['price'] = 64
# print(b['price'])

# with open('/Users/alpha/Desktop/数据分析资料/资料/盗墓笔记1.txt','r') as f:
# 	data = f.readlines()

# jieba的使用
# jieba.cut(s,cut_all=True) # 完全切分
# jieba.cut_for_search(s) # 按照搜索引擎来搜
# jieba.posseg.cut(s) # 不止得到词,还可以得到词性 item.word:词 , item.flag:词性
# jieba.load_userdict(path) # 加载自己的词库
# jieba.analyse jieba.analyse.extract_tags(s,nums)  jieba.analyse.extract_tags(s,3) 提取3个关键词
# jieba.tokenize(s) # 可以得到词的位置(起始)   jieba.tokenize(s,mode='search') # 以搜索引擎的方式搜词


import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

# from scipy import linalg,optimize
#
# print(np.info(optimize.fmin))

# names1800 = pd.read_csv('/Users/alpha/Desktop/names/yob1880.txt',names=['name','sex','birth'])
# print(names1800)


# years = range(1880,2017)

# pieces = []
# columns = ['name','sex','birth']

# for year in years:
# 	path = '/Users/alpha/Desktop/names/yob%s.txt'%year
# 	frame = pd.read_csv(path,names=columns)

# 	frame['year'] = year
# 	pieces.append(frame)

# names = pd.concat(pieces,ignore_index=True)

# names.pivot_table('birth',index='year',columns='sex',aggfunc=sum)

# def add_prop(group):
# 	birth = group.birth.astype(float)
# 	group['prop'] = birth / birth.sum()
# 	return group

# names = names.groupby(['year','sex']).apply(add_prop)

















