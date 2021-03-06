#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/8/18 14:13
# @Author : Greey
# @FileName: Log.py

"""
封装log方法
"""

import logging
import os
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf8")

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)


def get_current_time():
    return time.strftime(MyLog.date, time.localtime(time.time()))


class MyLog(object):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    currentdate = datetime.datetime.now().strftime('%Y-%m-%d')
    log_file = path + '/Log/' + currentdate + '.log'
    err_file = path + '/Log/' + currentdate + '_error.log'
    # log_file = path + '/Log/log.log'
    # err_file = path + '/Log/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    handler = logging.FileHandler(log_file, encoding='utf-8', mode='a')
    err_handler = logging.FileHandler(err_file, encoding='utf-8', mode='a')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.critical("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')


# if __name__ == "__main__":
    # MyLog.debug("This is debug message")
    # MyLog.info("This is info message")
#     MyLog.warning("This is warning message")
#     MyLog.error("This is error")
#     MyLog.critical("This is critical message")