#!/usr/bin/env python3
#coding:utf-8

import logging

# logging.basicConfig(level=logging.INFO)

# logging.warning('waring!')
# logging.debug('debug')
# logging.info('info')
# logging.error('error')
# logging.critical('critical')

# logging.log(logging.INFO,'info')
# logging.log(logging.DEBUG,'debug')
# logging.log(logging.WARNING,'warning')
# logging.log(logging.ERROR,'error')
# logging.log(logging.CRITICAL,'critical')

logger = logging.getLogger()
logger.warning('this is a warning')
