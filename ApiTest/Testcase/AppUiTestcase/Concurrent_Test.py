#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 22:00
# @Author : Greey
# @FileName: Concurrent_Test.py


import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By
import multiprocessing

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

class Testsmoke:

    def __init__(self):
        self.log = MyLog()
        self.log.info(u'初始化测试数据')
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.init_port = 4723
        self.init_systemPort = 8200
        self.section = 'SATURN_设备'
        self.mac1 = '9C:F6:DD:38:1B:81'
        self.mac2 = '9C:F6:DD:38:1B:78'
        self.mac3 = '9C:F6:DD:38:1B:00'
        self.mac4 = '9C:F6:DD:38:1B:11'
        self.mac5 = '9C:F6:DD:38:1B:22'

    def smoke1(self):
        info = "Process-1"
        port = self.init_port
        systemPort = self.init_systemPort
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()
        andriod_version = App(desired_cap).getdevice_version(uuid)
        desired_cap['deviceName'] = uuid[0]
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = systemPort
        App(desired_cap).start_appium(port, int(port) + 1)
        app = App(desired_cap)
        app.open_application(port)
        app.devices_bind(self.mac1, self.section)
        for i in range(1, 1000):
            try:
                self.log.debug(info + u'血氧心率运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + u"向上滑动成功")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + u"点击心率icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + u"进入心率功能成功")
                time.sleep(3)
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（心率-上级页面）")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + u"点击血氧icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + u"进入血氧功能成功")
                time.sleep(3)
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（血氧-上级页面）")
                app.device_home()
                self.log.debug(info + u"home键返回主页面")
            except:
                self.log.error(info + u'血氧心率在第N次运行失败：' + str(i))
                app.call_back(self.mac1, self.section)
    def smoke2(self):
        info = "Process-2"
        port = int(self.init_port) + 2
        systemPort = int(self.init_systemPort) + 2
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[1]
        andriod_version = App(desired_cap).getdevice_version(uuid)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = systemPort
        App(desired_cap).start_appium(port, int(port) + 1)
        app = App(desired_cap)
        app.open_application(port)
        # size = driver1.get_window_size()
        app.devices_bind(self.mac2, self.section)
        # app1.swpe(size['width']*0.25, size['height']*0.95, size['width']*0.25, size['height']*0.25)
        for i in range(1, 500):
            try:
                self.log.info(info + u'滑动/点击运行次数：' + str(i))
                app.device_downslide()
                self.log.debug(info + u"向下滑动成功")
                app.device_upslide()
                self.log.debug(info + u"向上滑动成功")
                app.device_leftslide()
                self.log.debug(info + u"向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + u"向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + u"向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + u"向左滑动成功")
                app.device_rightslide()
                self.log.debug(info + u"向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + u"向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + u"向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + u"向右滑动成功")
                app.device_longpress()
                self.log.debug(info + u"长按成功")
                app.assert_getdevicepagename("face_pick_page")
                self.log.debug(info + u"进入切换表盘页面成功")
                app.device_leftslide()
                self.log.debug(info + u"向左滑动成功")
                app.device_rightslide()
                self.log.debug(info + u"向右滑动成功")
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + u"点击表盘成功")
                app.device_clickDID()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + u"退出切换表盘页面成功")
            except:
                self.log.error(info + u'滑动/点击在第N次运行失败：' + str(i))
                app.call_back(self.mac2, self.section)

    def smoke3(self):
        info = "Process-3"
        port = int(self.init_port) + 4
        systemPort = int(self.init_systemPort) + 4
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[2]
        andriod_version = App(desired_cap).getdevice_version(uuid)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = systemPort
        App(desired_cap).start_appium(port, int(port) + 1)
        app = App(desired_cap)
        app.open_application(port)
        app.devices_bind(self.mac3, self.section)
        for i in range(1, 100):
            try:
                self.log.debug(info + u'进出各个应用运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + u"向上滑动成功")
                app.saturn_inputclick("80", "80", "80", "80")
                self.log.debug(info + u"点击活动icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("activity")
                self.log.debug(info + u"进入活动功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（活动-上级页面）")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + u"点击心率icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + u"进入心率功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（心率-上级页面）")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + u"点击血氧icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + u"进入血氧功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（血氧-上级页面）")
                app.saturn_inputclick("240", "240", "240", "240")
                self.log.debug(info + u"点击睡眠icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("sleep")
                self.log.debug(info + u"进入睡眠功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（睡眠-上级页面）")
                app.device_upslide()
                self.log.debug(info + u"向上滑动")
                app.saturn_inputclick("80", "10", "80", "10")
                self.log.debug(info + u"点击运动icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("sports")
                self.log.debug(info + u"进入运动功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（运动-上级页面）")
                app.saturn_inputclick("240", "10", "240", "10")
                self.log.debug(info + u"点击运动记录icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("sports_record")
                self.log.debug(info + u"进入运动记录功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（运动记录-上级页面）")
                app.saturn_inputclick("80", "120", "80", "120")
                self.log.debug(info + u"点击闹钟icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("alarm")
                self.log.debug(info + u"进入闹钟功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（闹钟-上级页面）")
                app.saturn_inputclick("240", "120", "240", "120")
                self.log.debug(info + u"点击天气icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("weather")
                self.log.debug(info + u"进入天气功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（天气-上级页面）")
                app.saturn_inputclick("80", "300", "80", "300")
                self.log.debug(info + u"点击秒表icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("appctr_stopwatch")
                self.log.debug(info + u"进入秒表功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（秒表-上级页面）")
                app.saturn_inputclick("240", "300", "240", "300")
                self.log.debug(info + u"点击倒计时icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("appctr_timer")
                self.log.debug(info + u"进入倒计时功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（倒计时-上级页面）")
                app.device_upslide()
                self.log.debug(info + u"向上滑动成功")
                app.saturn_inputclick("80", "40", "80", "40")
                self.log.debug(info + u"点击音乐icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("music")
                self.log.debug(info + u"进入音乐功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（音乐-上级页面）")
                app.saturn_inputclick("240", "40", "240", "40")
                self.log.debug(info + u"点击拍照icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("camera")
                self.log.debug(info + u"进入拍照功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（拍照-上级页面）")
                app.saturn_inputclick("80", "160", "80", "160")
                self.log.debug(info + u"点击冥想icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("meditation")
                self.log.debug(info + u"进入冥想功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（冥想-上级页面）")
                app.saturn_inputclick("240", "160", "240", "160")
                self.log.debug(info + u"点击查找手机icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("findphone")
                self.log.debug(info + u"进入查找手机功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（查找手机-上级页面）")
                app.saturn_inputclick("80", "300", "80", "300")
                self.log.debug(info + u"点击设置icon成功")
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("setting_page")
                self.log.debug(info + u"进入设置功能成功")
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（设置-上级页面）")
                app.device_home()
                self.log.debug(info + u"返回主页面")
            except:
                self.log.error(info + u'进出各个应用在第N次运行失败：' + str(i))
                app.call_back(self.mac3, self.section)

    def smoke4(self):
        info = "Process-4"
        port = int(self.init_port) + 6
        systemPort = int(self.init_systemPort) + 6
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[3]
        andriod_version = App(desired_cap).getdevice_version(uuid)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = systemPort
        App(desired_cap).start_appium(port, int(port) + 1)
        app = App(desired_cap)
        driver = app.open_application(port)
        app.devices_bind(self.mac4, self.section)
        for i in range(1, 2):
            try:
                self.log.debug(info + u'运动中发送消息运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + u'向上滑动成功')
                app.saturn_inputslide("160", "40", "160", "10")
                self.log.debug(info + u'向上滑动一段距离成功')
                app.saturn_inputclick("80", "315", "80", "315")
                self.log.debug(info + u'点击运动成功')
                app.device_clickDID()
                self.log.debug(info + u"获取设备标识")
                app.assert_getdevicepagename("sports")
                self.log.debug(info + u'进入运动应用成功')
                app.device_upslide()
                self.log.debug(info + u'向上滑动成功')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + u'点击IndoorRun')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + u'点击Start')
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                for j in range(1, 50):
                    time.sleep(10)
                    app.tv_send_notification('{"appMessage": {"appId": "app.wx", "text": "reeyx' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                    self.log.debug(info + u'发送消息条数' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.device_home()
                self.log.debug(info + u'按Home键成功')
                app.saturn_inputclick("80", "160", "80", "160")
                self.log.debug(info + u'点击Complete')
                app.saturn_inputclick("160", "300", "160", "300")
                self.log.debug(info + u'点击确认')
                app.device_home()
                self.log.debug(info + u"home键返回上级页面成功（运动-上级页面）")
                app.device_home()
                self.log.debug(info + u"返回主页面")
            except:
                self.log.error(info + u'运动中发送消息在第N次运行失败：' + str(i))
                app.call_back(self.mac4, self.section)

    def smoke5(self):
        info = "Process-5"
        port = int(self.init_port) + 8
        systemPort = int(self.init_systemPort) + 8
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[4]
        andriod_version = App(desired_cap).getdevice_version(uuid)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = systemPort
        App(desired_cap).start_appium(port, int(port) + 1)
        app = App(desired_cap)
        driver = app.open_application(port)
        app.devices_bind(self.mac4, self.section)
        for i in range(1, 500):
            try:
                self.log.debug(u'查看消息运行次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.tv_send_notification('{"appMessage": {"appId": "app.wx", "text": "reeyx' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(u'发送通知成功')
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.saturn_inputslide("160", "80", "160", "160")
                self.log.debug(u'向下滑动一段距离')
                app.saturn_inputslide("160", "160", "160", "80")
                self.log.debug(u'向上滑动一段距离')
                app.saturn_inputslide("160", "160", "160", "160")
                self.log.debug(u'查看消息')
                app.device_clickDID()
                self.log.debug(u'获取设备标识')
                app.assert_getdevicepagename('notification_box_detail')
                self.log.debug(u'进入消息详情页面成功')
            except:
                self.log.error(u'查看消息在第N次运行失败：' + str(i))
                app.call_back(self.mac5, self.section)

if __name__ == '__main__':
    multiprocessings = []
    t1 = multiprocessing.Process(target=Testsmoke().smoke1)
    t2 = multiprocessing.Process(target=Testsmoke().smoke2)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke3)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke4)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke5)
    multiprocessings.append(t1)
    multiprocessings.append(t2)
    # multiprocessings.append(t3)
    # multiprocessings.append(t4)
    # multiprocessings.append(t5)
    for t in multiprocessings:
        t.start()

