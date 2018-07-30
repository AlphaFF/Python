#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__: AlphaFF


import logging
import logging2


logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y/%m/%d %H:%M:%S',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('main')


logger.info('this is a log info %s', 'test')
logger.warning('this is a warning info')

# 捕获Traceback
try:
    result = 10 / 0
except Exception:
    logger.error('Fail to get %s result', 'error', exc_info=1)

try:
    result = 2 >= '1'
except Exception:
    logger.exception('Error')
logger.info('Finished')

logging2.run()
