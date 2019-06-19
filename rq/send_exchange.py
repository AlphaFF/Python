# -*- coding: utf-8 -*-

import sys
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

# 声明一个exchange, 类型是fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = sys.argv[1:] or 'hello world'

channel.basic_publish(exchange='logs', routing_key='', body=message)

print('[x] sent message..')

conn.close()
