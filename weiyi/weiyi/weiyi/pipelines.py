# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class WeiyiPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    """采用同步的机制写入mysql"""

    def __init__(self):
        self.conn = pymysql.connect('192.168.99.19', 'medicalmap1', 'medicalmap#1', 'test', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql, params = item.get_insert_sql()
        try:
            self.cursor.execute(insert_sql, params)
            self.conn.commit()
        except Exception as e:
            spider.logger.info(e)
