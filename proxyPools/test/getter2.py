#!/usr/bin/env python3
# coding=utf-8

import requests
from lxml import etree


# class ProxyMetaClass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['__crawlFunc__'] = []
#         for k, v in attrs.items():
#             if 'crawl' in k:
#                 attrs['__crawlFunc__'].append(k)
#         return type.__new__(cls, name, bases, attrs)


class ProxyGetter(object):
    # def __init__(self):
    #     self.base_headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    #         'Accept-Encoding': 'gzip, deflate, sdch',
    #         'Accept-Language': 'zh-CN,zh;q=0.8'
    #     }

    def get_html(self, url, options={}):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8'
            }
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                return etree.HTML(r.text)
        except ConnectionError:
            print('Crawling Failed', url)

    # 爬取66代理
    def crawl_daili66(self, page_count=2):
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = self.get_html(url)
            if html:
                try:
                    trs = html.xpath('//div[@id="main"]//tr')
                    for tr in trs[1:]:
                        ip = tr.xpath('td/text()')[0] + ':' + tr.xpath('td/text()')[1]
                        yield ip
                    pass
                except Exception as e:
                    print(e)


    # 爬取西刺代理
    def crawl_xici(self, page_count=2):
        start_url = 'http://www.xicidaili.com/nn{}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = self.get_html(url)
            try:
                trs = html.xpath('//table[@id="ip_list"]/tr')
                for tr in trs[1:]:
                    yield ':'.join(tr.xpath('./td/text()')[0:2])
            except Exception as e:
                print(e)
                pass

    # 爬取360代理

    def crawl_360(self, page_count=2):
        start_url = 'http://www.xicidaili.com/nn{}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = self.get_html(url)
            try:
                trs = html.xpath('//table[@id="ip_list"]/tr')
                for tr in trs[1:]:
                    yield ':'.join(tr.xpath('./td/text()')[0:2])
            except Exception as e:
                print(e)
                pass

    # 爬取全网代理

    def crawl_quanwang(self, page_count=2):
        start_url = 'http://www.goubanjia.com/free/gngn/index{}.shtml'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = self.get_html(url)
            try:
                trs = html.xpath('//div[@id="list"]/tr')
                for tr in trs[1:]:
                    yield ''.join(tr.xpath('./td/text()')[0])
            except Exception as e:
                print(e)
                pass

    # 爬取无忧代理

    def crawl_wuyou(self, page_count=2):
        start_url = 'http://www.goubanjia.com/free/gngn/index{}.shtml'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = self.get_html(url)
            try:
                trs = html.xpath('//ul[@class="l2"]')
                for tr in trs[1:]:
                    yield ':'.join(tr.xpath('.//li/text()')[0:2])
            except Exception as e:
                print(e)
                pass

    # 爬取ip181代理

    def crawl_ip181(self):
        url = 'http://www.ip181.com/'
        html = self.get_html(url)
        try:
            trs = html.xpath('//tr')
            for tr in trs[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])
        except Exception as e:
            print(e)
            pass


    def run(self):
        functions = self.__crawlFunc__
        for function in functions:
            results = eval('self.' + function + '()')
            for result in results:
                print('Getting Proxy', result)
                yield result


if __name__ == '__main__':
    p = ProxyGetter()
    # p.run()
    p.crawl_quanwang()