# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.conf import settings
from ..items import DepartmentItem
import re


class DepartmentSpider(scrapy.Spider):
    name = 'department'
    allowed_domains = ['91160.com']
    start_urls = ['https://sz.91160.com/search/dep.html']

    logger = logging.getLogger()

    headers = {
        'Accept': ('text/html,application/xhtml+xml,application/xml;'
                   'q=0.9,image/webp,image/apng,*/*;q=0.8'),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
        'Host': 'sz.91160.com',
        'Referer': "https://sz.91160.com/search/index/isopen-1.html",
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.'
                       '0.3440.106 Safari/537.36'),
    }

    cookies = {
        '__jsluid': '6b06958e2edec783845d6282c69be15a',
        '__jsl_clearance': settings['LIST_JSL']
    }

    data_source_from = '深圳医院预约挂号'

    def start_requests(self):
        for _ in self.start_urls:
            yield scrapy.Request(_,
                                 callback=self.parse_list,
                                 headers=self.headers,
                                 cookies=self.cookies,
                                 meta={'page': 1})

    def parse_list(self, response):
        page = response.meta['page']
        departments = response.xpath('//li[@class="search_item"]')
        dep_item = DepartmentItem()
        dep_item['dataSource_from'] = self.data_source_from
        for _ in departments:
            department_name = _.xpath('./h2/a/text()').extract_first()
            hospital_name = _.xpath(('./div[@class='
                                     '"h_info"]/p[contains(text(), "医院")]'
                                     '/text()')).extract_first()
            hospital_name = hospital_name[hospital_name.find('：') + 1:]
            hospital_name = hospital_name.split('【')[0].split('［')[0]
            dep_item['hospital_name'] = hospital_name
            dep_item['dept_name'] = department_name
            yield dep_item

        if int(page) == 1:
            last_page = (response.xpath('//p[@id="s_pager"]/a/@href')
                         .extract()[-1])
            pages = re.findall(r'p-(\d*?)\.', last_page)[0]
            if int(pages) > 1:
                for page in range(10, 20):
                    url = ('https://sz.91160.com/search/dep/isopen-1/p-{}.html'
                           .format(page))
                    self.logger.info('url: %s', url)
                    yield scrapy.Request(url,
                                         callback=self.parse_list,
                                         headers=self.headers,
                                         cookies=self.cookies,
                                         meta={'page': page})
