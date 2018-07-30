# -*- coding: utf-8 -*-

import logging

# 配置共享: logging 模块提供了父子模块共享配置的机制，会根据 Logger 的名称来自动加载父模块的配置
logger = logging.getLogger('main.core')


def run():
    logger.info('logging2 info')
    logger.warning('logging2 warning info')
