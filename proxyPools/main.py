#!/usr/bin/env python3
# coding=utf-8

from multiprocessing import Process
from proxyPools.api import run as ApiRun
from proxyPools.validScheduler import run as ValidRun
from proxyPools.refreshSchedule import run as RefreshRun

def run():
    p_list = []
    p1 = Process(target=ApiRun,name='apiRun')
    p_list.append(p1)
    p2 = Process(target=ValidRun,name='validRun')
    p_list.append(p2)
    p3 = Process(target=RefreshRun,name='refreshRun')
    p_list.append(p3)

    for p in p_list:
        p.start()

    for p in p_list:
        p.join()

if __name__ == '__main__':
    run()
