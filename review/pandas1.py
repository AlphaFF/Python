#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-09-07 16:29:59
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-09-07 16:45:51


import pandas as pd
import numpy as np

s = pd.Series([1, 2,6, np.nan, 44, 1])
print(s)

dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

# print(df['b'])
# print(df.index)
# print(df.sort_values(by='b'))
print(df.T)

print(df[0:2])

