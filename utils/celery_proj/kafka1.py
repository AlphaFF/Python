#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-11 17:17:58
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-11 17:18:37


from kafka import KafkaConsumer

consumer = KafkaConsumer('test_topic')
