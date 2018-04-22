#!/usr/bin/env python3
# coding:utf-8

from nltk.book import *

# print(text1)

## 查找某个文本中的某个词
# print(text1.concordance('monstrous'))

## 查询哪些词出现在相应的上下文中
# print(text1.similar('monstrous'))

## 研究两个或两个以上的词共同上下文
# print(text2.common_contexts(['monstrous','very']))

## 用离散图可以判断词在文本中的位置,每一个竖线代表一个单词,每一行代表整个文本
# text4.dispersion_plot(['citizens','demoncracy','freedom','duties','America'])

## text3.generate(words=None) 该方法已经过期

## 记数词汇
# text3.count('smote')

## 频率分布,即文本中每一个词项的频率
# f = FreqDist(text1)
# v = list(f.keys())
# print(f['whale'])

## 产生词汇的累积频率图
# f.plot(50,cumulative=True)

## 词语搭配和双连词(bigrams)
# bigrams(['more','is','than','done'])

## 找到频繁出现的双连词
# text4.collocations()

## 获得古腾堡项目的语料库
# nltk.corpus.gutenberg.fileids() 

## 获得语料库中的文本
# emma = nltk.corpus.gutenberg.words('austen-emma.txt') 

## 必须把文本转化为Text,才可以使用text1.concordance()检索功能
# emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

## raw()函数 包括了词之间的空格,原始数据
## sents()函数把文本划分为句子,其中每一个句子都是一个列表

## categories() 查看某个语料库的分类,如果有的话,words(categories='news')

## 带条件的频率分布函数
# >>> cfd = nltk.ConditionalFreqDist( ... (genre, word) ... for genre in brown.categories() ... for word in brown.words(categories=genre)) 
# >>> genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor'] 
# >>> modals = ['can', 'could', 'may', 'might', 'must', 'will'] 
# >>> cfd.tabulate(conditions=genres, samples=modals)

## nltk中定义的基本语料库函数(nltk.corpus.udhr.fileids())
# fileids() 语料库中的文件 
# fileids([categories]) 这些分类对应的语料库中的文件 
# categories() 语料库中的分类 
# categories([fileids]) 这些文件对应的语料库中的分类 
# raw() 语料库的原始内容 
# raw(fileids=[f1,f2,f3]) 指定文件的原始内容 
# raw(categories=[c1,c2]) 指定分类的原始内容 
# words() 整个语料库中的词汇 
# words(fileids=[f1,f2,f3]) 指定文件中的词汇 
# words(categories=[c1,c2]) 指定分类中的词汇 
# sents() 指定分类中的句子 
# sents(fileids=[f1,f2,f3]) 指定文件中的句子 
# sents(categories=[c1,c2]) 指定分类中的句子 
# abspath(fileid) 指定文件在磁盘上的位置 
# encoding(fileid) 文件的编码（如果知道的话） 
# open(fileid) 打开指定语料库文件的文件流 
# root() 到本地安装的语料库根目录的路径

## 载入自己的语料库
# from nltk.corpus import PlaintextCorpusReader
# wordlists = PlaintextCorpusReader(path, '.*')

## nltk中的条件频率分布:定义/访问和可视化一个计数的条件频率分布的常用方法
# cfdist= ConditionalFreqDist(pairs) 从配对链表中创建条件频率分布 
# cfdist.conditions() 将条件按字母排序 
# cfdist[condition] 此条件下的频率分布 
# cfdist[condition][sample] 此条件下给定样本的频率 
# cfdist.tabulate() 为条件频率分布制表 
# cfdist.tabulate(samples, conditions) 指定样本和条件限制下制表 
# cfdist.plot() 为条件频率分布绘图 
# cfdist.plot(samples, conditions) 指定样本和条件限制下绘图 
# cfdist1 < cfdist2 测试样本在 cfdist1 中出现次数是否小于在 cfdist2 中出现次 数







