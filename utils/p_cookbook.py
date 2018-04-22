
import heapq

# 如何从一个集合中获得最大或者最小的n个元素列表
nums = [1, 2, 3, 4, 5, 6, 7]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 能接受一个关键字参数
p = [{'name':'a','price':10},{'name':'b','price':12}]
cheap = heapq.nsmallest(3, p,key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, p, key=lambda s: s['price'])
print(expensive)