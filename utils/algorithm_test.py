#!/usr/bin/env python3
# coding=utf-8

from timeit import Timer


# def test1():
#     l = []
#     for i in range(1000):
#         l = l + [i]


# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)


# def test3():
#     l = [i for i in range(1000)]


# def test4():
#     l = list(range(1000))

# 栈的实现
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def divideByBase(num, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while num > 0:
        rem = num % base
        remstack.push(rem)
        num = num // base

    binString = ''
    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]

    return binString


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# 无序列表抽象结构
class UnorderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current.current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class OrderList:
    def __init__(self, item):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() < item:
                previous = current
                current = current.getNext()
            else:
                stop = True
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

# 前缀/中缀/后缀 (还未解决...)
def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)

# 顺序查找1(无序)
def sequentialSearch(alist,item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

# 顺序查找(有序)
def orderedSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = True
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

# 二分查找(有序)
def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first < last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = first + 1
    return found

# 二分查找(有序,递归)
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] > item:
            return binarySearch(alist[midpoint+1:],item)
        else:
            return binarySearch(alist[:midpoint],item)

# hash查找 (还未弄懂..待解决)
class HashTabel:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
def hashfunction(self,key,size):
    return key%size

def rehash(self,oldhash,size):
    return (oldhash+1)%size

# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
# 冒泡排序(短冒泡排序)
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

# 选择排序(改进冒泡排序,每次遍历只做一次交换)
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        postionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location]>alist[postionOfMax]:
                postionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[postionOfMax]
        alist[postionOfMax] = temp

# 插入排序
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position += 1

        alist[position] = currentvalue

    pass

# 希尔排序


# 归并排序
def mergeSort(alist):
    if  len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print('merging',alist)



## 树结构
def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

class BinaryTree:
	def __init__(self,rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key






# if __name__ == '__main__':
    # t1 = Timer('test1()', 'from __main__ import test1')
    # print('concat ', t1.timeit(number=1000), 'ms')
    # s = Stack()
    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # print(divideByBase(42, 2))
    # print(divideByBase(42, 16))
    # mylist = UnorderList()
    # mylist.add(31)
    # mylist.add(77)
    # mylist.add(17)
    # mylist.add(93)
    # mylist.add(26)
    # mylist.add(54)
    # print(mylist.search(17))
    # print(infixToPostfix('A * B + C * D'))
    # testlist = [0,1,2,8,13,17,19,32,42]
    # print(orderedSequentialSearch(testlist,3))
    # alist = [54,26,93,17,77,31,44]
    # bubbleSort(alist)
    # print(alist)
    # r = BinaryTree('a')
    # print(r.getRootVal())
    # r.insertLeft('b')
    # print(r.getLeftChild().getRootVal())












