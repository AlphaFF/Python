#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-11 17:29:39
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-11 20:17:17

from kafka import KafkaConsumer

consumer = KafkaConsumer('test2', bootstrap_servers=['localhost:9092'], group_id='test_group')

for message in consumer:
    print('message:', message)
    print(message.value.decode())
