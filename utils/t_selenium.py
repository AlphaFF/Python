#!/usr/bin/env python3
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# #phantomjs使用代理方式
# service_args = ['--proxy-auth=H14LXDJ6O07CAFDP:150D24D434AC09EE', '--proxy=http://proxy.abuyun.com:9010']
# driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs',service_args=service_args)
# driver.get('http://httpbin.org/ip')
# print(driver.page_source)

##与页面简单交互
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert 'Python' in driver.title
# elem = driver.find_element_by_name('q')
# elem.clear()
# elem.send_keys('pycon')
# elem.send_keys(Keys.RETURN)
# assert 'no results found' not in driver.page_source
# driver.quit()

##填写表格
# driver = webdriver.Chrome()
# driver.get('http://www.w3school.com.cn/tiy/t.asp?f=html_option')
# select = Select(driver.find_element_by_tag_name('select'))
# print(select.options)
# # select.select_by_visible_text('Audi')
# # select.select_by_index('Audi')
# # select.select_by_value('Audi')
# # select.options
# # select.deselect_all()
# # select.all_selected_options
# driver.find_element_by_id('submit').click()
# element.submit()
# driver.close()

#拖放

