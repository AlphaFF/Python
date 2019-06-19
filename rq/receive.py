#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

channel.queue_declare(queue='test')


def callback(ch, method, properties, body):
    print('[x] received', body)


channel.basic_consume(callback, queue='test')

print('waiting for messages. to exit press ctrl+c')
channel.start_consuming()
