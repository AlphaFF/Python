# -*- coding: utf-8 -*-

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

channel.queue_declare(queue='test')

channel.basic_publish(exchange='', routing_key='test', body='hahahaha world.')

print('[x] sent message..')

conn.close()
