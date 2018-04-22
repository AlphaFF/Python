#!/usr/bin/env python3
# coding:utf-8

# 乱序字符串检查

#1.把s1里的每个字符串拿出来,遍历去s2里找,如果找到了,就把s2里的这个元素设为None,如果没有则是没有找到,则返回false

def anagram1(s1,s2):
	if len(s1) != len(s2):
		return False
	alist = list(s2)

	pos1 = 0
	stillOk = True
	while pos1 < len(s1) and stillOk:
		pos2 = 0
		found = False
		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 += 1
		if found:
			alist[pos2] = None
		else:
			stillOk = False
		pos1 += 1
	return stillOk


# 把字符串排序,然后比较,但是调用排序方法也是耗时的
def anagram2(s1,s2):
	alist1 = list(s1)
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()

	pos = 0
	matches = True

	while pos < len(s1) and matches:
		if alist1[pos] == alist2[pos]:
			pos += 1
		else:
			matches = False
	return matches

# 桶排序,如果所有字母出现的次数都相同,则相同
def anagram3(s1,s2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('a')
		c1[pos] = c1[pos] + 1

	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('a')
		c2[pos] = c2[pos] + 1

	j = 0
	stillOk = True
	while j < 26 and stillOk:
		if c1[j] == c2[j]:
			j = j+1
		else:
			stillOk = False
	return stillOk


# 顺序查找 (复杂度O(n))
def sequentialSearch(alist,item):
	pos = 0
	found = False
	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else :
			pos += 1
	return found

# 有序顺序查找,如果item小于当前值,那么它也会小于后面的所有值,所以就不用再找了
def testOrderSequentialSearch(alist,item):
	pos = 0 
	found = False
	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		elif alist[pos] > item:
			return found
		else:
			pos += 1
	return found

def order

