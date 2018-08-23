#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: alpha
# @Date:   2018-08-20 16:32:56
# @Email: liushahedi@gmail.com
# @Last Modified by:   alpha
# @Last Modified time: 2018-08-21 09:25:22


import requests


# start_url = 'http://sz.91160.com/'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
#     # 'Connection': 'keep-alive',
#     'Host': 'sz.91160.com',
#     # 'Referer': "https://sz.91160.com/search/index/isopen-1.html",
#     # 'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#     # 'Cookie': '__jsluid=6b06958e2edec783845d6282c69be15a; __jsl_clearance=1534746223.042|0|0xf%2F9DA7QbR%2BWPQZRD8IPIPTHIk%3D'
# }
# res = requests.get(start_url, headers=headers)
# print(res.text)

# url = 'https://www.91160.com/unit/show/uid-21.html'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
    # 'Connection': 'keep-alive',
    'Host': 'sz.91160.com',
    # 'Referer': "https://sz.91160.com/search/index/isopen-1.html",
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    # 'Cookie': '__jsluid=6b06958e2edec783845d6282c69be15a; __jsl_clearance=1534746223.042|0|0xf%2F9DA7QbR%2BWPQZRD8IPIPTHIk%3D'
}

cookies = {
    '__jsluid': '6b06958e2edec783845d6282c69be15a',
    '__jsl_clearance': '1534813501.721|0|kbX%2BmSr1xdyCyrud3jfl9iMlLWY%3D'
}
# res = requests.get(url, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
# print(res.text)

# 1534746223.042|0|0xf%2F9DA7QbR%2BWPQZRD8IPIPTHIk%3D
# 1534754362.798|0|RzM4nXWlDQB4cNybkBxt0PbfiWM%3D


url = 'https://sz.91160.com/home/ajaxgetguahaourl.html'

res = requests.post(url, headers=headers, cookies=cookies, verify=False)
print(res.text)

