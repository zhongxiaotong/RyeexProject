#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/8/16 11:53
# @Author : Greey
# @FileName: Repeater.py

import os
import argparse
import time
import subprocess
import multiprocessing
import sys

class Repater(object):
    def __init__(self):
        current_path = os.path.abspath(__file__)
        self.father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)

    def repeater(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--taskname", type=str, help=u"固件路径", default='baileys')
        args = parser.parse_args()
        taskname = args.taskname
        try:
            sys.exit(0)
        except SystemExit:
            raise
        finally:
            os.popen("start python " + self.father_path + "\\Run.py --taskname " + taskname)
            os.popen('pause')

if __name__ == '__main__':
    t = multiprocessing.Process(target=Repater().repeater)
    t.start()