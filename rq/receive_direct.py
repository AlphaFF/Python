#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

# 声明一个exchange, 类型是fanout
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 声明一个临时队列
tmp_queue = channel.queue_declare(exclusive=True)
queue_name = tmp_queue.method.queue

severities = sys.argv[1:]
if not severities:
    sys.exit(1)


# 绑定一个交换机
for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)


def callback(ch, method, properties, body):
    print('[x] received', body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

print('waiting for messages. to exit press ctrl+c')
channel.start_consuming()
