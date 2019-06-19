# -*- coding: utf-8 -*-

import sys
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

# 声明一个exchange, 类型是fanout
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'hello world'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print('[x] sent message..', routing_key, message)
conn.close()
