# -*- coding: utf-8 -*-

import re
import logging
import scrapy
from ..items import WeiyiLoader, WeiyiItem, DepartmentItem, DoctorItem
from urllib.parse import urljoin


class HnHospitalSpider(scrapy.Spider):
    """河南省预约挂号服务平台"""
    name = 'hn_hospital'
    allowed_domains = ['169000.net']
    # start_urls = ['http://www.169000.net/index.gl?op=c']

    logger = logging.getLogger()
    cities = {
        # '410100': '郑州',
        '410200': '开封',
        # '410300': '洛阳',
        # '410400': '平顶山',
        # '410500': '安阳',
        # '410600': '鹤壁',
        # '410700': '新乡',
        # '410800': '焦作',
        # '410900': '濮阳',
        # '411000': '许昌',
        # '411100': '漯河',
        # '411200': '三门峡',
        # '411300': '南阳',
        # '411400': '商丘',
        # '411500': '信阳',
        # '411600': '周口',
        # '411700': '驻马店',
        # '411800': '济源'
    }

    data_source_from = '河南省预约挂号服务平台'

    def start_requests(self):
        for city in self.cities:
            url = 'http://www.169000.net/index.gl?op=c&city={}'.format(city)
            formdata = {
                'p': '1',
                'dept_a': '-1',
                'dept_b': '-1',
                'dept_c': '-1',
                'city': city
            }
            self.logger.info('url: %s', url)
            yield scrapy.FormRequest(url,
                                     formdata=formdata,
                                     callback=self.parse_list,
                                     meta={'city': city, 'page': 1})
        pass

    def parse_list(self, response):
        # self.logger.info(response.text)
        city = response.meta['city']
        page = response.meta['page']
        self.logger.info('page: %s', page)
        hospital_lists = response.xpath('//li[@class="yy_info"]')
        for _ in hospital_lists:
            hospital_name = (_.xpath('./p[@class="yy_info_name"]/a/text()')
                             .extract())
            hospital_name = hospital_name[0] if hospital_name else None
            hospital_url = (_.xpath('./p[@class="yy_info_name"]/a/@href')
                            .extract())
            hospital_url = hospital_url[0] if hospital_url else None
            hospital_level = (_.xpath('./p[2]/span[1]/text()')
                              .extract())
            hospital_level = hospital_level[0] if hospital_level else None
            hospital_category = (_.xpath('./p[2]/span[2]/text()')
                                 .extract())
            hospital_category = (hospital_category[0]
                                 if hospital_category else None)
            hospital_addr = _.xpath('./p[3]/text()').extract()
            hospital_addr = hospital_addr[0] if hospital_addr else None
            hospital_phone = _.xpath('./p[4]/text()').extract()
            hospital_phone = hospital_phone[0] if hospital_phone else None
            # self.logger.info('name: %s, %s', hospital_name, hospital_url)
            # self.logger.info('%s, %s', hospital_level, hospital_category)
            # self.logger.info('%s, %s', hospital_addr, hospital_phone)
            hospital_url = urljoin(response.url, hospital_url)
            yield scrapy.Request(hospital_url,
                                 callback=self.parse_detail,
                                 meta={'hospital_name': hospital_name,
                                       'hospital_level': hospital_level,
                                       'hospital_category': hospital_category,
                                       'hospital_addr': hospital_addr,
                                       'hospital_phone': hospital_phone,
                                       'hospital_city': city
                                       })

        pages = re.findall(r'window.onload=page\((\d+?),', response.text)
        if pages:
            pages = pages[0]
            if int(pages) > 1 and page == 1:
                for page in range(2, int(pages) + 1):
                    url = ('http://www.169000.net/index.gl?op=c'
                           '&city={}&page={}'.format(city, page))
                    formdata = {
                        'p': str(page),
                        'dept_a': '-1',
                        'dept_b': '-1',
                        'dept_c': '-1',
                        'city': city
                    }
                    self.logger.info('url: %s', url)
                    yield scrapy.FormRequest(url,
                                             formdata=formdata,
                                             callback=self.parse_list,
                                             meta={'city': city,
                                                   'page': page
                                                   })
        pass

    def parse_detail(self, response):
        hospital_loader = WeiyiLoader(item=WeiyiItem(), response=response)
        hospital_name = response.meta['hospital_name']
        hospital_level = response.meta['hospital_level']
        hospital_category = response.meta['hospital_category']
        hospital_addr = response.meta['hospital_addr']
        hospital_phone = response.meta['hospital_phone']
        hospital_city = self.cities.get(response.meta['hospital_city'])
        hospital_intro = (''.join(response.xpath(('//div[@class="p_detail"]'
                                                  '//text()')).extract()))
        hospital_intro = hospital_intro.strip() if hospital_intro else None
        hospital_loader.add_value('hospital_name', hospital_name)
        hospital_loader.add_value('hospital_level', hospital_level)
        hospital_loader.add_value('hospital_category', hospital_category)
        hospital_loader.add_value('hospital_addr', hospital_addr)
        hospital_loader.add_value('hospital_phone', hospital_phone)
        hospital_loader.add_value('hospital_pro', '河南')
        hospital_loader.add_value('hospital_city', hospital_city)
        hospital_loader.add_value('hospital_intro', hospital_intro)
        hospital_loader.add_value('registered_channel', self.data_source_from)
        hospital_loader.add_value('dataSource_from', self.data_source_from)
        yield hospital_loader.load_item()

        departments = response.xpath('//li[@class="clearfix"]')
        for _ in departments:
            department_type = _.xpath('./span/text()').extract()[0]
            department_all = _.xpath('./p/a')
            for _ in department_all:
                department_name = (_.xpath('./text()').extract()[0]
                                   .split('(')[0])
                department_url = _.xpath('./@href').extract()[0]
                department_url = urljoin(response.url, department_url)
                yield scrapy.Request(department_url,
                                     callback=self.parse_department,
                                     meta={'hospital_name': hospital_name,
                                           'department_type': department_type,
                                           'department_name': department_name,
                                           })

    def parse_department(self, response):
        department_loader = WeiyiLoader(item=DepartmentItem(),
                                        response=response)
        hospital_name = response.meta['hospital_name']
        department_type = response.meta['department_type']
        department_name = response.meta['department_name']
        department_info = (''.join(response.xpath('//div[@class="p_detail"]'
                                                  '//text()').extract()))
        department_info = department_info.strip() if department_info else None
        department_loader.add_value('hospital_name', hospital_name)
        department_loader.add_value('dept_type', department_type)
        department_loader.add_value('dept_name', department_name)
        department_loader.add_value('dept_info', department_info)
        department_loader.add_value('dataSource_from', self.data_source_from)
        item = department_loader.load_item()
        yield item

        doctors = response.xpath('//div[@class="ys_info"]')
        for _ in doctors:
            doctor_name = ''.join(_.xpath('.//a//text()').extract())
            doctor_url = _.xpath('.//a/@href').extract()[0]
            doctor_level = _.xpath('./ul/li/span/text()').extract()
            doctor_level = doctor_level[0].strip() if doctor_level else None
            doctor_url = urljoin(response.url, doctor_url)
            yield scrapy.Request(doctor_url,
                                 callback=self.parse_doctor,
                                 meta={'doctor_name': doctor_name,
                                       'doctor_level': doctor_level,
                                       'hospital_name': hospital_name,
                                       'department_name': department_name,
                                       })

    def parse_doctor(self, response):
        doctor_name = response.meta['doctor_name']
        doctor_level = response.meta['doctor_level']
        hospital_name = response.meta['hospital_name']
        department_name = response.meta['department_name']
        doctor_intro = (''.join(response.xpath('//div[@class="p_detail"]'
                                               '//text()').extract()))
        doctor_intro = doctor_intro.strip() if doctor_intro else None
        doctor_loader = WeiyiLoader(item=DoctorItem(), response=response)
        doctor_loader.add_value('doctor_name', doctor_name)
        doctor_loader.add_value('doctor_level', doctor_level)
        doctor_loader.add_value('hospital_name', hospital_name)
        doctor_loader.add_value('dept_name', department_name)
        doctor_loader.add_value('doctor_intro', doctor_intro)
        doctor_loader.add_value('dataSource_from', self.data_source_from)
        yield doctor_loader.load_item()
