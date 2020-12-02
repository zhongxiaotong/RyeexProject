#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 22:00
# @Author : Greey
# @FileName: Concurrent_Test.py


import pytest
import os
import time
import allure
from ApiTest.Common.Appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By
import multiprocessing

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"
log = MyLog()
def initdata():
    log.info(u'初始化测试数据')
    log.info(t1.name)
    # log.info(t2.name)


def smoke1():
    info1 = "Process-1"
    desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
    app = App(desired_caps)
    driver = app.open_application('4723')
    size = driver.get_window_size()
    app.devices_bind('9C:F6:DD:38:1B:81', 'SATURN_设备')
    app.device_upslide()
    for i in range(1, 50):
        try:
            log.debug(info1 + u'血氧心率运行次数：' + str(i))
            app.saturn_inputclick("240", "80", "240", "80")
            log.debug(info1 + u"点击心率icon成功")
            app.assert_getdevicepagename("hrm")
            log.debug(info1 + u"进入心率功能成功")
            time.sleep(3)
            app.device_home()
            log.debug(info1 + u"home键返回上级页面成功（心率-上级页面）")
            app.saturn_inputclick("80", "240", "80", "240")
            log.debug(info1 + u"点击血氧icon成功")
            app.assert_getdevicepagename("spo2")
            log.debug(info1 + u"进入血氧功能成功")
            time.sleep(3)
            app.device_home()
            log.debug(info1 + u"home键返回上级页面成功（血氧-上级页面）")
        except:
            log.error(info1 + u'血氧心率在第N次运行失败：' + str(i))
            app.device_home()
            app.device_home()
            app.device_upslide()
            log.debug(info1 + u"回到主页面")
def smoke2():
    info2 = "Process-2"
    desired_caps2 = Yamlc(yaml_path).get_yaml_data(3, "Model", "desired_caps")
    app1 = App(desired_caps2)
    # App.start_appium(4725, 4726, "HDP9K19128907088")
    driver1 = app1.open_application('4725')
    size = driver1.get_window_size()
    app1.devices_bind('9C:F6:DD:38:1B:81', 'SATURN_设备')
    app1.swpe(size['width']*0.25, size['height']*0.95, size['width']*0.25, size['height']*0.25)
    for i in range(1, 50):
        try:
            log.info(info2 + u'滑动/点击运行次数：' + str(i))
            app1.device_downslide()
            log.debug(info2 + u"向下滑动成功")
            app1.device_upslide()
            log.debug(info2 + u"向上滑动成功")
            app1.device_leftslide()
            log.debug(info2 + u"向左滑动成功")
            app1.device_leftslide()
            log.debug(info2 + u"向左滑动成功")
            app1.device_leftslide()
            log.debug(info2 + u"向左滑动成功")
            app1.device_leftslide()
            log.debug(info2 + u"向左滑动成功")
            app1.device_rightslide()
            log.debug(info2 + u"向右滑动成功")
            app1.device_home()
            log.debug(info2 + u"按home键成功")
            app1.device_longpress()
            log.debug(info2 + u"长按成功")
            app1.assert_getdevicepagename("face_pick_page")
            log.debug(info2 + u"进入切换表盘页面成功")
            app1.device_leftslide()
            log.debug(info2 + u"向左滑动成功")
            app1.device_rightslide()
            log.debug(info2 + u"向右滑动成功")
            app1.device_home()
            log.debug(info2 + u"home键成功")
            app1.assert_getdevicepagename("home_page")
            log.debug(info2 + u"退出切换表盘页面成功")
        except:
            log.error(info2 + u'滑动/点击在第N次运行失败：' + str(i))
            app1.device_home()
            log.debug(info2 + u"回到主页面")




if __name__ == '__main__':
    t1 = multiprocessing.Process(target=smoke1)
    # t2 = multiprocessing.Process(target=smoke2)
    t1.start()
    # t2.start()
    initdata()

