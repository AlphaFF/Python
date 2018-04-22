#!/usr/bin python3
# coding:utf-8

from proxyPools.redisClient import RedisClient
from proxyPools.test.getFreeProxy import GetFreeProxy


class ProxyManager(object):
    def __init__(self):
        self.db = RedisClient('proxy', 'localhost', 6379)
        self.raw_proxy_queue = 'raw_proxy'
        self.useful_proxy_queue = 'useful_proxy'
        pass

    # 将代理添加到数据库中
    def refresh(self):
        proxy_set = set()
        for proxy in GetFreeProxy.freeProxyFirst():
            print(proxy)
            if proxy.strip():
                proxy_set.add(proxy)
        self.db.change_table(self.raw_proxy_queue)
        for proxy in proxy_set:
            self.db.put(proxy)

        pass

    # 获得一个有用的代理
    def get(self):
        self.db.change_table(self.useful_proxy_queue)
        return self.db.get()
        pass

    # 从数据库中删除一个代理
    def delete(self, proxy):
        self.db.change_table(self.useful_proxy_queue)
        self.db.delete(proxy)
        pass

    # 获得所有代理
    def getAll(self):
        self.db.change_table(self.useful_proxy_queue)
        return self.db.get_all()
        pass

    # 获取数据库的数据量
    def get_status(self):
        self.db.change_table(self.raw_proxy_queue)
        total_raw_proxy = self.get_status()
        self.db.change_table(self.useful_proxy_queue)
        total_useful_proxy = self.get_status()
        return {"total_raw_proxy": total_raw_proxy, "total_userful_proxy": total_useful_proxy}


if __name__ == '__main__':
    pp = ProxyManager()
    pp.refresh()
    # print(pp.get_status())
