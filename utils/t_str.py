#!/usr/bin/env python3
# coding:utf-8

import re


# 罗马字母转数字
# 规则:相同的数字连写，所表示的数等于这些数字相加得到的数，例如：III = 3
# 小的数字在大的数字右边，所表示的数等于这些数字相加得到的数，例如：VIII = 8
# 小的数字，限于（I、X和C）在大的数字左边，所表示的数等于大数减去小数所得的数，例如：IV = 4
# 正常使用时，连续的数字重复不得超过三次
# 在一个数的上面画横线，表示这个数扩大1000倍（本题只考虑3999以内的数，所以用不到这条规则）

def romanToInt(s):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    z = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]

    return z + roman[s[-1]]


# 求所有字符串的最长公共前缀，即数组的所有字符串都包含这个前缀
# 把所有字符串的所有位置(大家都有的)都对应的拿出来,如果有哪一个对应位置的值不同,就返回前面的值
def longestCommonPrefix(strs):
    if not strs:
        return ''
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    return min(strs)


# 先拿最短的,然后拿最短的里面的每一个字母去与其余的对应位置的字符比较,如果相同就不管,如果不同就返回这位置之前的字符串
def longestCommonPrefix1(strs):
    if not strs:
        return ''
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


#
def test_validParentheses(s):
    d = {')': '(', '}': '{', ']': '['}
    stack = ['N']
    for _ in s:
        if _ in [')', '}', ']']:
            if stack.pop() != d[_]:
                return False
            pass
        elif _ in ['(', '{', '[']:
            stack.append(_)
    return len(stack) == 1


# 检索子串在字符串中首次出现的位置
def test_strStr(s1, s2):
    # return s2.index(s1)
    return s2.find(s1) if s2.find(s1) else -1


def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


# 序列中第一个字符串是“1”，接下来依次统计前一个字符串中连续相同字符的数量，并添加到下一字符串中
# 不懂...
def countAndSay(n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s


# 最后一个字符串的长度
def test_lengthOfLastWord(s):
    return len(s.strip().split()[-1])


# add binary 错误,字符串是不可变的
def test_addBinary(s1, s2):
    # 补零,使两个字符串长度相同
    s = min([s1, s2], key=len)
    t = []
    tmp = 0
    if s == s1:
        s1 = '0' * (len(s2 - s1)) + s1
        while len(s1):
            t_s1 = s1.pop()
            t_s2 = s2.pop()
            if int(t_s1) + int(t_s2) + tmp == 2:
                t.insert(0, 0)
                tmp = 1
            else:
                t.insert(0, int(s1.pop()) + int(s1.pop()) + tmp)
                tmp = 0
    return ''.join(t)
    pass

# 二进制相加
def addBinary(a, b):
    if len(a) == 0: return b
    if len(b) == 0: return a
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[0:-1], b[0:-1]), '1') + '0'
    else:
        return addBinary(a[0:-1], b[0:-1]) + str(int(a[-1]) + int(b[-1]))

# a = test_addBinary('1011', '10')
# print(a)

# 测试字符串是不是回文字符串
def test_palindrome(s):
	'''
	1.首先把字符串中不是字母的都去掉;
	2.i.j指针,一个从左开始,一个从右开始,如果相等怎继续,直至重合,不等则不是
	'''
	if not s: return True
	s = s.replace(' ','').replace(',','').replace(':','').lower()
	print(s)
	i = 0 
	j = len(s)-1
	isPalindrome = True
	while i < j:
		if s[i] == s[j]:
			i += 1
			j -= 1 
		else:
			isPalindrome = False
			return isPalindrome
	return isPalindrome

# t = test_palindrome("aba")
# print(t)

def isPalindrome(s):
	l,r = 0,len(s)-1
	while l<r:
		while l < r and not s[l].isalnum():
			l += 1
		while l < r and not s[r].isalnum():
			r -= 1
		if s[l].lower() != s[r].lower():
			return False
		l+=1;r-=1
	return True

# 反转字符串
def test_reverse(s):
	new_s = []
	for i in range(len(s),0,-1):
		print(i)
		new_s.append(s[i-1])
	return ''.join(new_s)

# t = test_reverse('hello')
# print(t)

def reverse(s):
	return s[::-1]

# 反转字符串中的元音字母,a,e,i,o,u,第一个跟最后一个换,倒数第二个跟顺数第二个换
def test_reverse_vowel(s):
	'''
	1.把所有的元音字母找出来,并把原来的替换为None;
	2.把元音字母反转
	3.替换None
	'''
	new_s = list(s)
	vowels = 'aeiouAEIOU'
	stack = []
	for i in range(len(new_s)):
		if new_s[i] in vowels:
			stack.append(new_s[i])
			new_s[i] = None
	print(new_s)
	print(stack)
	for i in range(len(new_s)):
		if new_s[i] is None:
			new_s[i] = stack.pop()
	print(new_s)
	return new_s

# test_reverse_vowel('leetcode')

def reverse_vowels(s):
	v = 'aeiouAEIOU'
	i,j = 0,len(s)-1
	s = list(s)
	while i<j:
		while i<j and s[i] not in v:
			i+=1
		while i<j and s[j] not in v:
			j-=1
		s[i],s[j] = s[j],s[i]
		i+=1
		j-=1
	return ''.join(s)

# ransom note
# 给两个字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成，第二个字符里的每个字符只能使用一次。（假设只包含小写字母）
def test_ransom(s1,s2):
	'''
	1.首先看s1中的每个字母是不是在s2中;
	2.如果在,则把s2中对应的第一个字母替换为None
	3.如果不在,则返回False
	不能用
	'''
	s2 = list(s2)
	# ransom = True
	# for i in range(len(s1)):
	# 	if s1[i] in s2:
	# 		for j in range(len(s2)):
	# 			if s1[i] == s2[j]:
	# 				s2[j] = None
	# 	else:
	# 		ransom = False

	i = 0
	j = 0
	ransom = True
	while i < len(s1) and ransom:
		while j < len(s2) and s1[i] != s2[j]:
			j += 1
		if s1[i] == s2[j]:
			s2[j] == None
			i += 1
		else:
			ransom = False
	return ransom

# t = test_ransom('a','b')
# print(t)


def canConstruct(ransomNote,magazine):
	'''
	两个字符串做差集,得到的Counter对象将删除小于1的元素,Counter对象以字典的形式存储
	'''
	import collections
	return not collections.Counter(ransomNote) - collections.Counter(t)

def test_segments(s):
	count = 0
	pos = 0
	while pos < len(s):
		if s[pos].isalnum():
			pos += 1
		else:
			count += 1 
	return count

# count = test_segments('Hello, my name is John')
# print(count)

def segments(s):
	return len(s.split())

count = segments('Hello, my name is John')
print(count)
	












