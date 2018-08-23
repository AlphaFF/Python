# -*- coding: utf-8 -*-
import scrapy
import logging
from ..items import WeiyiItem, AliasItem
from scrapy.conf import settings


class A160Spider(scrapy.Spider):
    name = '160'
    allowed_domains = ['91160.com']
    start_urls = ['https://sz.91160.com/search/index.html']

    logger = logging.getLogger()

    headers = {
        'Accept': ('text/html,application/xhtml+xml,application/xml;'
                   'q=0.9,image/webp,image/apng,*/*;q=0.8'),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
        'Host': 'sz.91160.com',
        'Referer': "https://sz.91160.com/search/index/isopen-1.html",
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68'
                       '.0.3440.106 Safari/537.36'),
    }

    data_source_from = '深圳医院预约挂号'

    def start_requests(self):
        cookies = {
            '__jsluid': '6b06958e2edec783845d6282c69be15a',
            '__jsl_clearance': settings['LIST_JSL']
        }
        for start_url in self.start_urls:
            yield scrapy.Request(start_url,
                                 callback=self.parse_list,
                                 headers=self.headers,
                                 cookies=cookies)
        pass

    def parse_list(self, response):
        hospitals = response.xpath('//li[contains(@class, "search_item")]')
        headers = {
            'Host': 'www.91160.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                           ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                           '68.0.3440.106 Safari/537.36'),
            'Accept': ('text/html,application/xhtml+xml,application/xml;q='
                       '0.9,image/webp,image/apng,*/*;q=0.8'),
            'Referer': 'https://www.91160.com/unit/show/uid-21.html',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6"
        }
        detail_cookies = {
            '__jsluid': '8d37748fb1ede7f0f9c6f3a0f037032f',
            '__jsl_clearance': settings['DETAIL_JSL']
        }
        for hospital in hospitals:
            hospital_url = hospital.xpath('./h2/a/@href').extract_first()
            hospital_name = hospital.xpath('./h2/a/text()').extract_first()
            hospital_addr = (hospital.xpath(('./div[@class='
                                             '"h_info layout"]/p[2]/text()'))
                             .extract_first().split('：')[-1])
            hospital_phone = (hospital.xpath(('./div[@class='
                                              '"h_info layout"]/p[3]/text()'))
                              .extract_first().split('：')[-1])
            self.logger.info('url: %s', hospital_url)
            # detail_url = hospital_url.replace('show', 'unitintro')
            # self.logger.info('detail_url: %s', detail_url)
            yield scrapy.Request(hospital_url,
                                 callback=self.parse_detail,
                                 headers=headers,
                                 cookies=detail_cookies,
                                 meta={'hospital_name': hospital_name,
                                       'hospital_addr': hospital_addr,
                                       'hospital_phone': hospital_phone})

        next_page = response.xpath('//p[@id="s_pager"]/a/@href').extract()[-2]
        self.logger.info('next_page: %s', next_page)
        if 'javascript' not in next_page:
            headers = {
                'Accept': ('text/html,application/xhtml+xml,application/xml;'
                           'q=0.9,image/webp,image/apng,*/*;q=0.8'),
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': ('en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;'
                                    'q=0.6'),
                'Host': 'sz.91160.com',
                'Referer': ('https://sz.91160.com/search/index/isopen-1/p-3.'
                            'html'),
                'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_'
                               '6) AppleWebKit/537.36 (KHTML, like Gecko) Chro'
                               'me/68.0.3440.106 Safari/537.36'),
            }
            list_cookies = {
                '__jsluid': '6b06958e2edec783845d6282c69be15a',
                '__jsl_clearance': settings['LIST_JSL']
            }
            yield scrapy.Request(next_page,
                                 callback=self.parse_list,
                                 headers=headers,
                                 cookies=list_cookies)

    def parse_detail(self, response):
        """
        特殊详情页
        https://www.91160.com/unit/show/uid-200023351.html
        https://www.91160.com/unit/show/uid-173.html
        """
        # self.logger.info(response.text)
        hospital_name = response.meta['hospital_name']
        hospital_addr = response.meta['hospital_addr']
        hospital_phone = response.meta['hospital_phone']
        item = WeiyiItem()
        hospital_county = response.xpath(('//div[contains(@class, '
                                          '"crumbs_link")]/a[contains(@href,'
                                          ' "aid")]/text()')).extract_first()
        new_hospital_name = response.xpath(('//div[@class="layout mb10"'
                                            ']/h1/a/text()')).extract_first()
        hospital_name = (new_hospital_name.strip()
                         if new_hospital_name else hospital_name.strip())
        hospital_level = response.xpath(('//div[@class="layout mb10"'
                                         ']/em/text()')).extract_first()
        hospital_infos = response.xpath(('//ul[contains(@class, "hos_info_ul"'
                                         ')]/li'))
        hospital_alias = hospital_infos.xpath(('./em[contains(text(), "别名")]'
                                               '/parent::li/text()')).extract()
        if not hospital_name:
            return
        if hospital_alias:
            alias_item = AliasItem()
            hospital_alias = hospital_alias[0].strip().split(',')
            for _ in hospital_alias:
                alias_item['hospital_name'] = hospital_name
                alias_item['hospital_alisename'] = _.strip()
                yield alias_item
        new_hospital_addr = (hospital_infos.xpath(('./font[contains(text(),'
                                                   ' "地址")]/parent::li/text()')
                                                  ).extract())
        hospital_addr = (new_hospital_addr[0]
                         if new_hospital_addr else hospital_addr)
        new_hospital_phone = hospital_infos.xpath(('./font[contains(text(),'
                                                   ' "电话")]/parent::li/text()')
                                                  ).extract()
        hospital_phone = (new_hospital_phone[0]
                          if new_hospital_phone else hospital_phone)
        if hospital_addr:
            hospital_addr = (None if '暂无' in hospital_addr
                             else hospital_addr.strip())
        else:
            hospital_addr = None
        if hospital_phone:
            hospital_phone = (None if '暂无' in hospital_phone
                              else hospital_phone.strip())
        else:
            hospital_phone = None
        hospital_info_url = (hospital_infos.xpath('./a[text()="详细>"]/@href')
                             .extract())
        item['hospital_name'] = hospital_name
        item['hospital_level'] = hospital_level
        item['hospital_addr'] = hospital_addr
        item['hospital_phone'] = hospital_phone
        item['hospital_county'] = hospital_county
        if not hospital_info_url:
            self.logger.info('url: %s详细介绍不存在', response.url)
            yield item
            return
        headers = {
            'Host': 'www.91160.com',
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                           ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                           '68.0.3440.106 Safari/537.36'),
            'Accept': ('text/html,application/xhtml+xml,application/xml;q=0'
                       '.9,image/webp,image/apng,*/*;q=0.8'),
            'Referer': response.url,
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6'
        }
        cookies = {
            '__jsluid': '8d37748fb1ede7f0f9c6f3a0f037032f',
            '__jsl_clearance': settings['DETAIL_JSL']
        }
        yield scrapy.Request(hospital_info_url[0],
                             callback=self.parse_info,
                             headers=headers,
                             cookies=cookies,
                             meta={'item': item})

    def parse_info(self, response):
        # self.logger.info(response.text)
        item = response.meta['item']
        hospital_infos = response.xpath(('//div[@class="hos_about layout"]'
                                         '//text()')).extract()
        hospital_intro = ''.join([_.strip() for _ in hospital_infos])
        item['hospital_intro'] = hospital_intro
        item['hospital_pro'] = '广东'
        item['hospital_city'] = '深圳'
        item['dataSource_from'] = self.data_source_from
        # self.logger.info(hospital_info)
        yield item
