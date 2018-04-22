# 1.使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉
# 在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N) 
from collections import deque, Iterator
from itertools import islice
import time

q = deque(maxlen=2)
q.append(1)
q.append(2)
# print(q)
q.append(3)
# print(q)

q.appendleft(0)
# print(q)
q.pop()
# print(q)
q.popleft()


# 2.处理大文件读取部分数据的解决方案,使用生成器,读取文件程序和使用文件程序解耦
# islice切片的快速选择
def get_words(path):
    with open(path, 'r') as f:
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            yield line


def deal_words(words, start, offset):
    if not isinstance(words, Iterator):
        return
    for i in islice(words, start, start + offset):
        print(i)


path = '/Users/alpha/Desktop/entname.txt'
t1 = time.time()
results = get_words(path)
deal_words(results, 10000, 12000)
t2 = time.time()
t = t1 - t2
print(t)


# 3.查找最大或最小的 N 个元素
# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素。并且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到，
# 该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N)，N 是堆大小）
import heapq
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# 进行堆排序
heap = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(heap)

# 实现一个优先级队列
# Python 在做元组比较时候，如果前面的比较已经可以确定结果了， 后面的比较操作就不会发生了
# heapq.heappush() 和 heapq.heappop() 分别在队列 _queue 上插入和删除第一个元素， 并且队列 _queue 保证第一个元素拥有最高优先级

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 4.字典中的键映射多个值 (list or set)
# 可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。 
# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了
# defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)


# 5.字典排序
# 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。 在迭代操作的时候它会保持元素被插入时的顺序
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2


# 6.字典的运算
# 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来。
# zip() 函数创建的是一个只能访问一次的迭代器


# 序列中出现次数最多的元素
# collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]


def add(a: int, b:int) -> int:
    return a + b

c = add(3, 4)
print(c)
