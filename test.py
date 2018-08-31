#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-30 16:22:18
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-31 14:45:40

import requests
from requests_toolbelt import MultipartEncoder
from lxml import etree
import pymysql


def get_page_response(state=None):
    url = 'http://app.bjsf.gov.cn/tabid/219/Default.aspx'
    headers = {
        'Host': 'app.bjsf.gov.cn',
        'Origin': 'http://app.bjsf.gov.cn',
        'Content-Type': '',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://app.bjsf.gov.cn/tabid/219/Default.aspx',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
        'Cookie': '.ASPXANONYMOUS=YYgaRsp21AEkAAAAMGM5NGQyYjItM2UyYS00Mzk4LTg2ZjQtMDUxZGViYjlkNzJj0;'
    }
    if not state:
        res = requests.get(url, headers=headers)
        return res
    file_payload = {
        '__EVENTARGUMENT': '',
        '__EVENTTARGET': 'ess$ctr740$LawOfficeSearchList$lbtnNextPage',
        '__VIEWSTATE': state,
        '__VIEWSTATEENCRYPTED': '',
        'ScrollTop': '',
        '__essVariable': '{"__scdoff":"1"}',
        'ess$ctr740$LawOfficeSearchList$txtName': '',
        'ess$ctr740$LawOfficeSearchList$txtCodeNum': '',
        'ess$ctr740$LawOfficeSearchList$txtReponseName': '',
        'ess$ctr740$LawOfficeSearchList$ddlType': '1',
        'ess$ctr740$LawOfficeSearchList$ddlCountry': '-1',
        'ess$ctr740$LawOfficeSearchList$txtPageNum': ''
    }
    m = MultipartEncoder(file_payload)
    headers['Content-Type'] = m.content_type
    res = requests.post(url, headers=headers, data=m, timeout=10)
    return res


def parse_list(response):
    html = etree.HTML(response.text)
    results = html.xpath('//table[@class="datagrid-main"]/tr')[1:]
    for result in results:
        lawyer_name = result.xpath('.//a/text()')[0]
        lawyer_url = result.xpath('.//a/@href')[0]
        lawyer_id = lawyer_url.split('=')[-1]
        print(lawyer_name, lawyer_url, lawyer_id)
        parse_detail(lawyer_id)

    next_page_disabled = html.xpath('//a[text()="下一页"]/@disabled')
    page = html.xpath('//font[@color="red"]/text()')[0]
    if not next_page_disabled:
        print('page:', page)
        state = html.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
        res = get_page_response(state)
        parse_list(res)


def parse_detail(lawyer_id):
    url = 'http://app.bjsf.gov.cn/tabid/238/Default.aspx?itemid={}'.format(lawyer_id)
    res = requests.get(url)
    html = etree.HTML(res.text)
    rows = html.xpath('//table[@class="TableHeader kaifxx"]/tr')
    lawyer_item = {}
    for row in rows:
        td_nums = len(row.xpath('./td'))
        for _ in range(td_nums // 2):
            key = row.xpath('./td[@class="tdLeft"][{}]/text()'.format(_ + 1))[0].strip()
            value = row.xpath('./td[@class="tdRight"][{}]//text()'.format(_ + 1))
            # print(value)
            if value:
                value = [_.strip() for _ in value if _.strip()]
                value = value[0] if value else ''
            else:
                value = ''
            lawyer_item[key] = value
    # print(lawyer_item)
    for key, value in lawyer_item.items():
        if '全称' in key:
            lawyer_full_name = value
        elif '主任' in key:
            lawyer_director = value
        elif '组织形式' in key:
            lawyer_form = value
        elif '电话' in key:
            lawyer_tel = value
        elif 'mail' in key:
            lawyer_email = value
        elif '发证日期' in key:
            lawyer_publish_date = value
        elif '党支部形式' in key:
            lawyer_party_form = value
        elif '党支部负责人' in key:
            lawyer_form_director = value
        elif '场所面积' in key:
            lawyer_place_size = value
        elif '场所性质' in key:
            lawyer_place_nature = value
        elif '传真' in key:
            lawyer_fox = value
        elif '地址' in key:
            lawyer_address = value
        else:
            pass
    params = lawyer_full_name, lawyer_director, lawyer_form, lawyer_tel, lawyer_email, lawyer_publish_date, lawyer_party_form, lawyer_form_director, lawyer_place_size, lawyer_place_nature, lawyer_fox, lawyer_address
    insert_into_sql(params)


def insert_into_sql(params):
    cursor = conn.cursor()
    sql = """insert into lawyer (lawyer_full_name, lawyer_director, lawyer_form, lawyer_tel, lawyer_email, lawyer_publish_date, lawyer_party_form, lawyer_form_director, lawyer_place_size, lawyer_place_nature, lawyer_fox, lawyer_address)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


if __name__ == '__main__':
    conn = pymysql.connect('127.0.0.1', 'root', '', 'test', charset="utf8", use_unicode=True)
    res = get_page_response()
    parse_list(res)
    conn.close()
    # parse_detail(125688)
