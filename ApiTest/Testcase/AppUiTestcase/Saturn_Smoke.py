#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 22:00
# @Author : Greey
# @FileName: Saturn_Smoke.py

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
        self.log.info('初始化测试数据')
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.init_port = 4723
        self.init_systemPort = 8200
        self.section = 'SATURN_设备'
        self.driver = None
        self.desired_cap = self.dictdatas[0]['desired_caps']

        self.uuids = App(self.desired_cap).getdevices_uuid()
        self.mac1 = '9C:F6:DD:38:1F:35'
        self.mac2 = '9C:F6:DD:38:1F:5E'
        self.mac3 = '9C:F6:DD:38:1D:96'
        self.mac4 = '9C:F6:DD:38:1C:22'
        self.mac5 = '9C:F6:DD:38:1F:8E'
        self.mac6 = '9C:F6:DD:38:1F:DF'
        self.mac7 = '9C:F6:DD:38:1F:88'
        self.mac8 = '9C:F6:DD:38:1F:BE'
        self.mac9 = '9C:F6:DD:38:1D:A9'
        self.mac10 = '9C:F6:DD:38:1E:E2'
        self.mac11 = '9C:F6:DD:38:1D:A4'
        self.mac12 = '9C:F6:DD:39:29:D6'
        self.mac13 = '9C:F6:DD:39:29:D6'
        self.mac14 = '9C:F6:DD:39:29:D6'
        self.mac15 = '9C:F6:DD:39:29:D6'
        self.mac16 = '9C:F6:DD:3C:BC:8D'

    def smoke1(self):
        info = "Process-1"
        self.port = self.init_port
        self.systemPort = self.init_systemPort
        uuid = self.uuids[0]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        print   self.desired_cap
        time.sleep(10000)
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac1, self.section, info)
        rebort_cnts = []              #定义一个空列表
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        app.device_upslide()
        self.log.debug(info + "向上滑动成功")
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                    app.device_upslide()
                    self.log.debug(info + "向上滑动成功")
                self.log.debug(info + '心率运行次数：' + str(i))
                app.saturn_inputclick("160", "50", "160", "50")
                self.log.debug(info + "点击心率icon成功")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + "进入心率功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（心率-上级页面）")
            except:
                self.log.error(info + '心率在第N次运行失败：' + str(i))
                app.call_back(self.mac1, self.section, self.port, uuid, info)
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")

    def smoke2(self):
        info = "Process-2"
        self.port = int(self.init_port) + 2
        self.systemPort = int(self.init_systemPort) + 2
        uuid = self.uuids[1]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac2, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        app.device_upslide()
        self.log.debug(info + "向上滑动成功")
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                    app.device_upslide()
                    self.log.debug(info + "向上滑动成功")
                self.log.debug(info + '血氧运行次数：' + str(i))
                app.saturn_inputclick("270", "50", "270", "50")
                self.log.debug(info + "点击血氧icon成功")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + "进入血氧功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（血氧-上级页面）")
            except:
                self.log.error(info + '血氧在第N次运行失败：' + str(i))
                app.call_back(self.mac2, self.section, self.port, uuid, info)
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")

    def smoke3(self):
        info = "Process-3"
        self.port = int(self.init_port) + 4
        self.systemPort = int(self.init_systemPort) + 4
        uuid = self.uuids[1]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac3, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '进入各个应用运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("50", "50", "50", "50")
                self.log.debug(info + "点击活动icon成功")
                app.assert_getdevicepagename("activity")
                self.log.debug(info + "进入活动功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（活动-上级页面）")
                app.saturn_inputclick("160", "50", "160", "50")
                self.log.debug(info + "点击心率icon成功")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + "进入心率功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（心率-上级页面）")
                app.saturn_inputclick("270", "50", "270", "50")
                self.log.debug(info + "点击血氧icon成功")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + "进入血氧功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（血氧-上级页面）")
                app.saturn_inputclick("50", "160", "50", "160")
                self.log.debug(info + "点击睡眠icon成功")
                app.assert_getdevicepagename("sleep")
                self.log.debug(info + "进入睡眠功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（睡眠-上级页面）")
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + "点击运动icon成功")
                app.assert_getdevicepagename("sport_list")
                self.log.debug(info + "进入运动功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（运动-上级页面）")
                app.saturn_inputclick("270", "160", "270", "160")
                self.log.debug(info + "点击运动记录icon成功")
                app.assert_getdevicepagename("sports_record")
                self.log.debug(info + "进入运动记录功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（运动记录-上级页面）")
                app.saturn_inputclick("50", "270", "50", "270")
                self.log.debug(info + "点击闹钟icon成功")
                app.assert_getdevicepagename("alarm")
                self.log.debug(info + "进入闹钟功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（闹钟-上级页面）")
                app.saturn_inputclick("160", "270", "160", "270")
                self.log.debug(info + "点击天气icon成功")
                app.assert_getdevicepagename("weather")
                self.log.debug(info + "进入天气功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（天气-上级页面）")
                app.saturn_inputclick("270", "270", "270", "270")
                self.log.debug(info + "点击秒表icon成功")
                app.assert_getdevicepagename("appctr_stopwatch")
                self.log.debug(info + "进入秒表功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（秒表-上级页面）")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("50", "50", "50", "50")
                self.log.debug(info + "点击倒计时icon成功")
                app.assert_getdevicepagename("appctr_timer")
                self.log.debug(info + "进入倒计时功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（倒计时-上级页面）")
                app.saturn_inputclick("160", "50", "160", "50")
                self.log.debug(info + "点击音乐icon成功")
                app.assert_getdevicepagename("music")
                self.log.debug(info + "进入音乐功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（音乐-上级页面）")
                app.saturn_inputclick("270", "50", "270", "50")
                self.log.debug(info + "点击拍照icon成功")
                app.assert_getdevicepagename("camera")
                self.log.debug(info + "进入拍照功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（拍照-上级页面）")
                app.saturn_inputclick("50", "160", "50", "160")
                self.log.debug(info + "点击冥想icon成功")
                app.assert_getdevicepagename("meditation")
                self.log.debug(info + "进入冥想功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（冥想-上级页面）")
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + "点击查找手机icon成功")
                app.assert_getdevicepagename("findphone")
                self.log.debug(info + "进入查找手机功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（查找手机-上级页面）")
                app.saturn_inputclick("270", "160", "270", "160")
                self.log.debug(info + "点击设置icon成功")
                app.assert_getdevicepagename("iot_link")
                self.log.debug(info + "进入iot_link功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（iot_link-上级页面）")
                app.saturn_inputclick("50", "270", "50", "270")
                self.log.debug(info + "点击设置icon成功")
                app.assert_getdevicepagename("setting_page")
                self.log.debug(info + "进入设置功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（设置-上级页面）")
                app.device_home()
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '进出各个应用在第N次运行失败：' + str(i))
                app.call_back(self.mac3, self.section, self.port, uuid, info)


    def smoke4(self):
        info = "Process-4"
        self.port = int(self.init_port) + 6
        self.systemPort = int(self.init_systemPort) + 6
        uuid = self.uuids[3]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac4, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '运动中发送消息运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '点击运动icon成功')
                app.saturn_inputclick("160", "300", "160", "300")
                self.log.debug(info + '点击IndoorRun')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '点击Start')
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_send_notification('{"appMessage": {"appId": "app.wx", "text": "ryeex' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(info + '发送消息次数' + str(i))
                time.sleep(3)
                app.tv_send_notification('{"sms": {"contact": "ryeex' + str(i) + '", "content": "ryeex' + str(i) + '", "sender": ' + str(i) + '}, "type": "SMS"}')
                self.log.debug(info + '发短信次数' + str(i))
                time.sleep(3)
                app.tv_send_notification('{"telephony": {"contact": "ryeex' + str(i) + '", "number": ' + str(i) + ', "status": "RINGING_UNANSWERABLE"}, "type": "TELEPHONY"}')
                self.log.debug(info + '打电话次数' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.assert_getdevicepagename("remind")
                self.log.debug(info + '进入电话提醒页面成功')
                app.device_home()
                self.log.debug(info + '取消电话震动')
                app.assert_getdevicepagename("sports")
                self.log.debug(info + '退出电话震动页面成功')
                app.device_home()
                self.log.debug(info + '退出运动模式')
                app.saturn_inputclick("80", "160", "80", "160")
                self.log.debug(info + '点击Complete')
                app.saturn_inputclick("280", "280", "280", "280")
                self.log.debug(info + '点击确认')
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + '退出运动成功')
                app.device_home()
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '运动中发送消息在第N次运行失败：' + str(i))
                app.call_back(self.mac4, self.section, self.port, uuid, info)

    def smoke5(self):
        info = "Process-5"
        self.port = int(self.init_port) + 8
        self.systemPort = int(self.init_systemPort) + 8
        uuid = self.uuids[4]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac5, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '查看消息详情次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(info + '发送通知成功')
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.assert_getdevicepagename('remind')
                self.log.debug(info + '进入消息详情页面成功')
                app.device_home()
                self.log.debug(info + '返回主页面成功')
                app.assert_getdevicepagename("home_page")
                app.device_downslide()
                self.log.debug(info + '向下滑动成功')
                self.log.debug(info + "返回到消息页面")
                app.saturn_inputslide("160", "40", "160", "160")
                self.log.debug(info + '向下滑动一段距离')
                app.saturn_inputslide("160", "160", "160", "40")
                self.log.debug(info + '向上滑动一段距离')
                app.saturn_inputclick("160", "200", "160", "200")
                self.log.debug(info + '查看消息')
                app.assert_getdevicepagename('notification_box_detail')
                self.log.debug(info + '进入消息详情页面成功')
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page')
                self.log.debug(info + '退出消息页面成功')
                app.device_home()
                self.log.debug(info + '返回主页面成功')
            except:
                self.log.error(info + '查看消息在第N次运行失败：' + str(i))
                app.call_back(self.mac5, self.section, self.port, uuid, info)


    def smoke6(self):
        info = "Process-6"
        self.port = int(self.init_port) + 10
        self.systemPort = int(self.init_systemPort) + 10
        uuid = self.uuids[5]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac6, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '运动功能页面上下滑动次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '点击运动icon成功')
                app.assert_getdevicepagename('sport_list')
                self.log.debug(info + '进入运动应用成功')
                for j in range(1, 5):
                    app.device_upslide()
                    self.log.debug(info + '向上滑动成功')
                    app.device_upslide()
                    self.log.debug(info + '向上滑动成功')
                    app.device_upslide()
                    self.log.debug(info + '向上滑动成功')
                    app.device_upslide()
                    self.log.debug(info + '向上滑动成功')
                    app.device_downslide()
                    self.log.debug(info + '向下滑动成功')
                    app.device_downslide()
                    self.log.debug(info + '向下滑动成功')
                    app.device_downslide()
                    self.log.debug(info + '向下滑动成功')
                    app.device_downslide()
                    self.log.debug(info + '向下滑动成功')
                app.device_home()
                self.log.debug(info + "返回上级页面成功（运动-上级页面）")
                app.assert_getdevicepagename('home_page')
                self.log.debug(info + '退出运动应用成功')
                app.device_home()
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '运动功能页面上下滑动在第N次运行失败：' + str(i))
                app.call_back(self.mac6, self.section, self.port, uuid, info)


    def smoke7(self):
        info = "Process-7"
        self.port = int(self.init_port) + 12
        self.systemPort = int(self.init_systemPort) + 12
        uuid = self.uuids[6]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac7, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '血氧中发送消息次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("270", "50", "270", "50")
                self.log.debug(info + "点击血氧icon成功")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + "进入血氧功能成功")
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_send_notification('{"appMessage": {"appId": "app.wx", "text": "ryeex' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(info + '发送消息次数' + str(i))
                time.sleep(3)
                app.tv_send_notification('{"sms": {"contact": "ryeex' + str(i) + '", "content": "ryeex' + str(i) + '", "sender": ' + str(i) + '}, "type": "SMS"}')
                self.log.debug(info + '发短信次数' + str(i))
                time.sleep(3)
                app.tv_send_notification('{"telephony": {"contact": "ryeex' + str(i) + '", "number": ' + str(i) + ', "status": "RINGING_UNANSWERABLE"}, "type": "TELEPHONY"}')
                self.log.debug(info + '打电话次数' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.assert_getdevicepagename("remind")
                self.log.debug(info + '进入电话提醒页面成功')
                app.device_home()
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + '退出电话震动页面成功')
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + '退出血氧功能成功')
                app.device_home()
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '血氧中发送消息在第N次运行失败：' + str(i))
                app.call_back(self.mac7, self.section, self.port, uuid, info)

    def smoke8(self):
        info = "Process-8"
        self.port = int(self.init_port) + 14
        self.systemPort = int(self.init_systemPort) + 14
        uuid = self.uuids[7]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac8, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '切换表盘次数：' + str(i))
                for n in range(1, 6):
                    app.device_longpress()
                    self.log.debug(info + "进入切换表盘页面成功")
                    time.sleep(1)
                    app.device_rightslide()
                    self.log.debug(info + '向右滑动成功')
                    app.saturn_inputclick("160", "160", "160", "160")
                    self.log.debug(info + "点击表盘成功")
                    time.sleep(1)
                    app.assert_getdevicepagename("home_page")
                    self.log.debug(info + "退出切换表盘页面成功")
                for m in range(1, 6):
                    app.device_longpress()
                    self.log.debug(info + "进入切换表盘页面成功")
                    time.sleep(1)
                    app.device_leftslide()
                    self.log.debug(info + '向左滑动成功')
                    app.saturn_inputclick("160", "160", "160", "160")
                    self.log.debug(info + "点击表盘成功")
                    time.sleep(1)
                    app.assert_getdevicepagename("home_page")
                    self.log.debug(info + "退出切换表盘页面成功")
            except:
                self.log.error(info + '切换表盘在第N次运行失败：' + str(i))
                app.call_back(self.mac8, self.section, self.port, uuid, info)

    def smoke9(self):
        info = "Process-9"
        self.port = int(self.init_port) + 16
        self.systemPort = int(self.init_systemPort) + 16
        uuid = self.uuids[8]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac9, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '滑动屏幕次数：' + str(i))
                app.device_downslide()
                self.log.debug(info + '向下滑动成功')
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.device_leftslide()
                self.log.debug(info + "向上滑动成功")
                app.device_downslide()
                self.log.debug(info + '向下滑动成功')
                app.device_leftslide()
                self.log.debug(info + "向右滑动成功")
                app.device_leftslide()
                self.log.debug(info + "向左滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + "向左滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向右滑动成功")
            except:
                self.log.error(info + '滑动屏幕在第N次运行失败：' + str(i))
                app.call_back(self.mac9, self.section, self.port, uuid, info)

    def smoke10(self):
        info = "Process-10"
        self.port = int(self.init_port) + 18
        self.systemPort = int(self.init_systemPort) + 18
        uuid = self.uuids[9]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        self.driver = app.open_application(self.port)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '绑定解绑次数：' + str(i))
                app.devices_bind_ota(self.mac10, self.section, info)
                app.device_leftslide()
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                self.log.debug(info + "向左滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                self.log.debug(info + "向右滑动成功")
                if "page_name" in app.getresult():
                    self.log.debug(info + u'绑定成功')
                    if app.object_exist("解绑"):
                        app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
                    self.log.debug(info + u'解绑成功')
                    time.sleep(10)
                    self.driver.keyevent(4)
                    self.driver.keyevent(4)
                    time.sleep(20)
                    self.log.debug(info + u'等待设备重启成功')
                else:
                    self.log.error(info + u'绑定失败')
            except:
                self.log.error(info + u'绑定解绑在第N次运行失败：' + str(i))
                if app.object_exist(u"绑定失败"):
                    self.log.error(info + u'绑定失败')
                    self.driver.keyevent(4)
                # self.driver.quit()
                # self.log.debug(info + '结束IDT进程')
                # time.sleep(5)
                self.driver = app.open_application(self.port)
                self.log.debug(info + '启动IDT')
                self.log.debug(info + '-----------异常处理结束----------')


    def smoke11(self):
        info = "Process-11"
        self.port = int(self.init_port) + 20
        self.systemPort = int(self.init_systemPort) + 20
        uuid = self.uuids[10]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        self.driver = app.open_application(self.port)
        app.devices_bind(self.mac11, self.section, info)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '重启次数：' + str(i))
                app.device_reboot()
                time.sleep(60)
            except:
                self.log.error(info + '重启在第N次运行失败：' + str(i))
                app.call_back(self.mac11, self.section, self.port, uuid, info)

    def smoke12(self):
        info = "Process-12"
        self.port = int(self.init_port) + 22
        self.systemPort = int(self.init_systemPort) + 22
        uuid = self.uuids[11]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac12, self.section, info)
        size = driver.get_window_size()
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '安装表盘发送消息次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_installSurface("10001,STATIC")       #这里安装表盘的参数已经写死了
                self.log.debug(info + '安装表盘')
                app.tv_send_notification1('{"appMessage": {"appId": "app.wx", "text": "1ryeex' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                for j in range(1, 10):
                    app.tv_send_notification2()
                    self.log.debug(info + '发送消息')
                time.sleep(30)
                app.tv_deleteSurface(9568)
                self.log.debug(info + '删除表盘')
                driver.keyevent(4)
            except:
                self.log.error(info + '安装表盘发送消息在第N次运行失败：' + str(i))
                app.call_back(self.mac12, self.section, self.port, uuid, info)

    def smoke13(self):
        info = "Process-13"
        self.port = int(self.init_port) + 24
        self.systemPort = int(self.init_systemPort) + 24
        uuid = self.uuids[12]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind_ota(self.mac13, self.section, info)
        size = driver.get_window_size()
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '安装表盘断开蓝牙次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_installSurface("10001,STATIC")       #这里表盘的参数已经写死了
                self.log.debug(info + '安装表盘')
                time.sleep(10)
                app.tv_bluetoothcontrol()
                self.log.debug(info + '断开蓝牙')
                app.tv_bluetoothcontrol()
                self.log.debug(info + '打开蓝牙')
                time.sleep(60)
                if app.object_exist('SATURN_APP'):
                    app.devices_click('SATURN_APP')
                app.connect_status()
                app.devices_installsurface("10001,STATIC")       #这里表盘的参数已经写死了
                self.log.debug(info + '重新安装表盘')
                app.tv_deleteSurface("10001,STATIC")       #这里表盘的参数已经写死了
                self.log.debug(info + '删除表盘')
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.device_longpress()
                self.log.debug(info + '长按')
                app.device_rightslide()
                self.log.debug(info + '打开右滑')
                app.saturn_inputclick('160', '160', '160', '160')
                self.log.debug(info + '选择表盘')
            except:
                self.log.error(info + '安装表盘断开蓝牙在第N次运行失败：' + str(i))
                app.call_back(self.mac13, self.section, self.port, uuid, info)

    def smoke14(self):
        info = "Process-14"
        self.port = int(self.init_port) + 26
        self.systemPort = int(self.init_systemPort) + 26
        uuid = self.uuids[13]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac14, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '进出运动（室内）次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '点击运动icon成功')
                app.assert_getdevicepagename('sport_list')
                self.log.debug(info + '进入运动应用成功')
                app.saturn_inputclick("160", "300", "160", "300")
                self.log.debug(info + '选择室内运动')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '点击Start')
                time.sleep(200)
                app.device_home()
                app.saturn_inputclick("800", "160", "800", "160")
                self.log.debug(info + '点击停止运动')
                app.device_home()
                app.device_home()
                self.log.debug(info + '返回表盘页面')
            except:
                self.log.error(info + '运动功能页面上下滑动在第N次运行失败：' + str(i))
                app.call_back(self.mac14, self.section, self.port, uuid, info)

    def smoke15(self):
        info = "Process-15"
        self.port = int(self.init_port) + 28
        self.systemPort = int(self.init_systemPort) + 28
        uuid = self.uuids[14]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac15, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        dial_list = [10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026]
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '循环安装表盘次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                for m in range(0, 10):
                    app.tv_installSurface(str(dial_list[m])+",STATIC")
                    self.log.debug(info + '安装表盘:' + dial_list[m])
            except:
                self.log.error(info + '循环安装表盘在第N次运行失败：' + str(i))
                app.call_back(self.mac15, self.section, self.port, uuid, info)

    def smoke16(self):
        surface_list=[]
        for num in range(10001,65535):
            # if 20001<=num<20021:
            if 10001<=num<10102 or 20001<=num<20021 or 65530<=num<65535:
                surface_list.append(num)
        print('表盘一共有：{} 个'.format(len(surface_list)))
        surface_num=0
        info = "Process-16"
        self.port = int(self.init_port) + 26
        self.systemPort = int(self.init_systemPort) + 26
        uuid = self.uuids[0]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)


        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac16, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])

        for i in range(1, 10000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                app.get_rebort_cnts(rebort_cnts, info)
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    print('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    print('SATURN_设备')
                    app.call_back_devices_init(info)
                self.log.debug(info + '安装表盘次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                print('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                if surface_num >len(surface_list):
                    surface_num=0
                # app.tv_installSurface(surface_list[surface_num])
                if 10001 <= surface_list[surface_num] < 10102 or 65530 <= surface_list[surface_num] < 65535:
                    watch_surface=str(surface_list[surface_num])+",STATIC"
                    print(watch_surface)
                    app.devices_installsurface(watch_surface)
                elif 20001 <= surface_list[surface_num] < 20021:
                    watch_surface = str(surface_list[surface_num]) + ",DYNAMIC"
                    print(watch_surface)
                    app.devices_installsurface(watch_surface)

                self.log.debug(info+"安装表盘结束")
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                print("现在安装的表盘id为:{}".format(surface_list[surface_num]))
                surface_num += 1
                print("第{}次安装结束".format(surface_num))
                print()
            except:
                self.log.error(info + '安装表盘在第N次运行失败：' + str(i))
                app.call_back(self.mac16, self.section, self.port, uuid, info)
                surface_num += 1
                print()


if __name__ == '__main__':
    multiprocessings = []
    t1 = multiprocessing.Process(target=Testsmoke().smoke1)
    t2 = multiprocessing.Process(target=Testsmoke().smoke2)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke3)
    # t4 = multiprocessing.Process(target=Testsmoke().smoke4)
    # t5 = multiprocessing.Process(target=Testsmoke().smoke5)
    # t6 = multiprocessing.Process(target=Testsmoke().smoke6)
    # t7 = multiprocessing.Process(target=Testsmoke().smoke7)
    # t8 = multiprocessing.Process(target=Testsmoke().smoke8)
    # t9 = multiprocessing.Process(target=Testsmoke().smoke9)
    # t10 = multiprocessing.Process(target=Testsmoke().smoke10)
    # t11 = multiprocessing.Process(target=Testsmoke().smoke11)
    # t12 = multiprocessing.Process(target=Testsmoke().smoke12)
    t16=multiprocessing.Process(target=Testsmoke().smoke16)

    # multiprocessings.append(t1)
    # multiprocessings.append(t2)
    # multiprocessings.append(t3)
    # multiprocessings.append(t4)
    # multiprocessings.append(t5)
    # multiprocessings.append(t6)
    # multiprocessings.append(t7)
    # multiprocessings.append(t8)
    # multiprocessings.append(t9)
    # multiprocessings.append(t10)
    # multiprocessings.append(t11)
    # multiprocessings.append(t12)
    multiprocessings.append(t16)
    for t in multiprocessings:
        t.start()

