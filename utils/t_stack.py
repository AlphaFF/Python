#! /usr/bin/env python3
# coding:utf-8

# implement queue using stacks

class Queue:
	def __init__(self):
		self.inStack,self.outStack = [],[]
		pass

	def push(self,x):
		self.inStack.append(x)
		pass

	def pop(self):
		self.move()
		self.outStack.pop()
		pass

	def peek(self):
		self.move()
		return self.outStack[-1]
		pass

	def empty(self):
		return (not self.inStack) and (not self.outStack)
		pass

	# 采用一个辅助函数,来将列表反转
	def move(self):
		if not self.outStack:
			while self.inStack:
				self.outStack.append(self.inStack.pop())


# next greater element

def test_nextGreaterElement(num1,num2):
	res = -1
	for first_num in num1:
		for last_num in num2:
			if first_num == last_num:
				for final_num in num2[num2.index(first_num)+1:]:
					if final_num > first_num:
						res = final_num
	return final_num

def nextGreaterElement(findNums,nums):
	d = {}
	st = []
	ans = []

	# 给定一个列表,如果有比它大的,就把它从列表中删除,并把它的值记下来,然后进行列表中下一个值的比较
	for x in nums:
		while len(st) and st[-1] < x:
			d[st.pop()] = x
		st.append(x)

	for x  in findNums:
		ans.append(d.get(x,-1))

	return ans


def test_baseBallGamge(l):
	i = ['1','2','3','4','5','6','7','8','9','0']
	valid_values = []
	for _ in l:
		if _ in i:
			score = int(i)
			valid_values.append(score)
			pass
		elif _ == 'C' and len(valid_values):
			valid_values.pop()
			pass
		elif _ == 'D':
			tmp = valid_values[-1]
			valid_values.append(tmp * 2)
			pass
		elif _ == '+':
			valid_values.append(valid_values[-2:])
			pass
	return sum(valid_values)








