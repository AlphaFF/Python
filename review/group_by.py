#!/usr/bin/python3
# -*- coding: utf-8

from itertools import *

# 根据keyfunc对序列每个元素执行后的结果分组
def height_class(h):
    """根据不同的height返回不同的结果"""
    if h > 180:
        return 'tail'
    elif h < 160:
        return 'short'
    else:
        return 'middle'


friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key=height_class)
print(friends)

for key, group in groupby(friends, key=height_class):
    print(key, list(group))
