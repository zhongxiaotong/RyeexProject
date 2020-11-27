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
    log.info(t2.name)


def smoke1():
    info1 = "Process-1"
    desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
    app = App(desired_caps)
    wyzeband_mac1 = "9C:F6:DD:38:1B:81"
    # App.start_appium(4723, 4724, "468207dd")
    driver = app.open_application('4723')
    time.sleep(1)
    app.devices_click('SATURN_设备')
    time.sleep(1)
    while app.object_exist(wyzeband_mac1 + "  正在连接...") :
        time.sleep(1)
    if app.object_exist(wyzeband_mac1 + "  已连接") == False:
        app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        app.click_prompt_box()
        if (app.object_exist("realme Watch Saturn") or app.object_exist("WYZE") or app.object_exist("hey+")) == False:
            app.close_app()
            # self.app_setting.restart_bluetooth()                                                                       #重启蓝牙
            driver = app.open_app()
            app.devices_click('SATURN_设备')
            app.devices_click('解绑')
        while app.object_exist(wyzeband_mac1) == False:
            time.sleep(1)
        app.devices_click(wyzeband_mac1)
        while app.object_exist(wyzeband_mac1) == False:
            time.sleep(1)
            app.devices_click('完成')
            app.devices_click('SATURN_设备')
            app.saturn_inputclick("160", "240", "160", "240")
            driver.keyevent(4)
            app.devices_click('SATURN_设备')
    time.sleep(1)
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
    wyzeband_mac2 = "9C:F6:DD:38:1B:78"
    # App.start_appium(4725, 4726, "HDP9K19128907088")
    driver1 = app1.open_application('4725')
    size = driver1.get_window_size()
    time.sleep(1)
    app1.devices_click('SATURN_设备')
    time.sleep(1)
    while app1.object_exist(wyzeband_mac2 + "  正在连接...") :
        time.sleep(1)
    if app1.object_exist(wyzeband_mac2 + "  已连接") == False:
        app1.devices_click('解绑')
        app1.click_prompt_box()
        if (app1.object_exist("realme Watch 2") or app1.object_exist("WYZE") or app1.object_exist("hey+")) == False:
            app1.close_app()
            # app1.restart_bluetooth()                                                                       #重启蓝牙
            driver1 = app1.open_app()
            app1.devices_click('SATURN_设备')
            app1.devices_click('解绑')
        while app1.object_exist(wyzeband_mac2) == False:
            time.sleep(1)
        app1.devices_click(wyzeband_mac2)
        while app1.object_exist("请在设备上点击确认") == False:
            time.sleep(1)
        driver1.keyevent(4)
        driver1.keyevent(4)
        app1.devices_click('完成')
        app1.devices_click('SATURN_设备')
        app1.saturn_inputclick("160", "240", "160", "240")
        driver1.keyevent(4)
        app1.devices_click('SATURN_设备')
    time.sleep(1)
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
    t2 = multiprocessing.Process(target=smoke2)
    t1.start()
    t2.start()
    initdata()
