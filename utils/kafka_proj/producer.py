#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-11 17:26:49
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-11 20:17:21

import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

i = 0

while i < 100:
    ts = int(time.time() * 1000)
    producer.send(topic='test2', value=str(i).encode(), key=str(i).encode(), timestamp_ms=ts)
    producer.flush()
    print('发送消息:', i)
    i += 1
    time.sleep(2)
