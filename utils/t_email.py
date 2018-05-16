#!/usr/bin/env python3
# coding:utf-8

import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import pymysql
from datetime import datetime

# 与邮件相关的发件人、收件人以及邮箱服务器的基本信息（公有的）
from_addr = 'automail@yscredit.com'
password = 'y8svUoBf'  # 此处是客户端的授权密码，而不是登录密码
to_addrs = '291376690@qq.com, 804950408@qq.com'
smtp_server = 'smtp.yscredit.com'

def send_msg(body, to_addr):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['Subject'] = Header('搜狗微信插入数据结果', 'utf-8').encode()
    msg['To'] = to_addr
    server = smtplib.SMTP(smtp_server, 80)  # 阿里云上需要80端口发送
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr.split(), msg.as_string())  # 收件人多个用,号分开，这里是一个列表
    server.quit()

if __name__ == '__main__':
    msg = 'test email'
    receivers = ['291376690@qq.com', '804950408@qq.com', '986883050@qq.com']
    # msg = '测试单个收件人'
    for receiver in receivers:
        send_msg(msg, receiver)
