#!/usr/bin/env python3
# coding:utf-8

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# 该文件不能命名为email.py,不然会报错（与上面的email冲突）


# 与邮件相关的发件人、收件人以及邮箱服务器的基本信息（公有的）
from_addr = input('From:')
password = input('Password:')  # 此处是客户端的授权密码，而不是登录密码
to_addr = '804950408@qq.com,liushahedi@163.com'
smtp_server = 'smtp.163.com'

# 邮件的内容

# 1.发送文本邮件
# msg = MIMEText('hello,send by python...','plain','utf-8')

# 2.发送html邮件
# msg = MIMEText('<html><body><h1>hello</h1><p>send by <a href="http://www.python.org">Python</a></p></body></html>','html','utf-8')

# 3.发送附件
msg = MIMEMultipart()
msg.attach(MIMEText('hello,send by python...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>hello</h1><p>send by <a href="http://www.python.org">Python</a></p></body></html>',
                    'html', 'utf-8'))

with open('/Users/alpha/Desktop/logo.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='logo.png')
    mime.add_header('Content-Disposition', 'attachment', filename='logo.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

# 发件人、收件人、主题信息（公有的）
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header('测试发邮件 --  python', 'utf-8').encode()  # 必须带上主题，不然会报错

# 基本信息配置后邮件的发送过程（公有的）
# 经过多次测试发现MIMEText()["to"]的数据类型与sendmail(from_addrs,to_addrs,...)的to_addrs不同；前者为str类型，多个地址使用逗号分隔，后者为list类型
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(','), msg.as_string())  # 收件人多个用,号分开，这里是一个列表
server.quit()
