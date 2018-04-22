#!/usr/bin/env python
# coding:utf-8

from threading import Thread

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

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


class ProxyRefreshSchedule(ProxyManager):
    def __init__(self):
        super(ProxyRefreshSchedule, self).__init__()
        # ProxyManager.__init__(self)

    # 验证raw_proxy_queue中的代理，将可用的代理放到useful_proxy_queue中
    def validProxy(self):
        self.db.change_table(self.raw_proxy_queue)
        exist_proxy = self.db.get_all()
        print(exist_proxy)
        for proxy in exist_proxy:
            if isinstance(proxy,bytes):
                proxy = proxy.decode('utf-8')
                print(proxy)
            if not validUsefulProxy(proxy):
                print("validation fail...")
                self.db.delete(proxy)
            else:
                print("validation pass")


def refreshPool():
    pp = ProxyRefreshSchedule()
    pp.validProxy()


def main(process_num=3):
    p = ProxyRefreshSchedule()

    # 获取新代理
    p.refresh()

    # 检测新代理
    pl = []
    for num in range(process_num):
        proc = Thread(target=refreshPool, args=())
        pl.append(proc)

    for num in range(process_num):
        pl[num].start()

    for num in range(process_num):
        pl[num].join()


def run():
    sched = BlockingScheduler()
    sched.add_job(main, "interval", minutes=1)
    sched.start()


if __name__ == "__main__":
    run()
