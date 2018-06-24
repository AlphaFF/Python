#!/usr/bin/env python3
# coding=utf-8

# 输入
# 计算地图上两点经纬度间的距离
from math import radians, cos, sin, asin, sqrt
# Haversine(lon1, lat1, lon2, lat2)的参数代表：经度1，纬度1，经度2，纬度2（十进制度数）
def Haversine(lon1, lat1, lon2, lat2):
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半径，单位为公里
    d = c * r
    print("该两点间距离={0:0.3f} km".format(d))
#
# # 广州市人民政府 113.270714,23.13552
# # 深圳市人民政府 114.064803,22.549054
# Haversine(113.270714,23.13552,114.064803,22.549054)


import json
import requests

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'SNs64mAiYOUlfOtZ8ttv8gGq9pkd9eD6'
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
    req = requests.get(uri)
    res = req.text #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

print(getlnglat('松和时代商城'))