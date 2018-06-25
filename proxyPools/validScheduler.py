#!/usr/bin/env python3
# coding=utf-8

import requests

from ipManager import ProxyManager


def validUsefulProxy(proxy):
    proxies = {
        'http':'http://{}'.format(proxy),
        'https':'https://{}'.format(proxy),
    }
    try:
        r = requests.get('http://httpbin.org/ip',proxies=proxies,timeout=40,verify=False)
        if r.status_code == 200:
            return True
        pass
    except Exception as e:
        print(e)
        return False

class ProxyValidSchedule(ProxyManager):
    def __init__(self):
        ProxyManager.__init__(self)

    def __validProxy(self):
        while True:
            self.db.change_table(self.useful_proxy)
            for each_proxy in self.getAll():
                print(each_proxy)
                if isinstance(each_proxy,bytes):
                    each_proxy = each_proxy.decode('utf-8')
                if validUsefulProxy(each_proxy):
                    self.db.inckey(each_proxy,1)
                else:
                    self.db.inckey(each_proxy,-1)
                value = self.db.get_value(each_proxy)
                if value and int(value) < -5:
                    self.db.delete(each_proxy)

    def main(self):
        self.__validProxy()

def run():
    p = ProxyValidSchedule()
    p.main()

if __name__ == '__main__':
    # p = ProxyValidSchedule()
    # p.main()
    t = validUsefulProxy('101.236.22.141:8866')
    print(t)

