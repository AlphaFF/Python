# -*- coding: utf-8 -*-

import sys
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

# 声明一个exchange, 类型是fanout
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = ' '.join(sys.argv[2:]) or 'hello world'

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)

print('[x] sent message..')
conn.close()
