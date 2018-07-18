#!/usr/bin/python3
# -*- coding: utf-8 -*-

from copy import copy, deepcopy

# copy.copy()
a = [1, 2, [3, 4]]
b = copy(a)
a[2].append(5)
print(a, b)

# copy.deepcopy()
c = deepcopy(a)
a[2][2] = 6
print(a, c)
