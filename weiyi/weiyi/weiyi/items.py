# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class WeiyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hospital_name = scrapy.Field()
    consulting_hour = scrapy.Field()
    hospital_level = scrapy.Field()
    hospital_type = scrapy.Field()
    hospital_category = scrapy.Field()
    hospital_addr = scrapy.Field()
    hospital_pro = scrapy.Field()
    hospital_city = scrapy.Field()
    hospital_county = scrapy.Field()
    hospital_phone = scrapy.Field()
    hospital_intro = scrapy.Field()
    is_medicare = scrapy.Field()
    medicare_type = scrapy.Field()
    vaccine_name = scrapy.Field()
    is_cpc = scrapy.Field()
    is_bdc = scrapy.Field()
    cooperative_business = scrapy.Field()
    hospital_district = scrapy.Field()
    registered_channel = scrapy.Field()
    dataSource_from = scrapy.Field()
    update_time = scrapy.Field()
    pass

    # (hospital_name, consulting_hour, hospital_level, hospital_type, hospital_category, hospital_addr, hospital_pro, hospital_city, hospital_county, hospital_phone, hospital_intro, is_medicare, medicare_type,vaccine_name, is_cpc, is_bdc, cooperative_business, hospital_district, registered_channel, dataSource_from,update_time)
    def get_insert_sql(self):
        insert_sql = """
            insert into hospital_info_test (hospital_name, consulting_hour, hospital_level, hospital_type, hospital_category, hospital_addr, hospital_pro, hospital_city, hospital_county, hospital_phone, hospital_intro, is_medicare, medicare_type,vaccine_name, is_cpc, is_bdc, cooperative_business, hospital_district, registered_channel, dataSource_from,update_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        params = (self.get('hospital_name'),
                  self.get('consulting_hour'),
                  self.get('hospital_level'),
                  self.get('hospital_type'),
                  self.get('hospital_category'),
                  self.get('hospital_addr'),
                  self.get('hospital_pro'),
                  self.get('hospital_city'),
                  self.get('hospital_county'),
                  self.get('hospital_phone'),
                  self.get('hospital_intro'),
                  self.get('is_medicare'),
                  self.get('medicare_type'),
                  self.get('vaccine_name'),
                  self.get('is_cpc'),
                  self.get('is_bdc'),
                  self.get('cooperative_business'),
                  self.get('hospital_district'),
                  self.get('registered_channel'),
                  self.get('dataSource_from'),
                  self.get('update_time', datetime.now().strftime('%Y-%m-%d')))
        return insert_sql, params


class AliasItem(scrapy.Item):
    hospital_name = scrapy.Field()
    hospital_alisename = scrapy.Field()
    dataSource_from = scrapy.Field()
    update_time = scrapy.Field()
    pass

    def get_insert_sql(self):
        insert_sql = """
            insert into hospital_alias_test (hospital_name, hospital_alisename, dataSource_from, update_time)
            values (%s, %s, %s, %s)
        """
        params = (self.get('hospital_name'),
                  self.get('hospital_alisename'),
                  self.get('dataSource_from'),
                  self.get('update_time', datetime.now().strftime('%Y-%m-%d')))
        return insert_sql, params


class DepartmentItem(scrapy.Item):
    hospital_name = scrapy.Field()
    dept_type = scrapy.Field()
    dept_name = scrapy.Field()
    dept_info = scrapy.Field()
    dataSource_from = scrapy.Field()
    update_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into department_info_test (hospital_name, dept_type, dept_name, dept_info, dataSource_from, update_time)
            values (%s, %s, %s, %s, %s, %s)
        """
        params = (self.get('hospital_name'),
                  self.get('dept_type'),
                  self.get('dept_name'),
                  self.get('dept_info'),
                  self.get('dataSource_from'),
                  self.get('update_time', datetime.now().strftime('%Y-%m-%d')))
        return insert_sql, params


class DoctorItem(scrapy.Item):
    doctor_name = scrapy.Field()
    dept_name = scrapy.Field()
    hospital_name = scrapy.Field()
    sex = scrapy.Field()
    doctor_level = scrapy.Field()
    doctor_intro = scrapy.Field()
    doctor_goodat = scrapy.Field()
    diagnosis_amt = scrapy.Field()
    dataSource_from = scrapy.Field()
    update_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into doctor_info_test (doctor_name, dept_name, hospital_name, sex, doctor_level, doctor_intro, doctor_goodat, diagnosis_amt, dataSource_from, update_time)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (self.get('doctor_name'),
                  self.get('dept_name'),
                  self.get('hospital_name'),
                  self.get('sex'),
                  self.get('doctor_level'),
                  self.get('doctor_intro'),
                  self.get('doctor_goodat'),
                  self.get('diagnosis_amt'),
                  self.get('dataSource_from'),
                  self.get('update_time', datetime.now().strftime('%Y-%m-%d')))
        return insert_sql, params


class WeiyiLoader(ItemLoader):
    default_output_processor = TakeFirst()
