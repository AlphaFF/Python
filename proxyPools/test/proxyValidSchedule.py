#!/usr/bin/env python3
# coding=utf-8

import requests

from proxyPools.test.proxyManager import ProxyManager


def validUsefulProxy(proxy):
    proxies = {"http": "http://{}".format(proxy)}
    print(proxies)
    try:
        r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=40)
        if r.status_code == 200:
            print('%s is ok' % proxy)
            return True
    except Exception as e:
        print(e)
        return False


class ProxyValidSchedule(ProxyManager):
    def __init__(self):
        super(ProxyValidSchedule, self).__init__()

    def __validProxy(self):
        while True:
            self.db.change_table(self.useful_proxy_queue)
            for each_proxy in self.db.get_all():
                if isinstance(each_proxy, bytes):
                    each_proxy = each_proxy.decode('utf-8')
                if validUsefulProxy(each_proxy):
                    self.db.inckey(each_proxy, 1)
                else:
                    self.db.inckey(each_proxy, -1)
                value = self.db.get_value(each_proxy)
                if value and int(value) < -5:
                    self.db.delete(each_proxy)

    def main(self):
        self.__validProxy()


def run():
    p = ProxyValidSchedule()
    p.main()


if __name__ == '__main__':
    run()
