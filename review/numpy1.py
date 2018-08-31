#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-30 14:53:48
# @Email: liushahedi@gmail.com
# @Last Modified by:   alpha
# @Last Modified time: 2018-08-30 15:55:20

import numpy as np

array1 = np.array([1, 2, 3])
print(array1)

array2 = np.array([[1, 2, 3], [2, 3, 4]])
print(array2)
print(array2.ndim)
print(array2.shape)
print(array2.size)

array3 = np.array([2, 34, 46], dtype=np.int32)
print(array3.dtype)

array4 = np.zeros((3, 4))
print(array4)

array5 = np.ones((2, 3))
print(array5)

array6 = np.empty((4, 6))
print(array6)

array7 = np.arange(12)
print(array7.reshape(3, 4))


array8 = np.linspace(1, 10, 5)
print(array8)

array9 = np.random.random((2, 4))
print(array9)
print(np.sum(array9, axis=0))
print(np.sum(array9, axis=1))

array10 = np.arange(2, 14).reshape((3, 4))
print(array10)
print(np.argmin(array10))
print(np.argmax(array10))
print(np.mean(array10))
