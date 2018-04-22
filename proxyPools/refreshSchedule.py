#!/usr/bin/env python3
# coding=utf-8

from proxyPools.ipManager import ProxyManager
import requests
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler


def validUsefulProxy(proxy):
    proxies = {
        'http': 'http://{}'.format(proxy),
        'https': 'https://{}'.format(proxy),
    }
    try:
        r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=40, verify=False)
        if r.status_code == 200:
            return True
        pass
    except Exception as e:
        print(e)
        return False


class ProxyRefreshSchedule(ProxyManager):
    def __init__(self):
        ProxyManager.__init__(self)

    def validProxy(self):
        self.db.change_table(self.raw_proxy)
        raw_proxy = self.db.pop()
        print(raw_proxy)
        print('start validProxy_a :', raw_proxy)
        exist_proxy = self.db.get_all()
        while raw_proxy:
            if validUsefulProxy(raw_proxy) and (raw_proxy not in exist_proxy):
                self.db.change_table(self.useful_proxy)
                self.db.put(raw_proxy)
                print('validProxy_a: %s validation pass' % raw_proxy)
            else:
                print('validProxy_a: %s validation fail' % raw_proxy)
            self.db.change_table(self.raw_proxy)
            raw_proxy = self.db.pop()
        print('validProxy_a complete...')


def refreshPool():
    pp = ProxyRefreshSchedule()
    pp.validProxy()


def main(process_num=30):
    p = ProxyRefreshSchedule()

    p.refresh()

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
    sched.add_job(main, 'interval', minutes=5)
    sched.start()


if __name__ == '__main__':
    run()
