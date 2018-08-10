#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-10 11:38:51
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-10 11:41:14


from example import crawl


def manage_crawl(urls):
    for url in urls:
        crawl.delay(url)


if __name__ == '__main__':
    start_url = 'https://book.douban.com/tag/小说'
    url_list = ['{}?start={}&type=T'.format(start_url, page * 20) for page in range(10)]
    manage_crawl(url_list)
