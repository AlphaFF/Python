# -*- coding: utf-8 -*-
import logging
import re
import scrapy
from scrapy.conf import settings
from ..items import DoctorItem


class DoctorSpider(scrapy.Spider):
    """
    1.需带cookie访问,cookie有时效性,好像是根据js算出来的,爬取的时候需要实时更新一下
    cookie值, list和detail的cookie值不同;
    2.每个条件只能拿到1000页的数据;
    """

    name = 'doctor'
    allowed_domains = ['91160.com']
    # 根据科室类型爬取
    start_urls = [('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-D/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-A/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-E/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-F/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-B/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-M/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-C/ysort-1/isopen-1/disease_id-0.html'),
                  ('https://sz.91160.com/search/doctor/p-1/'
                   'cid-5/cno-O/ysort-1/isopen-1/disease_id-0.html')]

    logger = logging.getLogger()

    data_source_from = '深圳医院预约挂号'

    # 爬取list的cookie值
    list_cookies = {
        '__jsluid': '6b06958e2edec783845d6282c69be15a',
        '__jsl_clearance': settings['LIST_JSL']
    }

    # 爬取detail的cookie值
    detail_cookies = {
        '__jsluid': '8d37748fb1ede7f0f9c6f3a0f037032f',
        '__jsl_clearance': settings['DETAIL_JSL']
    }

    # 爬取list需要的headers
    headers = {
        'Accept': ('text/html,application/xhtml+xml,application'
                   '/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
        'Host': 'sz.91160.com',
        'Referer': "https://sz.91160.com/search/doctor.html",
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68'
                       '.0.3440.106 Safari/537.36')
    }

    def start_requests(self):
        for _ in self.start_urls:
            yield scrapy.Request(_,
                                 callback=self.parse_list,
                                 headers=self.headers,
                                 cookies=self.list_cookies,
                                 meta={'page': 1})

    def parse_list(self, response):
        """
        解析列表页内容
        """
        page = response.meta['page']
        doctors = response.xpath('//li[contains(@class, "docter_item")]')
        headers = {
            'Accept': ('text/html,application/xhtml+xml,application/xml;'
                       'q=0.9,image/webp,image/apng,*/*;q=0.8'),
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
            'Host': 'www.91160.com',
            'Referer': response.url,
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.'
                           '0.3440.106 Safari/537.36'),
        }
        self.logger.info('page is %s and doctors is %s', page, len(doctors))
        for _ in doctors:
            # 医生名称
            doctor_name = (_.xpath('./div[@class="doc_info fl"]/h2/a/@title')
                           .extract_first())
            # 医生详情url
            doctor_url = (_.xpath('./div[@class="doc_info fl"]/h2/a/@href')
                          .extract_first())
            # 医生等级
            doctor_level = (_.xpath(('./div[@class="doc_info fl"]/h2/span/'
                                     'text()')).extract_first()
                            .replace('［', '').replace('］', ''))
            hospital_infos = _.xpath(('./div[@class="doc_info fl"]/div[1]/p/'
                                      'text()')).extract()
            # 医院名称, 部门名称
            hospital_name, dept_name = hospital_infos
            # 截取符号前面有用的部门信息
            dept_name = dept_name.split('（')[0].split('【')[0]
            yield scrapy.Request(doctor_url,
                                 callback=self.parse_detail,
                                 headers=headers,
                                 cookies=self.detail_cookies,
                                 meta={'doctor_name': doctor_name,
                                       'doctor_level': doctor_level,
                                       'hospital_name': hospital_name,
                                       'dept_name': dept_name})

        # 如果当前页是第一页,够构造所有页面的爬取链接
        if int(page) == 1:
            last_page = (response.xpath('//p[@id="s_pager"]/a/@href')
                         .extract()[-1])
            # 某条件下的所有页数
            pages = re.findall(r'p-(\d*?)/', last_page)[0]
            if int(pages) > 1:
                for page in range(2, int(pages) + 1):
                    url = re.sub(r'p-\d+?', 'p-{}'.format(page), response.url)
                    self.logger.info('url: %s', url)
                    yield scrapy.Request(url,
                                         callback=self.parse_list,
                                         headers=self.headers,
                                         cookies=self.list_cookies,
                                         meta={'page': page},
                                         dont_filter=True)

    def parse_detail(self, response):
        """
        解析详情页内容
        有些字段列表页已经获取到内容,但是可能不准确,详情页如果获取到值就更新这个值
        """
        # 医生名称
        doctor_name = response.meta['doctor_name']
        # 医院等级
        doctor_level = response.meta['doctor_level']
        # 医院名称
        hospital_name = response.meta['hospital_name'].strip()
        # 部门名称
        dept_name = response.meta['dept_name'].strip()
        # 详情页医生名称
        new_doctor_name = response.xpath('//h1/text()').extract()
        # 详情如果有值则更新值
        doctor_name = (new_doctor_name[0].strip()
                       if new_doctor_name else doctor_name.strip())
        new_doctor_level = response.xpath('//h1/font/text()').extract()
        doctor_level = (new_doctor_level[0].strip()
                        if new_doctor_level else doctor_level.strip())
        # 医生简介
        doctor_intro = ''.join(response.xpath('//p[@id="doc_details"]//text()')
                               .extract()).strip()
        # 医生擅长
        doctor_goodat = response.xpath(('//div[@class='
                                        '"righr_side_content pt10 cl6"'
                                        ']/p/text()')).extract_first()
        item = DoctorItem()
        item['doctor_name'] = doctor_name
        item['doctor_level'] = doctor_level
        item['hospital_name'] = hospital_name
        item['dept_name'] = dept_name
        item['doctor_intro'] = doctor_intro
        item['doctor_goodat'] = doctor_goodat
        item['dataSource_from'] = self.data_source_from
        yield item
