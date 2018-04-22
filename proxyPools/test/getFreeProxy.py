#!/usr/bin python3
# coding:utf-8

class GetFreeProxy(object):
    def __init__(self):
        pass

    @staticmethod
    def freeProxyFirst():
        '''抓取第一个代理'''
        url = 'http://www.kuaidaili.com/free/inha/1/'
        tree = getHtmlTree(url)
        proxy_list = tree.xpath('.//div[@id="list"]//tbody/tr')
        for proxy in proxy_list:
            print(proxy)
            proxy = ':'.join(proxy.xpath('./td/text()')[0:2])
            yield proxy

    @staticmethod
    def freeProxySecond(proxy_number=100):        pass


def getHtmlTree(url, **kw):
    import requests
    from lxml import etree

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }

    html = requests.get(url, headers=headers, timeout=3).text
    return etree.HTML(html)


if __name__ == '__main__':
    gg = GetFreeProxy()
    for e in gg.freeProxyFirst():
        print(e)
