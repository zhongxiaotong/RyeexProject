#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 22:00
# @Author : Greey
# @FileName: Saturn_Smoke.py

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
        self.mac1 = 'CC:CC:CC:CC:BB:E5'
        self.mac2 = 'CC:CC:CC:CC:BB:E5'
        self.mac3 = 'CC:CC:CC:CC:BB:E5'
        self.mac4 = 'CC:CC:CC:CC:BB:E5'
        self.mac5 = 'CC:CC:CC:CC:BB:E5'
        self.mac6 = 'CC:CC:CC:CC:BB:E5'
        self.mac7 = 'CC:CC:CC:CC:BB:E5'
        self.mac8 = 'CC:CC:CC:CC:BB:E5'
        self.mac9 = 'CC:CC:CC:CC:BB:E5'
        self.mac10 = 'CC:CC:CC:CC:BB:E5'
        self.mac11 = 'CC:CC:CC:CC:BB:E5'
        self.mac12 = 'CC:CC:CC:CC:BB:E5'
        self.mac13 = 'CC:CC:CC:CC:BB:E5'
        self.mac14 = 'CC:CC:CC:CC:BB:E5'
        self.mac15 = '2C:AA:8E:09:D1:31'
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
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac1, self.section, info)
        app.devices_baileys_init(info)
        rebort_cnts = []              #定义一个空列表
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        app.device_upslide()
        app.assert_getdevicepagename('home_page', 'home_id_down')
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
                    app.call_back_devices_baileys_init(info)
                    app.device_upslide()
                    app.assert_getdevicepagename('home_page', 'home_id_down')
                    self.log.debug(info + "向上滑动成功")
                self.log.debug(info + '心率运行次数：' + str(i))
                app.saturn_inputclick("180", "50", "180", "50")
                self.log.debug(info + "点击心率icon成功")
                # app.assert_getdevicepagename("hrm", "view_record")
                self.log.debug(info + "进入心率功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（心率-上级页面）")
            except:
                self.log.error(info + '心率在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac1, self.section, self.port, uuid, info)
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "向上滑动成功")

    def smoke2(self):
        info = "Process-2"
        self.port = int(self.init_port) + 2
        self.systemPort = int(self.init_systemPort) + 2
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
        app.devices_bind(self.mac2, self.section, info)
        app.devices_baileys_init(info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        app.device_upslide()
        app.assert_getdevicepagename('home_page', 'home_id_down')
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
                    app.call_back_devices_baileys_init(info)
                    app.device_upslide()
                    app.assert_getdevicepagename('home_page', 'home_id_down')
                    self.log.debug(info + "向上滑动成功")
                self.log.debug(info + '血氧运行次数：' + str(i))
                app.saturn_inputclick("300", "50", "300", "50")
                self.log.debug(info + "点击血氧icon成功")
                # app.assert_getdevicepagename("spo2", "view_measure")
                self.log.debug(info + "进入血氧功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（血氧-上级页面）")
            except:
                self.log.error(info + '血氧在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac2, self.section, self.port, uuid, info)
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "向上滑动成功")

    def smoke3(self):
        info = "Process-3"
        self.port = int(self.init_port) + 4
        self.systemPort = int(self.init_systemPort) + 4
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
        app.devices_bind(self.mac3, self.section, info)
        app.devices_baileys_init(info)
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
                    app.call_back_devices_baileys_init(info)
                self.log.debug(info + '进入各个应用运行次数：' + str(i))
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("50", "50", "50", "50")
                self.log.debug(info + "点击活动icon成功")
                app.assert_getdevicepagename("activity", "list_view")
                self.log.debug(info + "进入活动功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（活动-上级页面）")
                app.saturn_inputclick("180", "50", "180", "50")
                self.log.debug(info + "点击心率icon成功")
                # app.assert_getdevicepagename("hrm", "view_record")
                self.log.debug(info + "进入心率功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（心率-上级页面）")
                app.saturn_inputclick("300", "50", "300", "50")
                self.log.debug(info + "点击血氧icon成功")
                # app.assert_getdevicepagename("spo2", "view_measure")
                self.log.debug(info + "进入血氧功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（血氧-上级页面）")
                app.saturn_inputclick("50", "170", "50", "170")
                self.log.debug(info + "点击睡眠icon成功")
                app.assert_getdevicepagename("sleep", "view_no_data")
                self.log.debug(info + "进入睡眠功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（睡眠-上级页面）")
                app.saturn_inputclick("180", "180", "180", "180")
                self.log.debug(info + "点击运动icon成功")
                app.assert_getdevicepagename("sport_list", "view_all_type")
                self.log.debug(info + "进入运动功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（运动-上级页面）")
                app.saturn_inputclick("300", "180", "300", "180")
                self.log.debug(info + "点击运动记录icon成功")
                app.assert_getdevicepagename("sports_record", "view_no_data")
                self.log.debug(info + "进入运动记录功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（运动记录-上级页面）")
                app.saturn_inputclick("50", "280", "50", "280")
                self.log.debug(info + "点击冥想icon成功")
                app.assert_getdevicepagename("meditation", "view_start")
                self.log.debug(info + "进入冥想功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（冥想-上级页面）")
                app.saturn_inputclick("180", "280", "180", "280")
                self.log.debug(info + "点击秒表icon成功")
                app.assert_getdevicepagename("alarm", "view_empty")
                self.log.debug(info + "进入秒表功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（秒表-上级页面）")
                app.saturn_inputclick("300", "280", "300", "280")
                self.log.debug(info + "点击天气icon成功")
                app.assert_getdevicepagename("weather", "offline_weather")
                self.log.debug(info + "进入天气功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（天气-上级页面）")
                app.saturn_inputclick("50", "400", "50", "400")
                self.log.debug(info + "点击秒表icon成功")
                app.assert_getdevicepagename("appctr_stopwatch", "view_start")
                self.log.debug(info + "进入秒表功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（秒表-上级页面）")
                app.saturn_inputclick("180", "400", "180", "400")
                self.log.debug(info + "点击倒计时icon成功")
                app.assert_getdevicepagename("appctr_timer", "label_timer/list_view")
                self.log.debug(info + "进入倒计时功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（倒计时-上级页面）")
                app.saturn_inputclick("300", "400", "300", "400")
                self.log.debug(info + "点击音乐icon成功")
                app.assert_getdevicepagename("music", "online_music")
                self.log.debug(info + "进入音乐功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（音乐-上级页面）")
                app.device_upslide()
                app.saturn_inputclick("50", "400", "50", "400")
                self.log.debug(info + "点击拍照icon成功")
                app.assert_getdevicepagename("camera", "view_camera_home")
                self.log.debug(info + "进入拍照功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（拍照-上级页面）")
                app.saturn_inputclick("180", "400", "180", "400")
                self.log.debug(info + "点击查找手机icon成功")
                app.assert_getdevicepagename("findphone", "view_online")
                self.log.debug(info + "进入查找手机功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "返回上级页面成功（查找手机-上级页面）")
                app.saturn_inputclick("300", "400", "300", "400")
                self.log.debug(info + "点击设置icon成功")
                app.assert_getdevicepagename("setting_page", "list_view")
                self.log.debug(info + "进入设置功能成功")
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                app.device_home()
                self.log.debug(info + "返回主页面")
                app.assert_getdevicepagename('home_page', 'home_id_surface')
            except:
                self.log.error(info + '进出各个应用在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac3, self.section, self.port, uuid, info)


    def smoke4(self):
        info = "Process-4"
        self.port = int(self.init_port) + 6
        self.systemPort = int(self.init_systemPort) + 6
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
        app.devices_bind(self.mac4, self.section, info)
        app.devices_baileys_init(info)
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
                    app.call_back_devices_baileys_init(info)
                self.log.debug(info + '运动中发送消息运行次数：' + str(i))
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("180", "180", "180", "180")
                app.assert_getdevicepagename("sport_list", "view_all_type")
                self.log.debug(info + '点击运动icon成功')
                app.saturn_inputclick("180", "230", "180", "230")
                app.assert_getdevicepagename("sport_list", "view_gps_start")
                self.log.debug(info + '点击IndoorRun')
                app.saturn_inputclick("180", "230", "180", "230")
                time.sleep(3)
                app.assert_getdevicepagename("sports", "view_calculate_show")
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
                app.assert_getdevicepagename("remind", "view_call")
                self.log.debug(info + '进入电话提醒页面成功')
                app.device_home()
                self.log.debug(info + '取消电话震动')
                app.assert_getdevicepagename("sports", "view_calculate_show")
                self.log.debug(info + '退出电话震动页面成功')
                app.device_home()
                app.assert_getdevicepagename("sports", "view_pause")
                self.log.debug(info + '退出运动模式')
                app.saturn_inputclick("90", "230", "90", "230")
                self.log.debug(info + '点击Complete')
                app.assert_getdevicepagename("sports", "view_end_confirm")
                app.saturn_inputclick("300", "400", "300", "400")
                self.log.debug(info + '点击确认')
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '退出运动成功')
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '运动中发送消息在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac4, self.section, self.port, uuid, info)

    def smoke5(self):
        info = "Process-5"
        self.port = int(self.init_port) + 8
        self.systemPort = int(self.init_systemPort) + 8
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
                    # app.call_back_devices_baileys_init(info)
                self.log.debug(info + '查看消息详情次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i+1) + '", "title": ' + str(i+1) + '}, "type": "APP_MESSAGE"}')
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i+2) + '", "title": ' + str(i+2) + '}, "type": "APP_MESSAGE"}')
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i+3) + '", "title": ' + str(i+3) + '}, "type": "APP_MESSAGE"}')
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i+4) + '", "title": ' + str(i+4) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(info + '发送通知成功')
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.assert_getdevicepagename("remind", "view_app_notify")
                self.log.debug(info + '进入消息详情页面成功')
                app.device_home()
                self.log.debug(info + '返回主页面成功')
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                app.device_downslide()
                self.log.debug(info + '向下滑动成功,返回到消息页面')
                app.assert_getdevicepagename('home_page', 'home_id_up')
                app.saturn_inputslide("180", "40", "180", "400")
                self.log.debug(info + '向下滑动一段距离')
                app.saturn_inputslide("180", "400", "180", "40")
                self.log.debug(info + '向上滑动一段距离')
                app.saturn_inputclick("180", "230", "180", "230")
                self.log.debug(info + '查看消息')
                app.assert_getdevicepagename('notification_box_detail', 'list_view')
                self.log.debug(info + '进入消息详情页面成功')
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page', 'home_id_up')
                self.log.debug(info + '退出消息页面成功')
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + '返回主页面成功')
            except:
                self.log.error(info + '查看消息在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac5, self.section, self.port, uuid, info)


    def smoke6(self):
        info = "Process-6"
        self.port = int(self.init_port) + 10
        self.systemPort = int(self.init_systemPort) + 10
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
        app.devices_bind(self.mac6, self.section, info)
        app.devices_baileys_init(info)
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
                    app.call_back_devices_baileys_init(info)
                self.log.debug(info + '运动功能页面上下滑动次数：' + str(i))
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("180", "180", "180", "180")
                self.log.debug(info + '点击运动icon成功')
                app.assert_getdevicepagename('sport_list', 'view_all_type')
                self.log.debug(info + '进入运动应用成功')
                for j in range(1, 5):
                    app.device_upslide()
                    self.log.debug(info + '向上滑动成功')
                    app.device_upslide()
                    self.log.debug(info + '向上滑动成功')
                    # app.device_upslide()
                    # self.log.debug(info + '向上滑动成功')
                    # app.device_downslide()
                    # self.log.debug(info + '向下滑动成功')
                    app.device_downslide()
                    self.log.debug(info + '向下滑动成功')
                    app.device_downslide()
                    self.log.debug(info + '向下滑动成功')
                app.device_home()
                self.log.debug(info + "返回上级页面成功（运动-上级页面）")
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '退出运动应用成功')
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '运动功能页面上下滑动在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac6, self.section, self.port, uuid, info)


    def smoke7(self):
        info = "Process-7"
        self.port = int(self.init_port) + 12
        self.systemPort = int(self.init_systemPort) + 12
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
        app.devices_bind(self.mac7, self.section, info)
        app.devices_baileys_init(info)
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
                    app.call_back_devices_baileys_init(info)
                self.log.debug(info + '血氧中发送消息次数：' + str(i))
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("300", "50", "300", "50")
                self.log.debug(info + "点击血氧icon成功")
                # app.assert_getdevicepagename("spo2", "view_measure")
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
                app.assert_getdevicepagename('remind', 'view_call')
                self.log.debug(info + '进入电话提醒页面成功')
                app.device_home()
                # app.assert_getdevicepagename("spo2", "view_measure")
                self.log.debug(info + '退出电话震动页面成功')
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '退出血氧功能成功')
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '血氧中发送消息在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac7, self.section, self.port, uuid, info)

    def smoke8(self):
        info = "Process-8"
        self.port = int(self.init_port) + 14
        self.systemPort = int(self.init_systemPort) + 14
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
        app.devices_bind(self.mac8, self.section, info)
        app.devices_baileys_init(info)
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
                    # app.call_back_devices_baileys_init(info)
                self.log.debug(info + '切换表盘次数：' + str(i))
                for n in range(1, 4):
                    app.device_longpress()
                    app.assert_getdevicepagename('face_pick_page', 'slide_view_view')
                    self.log.debug(info + "进入切换表盘页面成功")
                    time.sleep(1)
                    app.device_leftslide()
                    self.log.debug(info + '向左滑动成功')
                    app.saturn_inputclick("160", "160", "160", "160")
                    self.log.debug(info + "点击表盘成功")
                    time.sleep(1)
                    app.assert_getdevicepagename('home_page', 'home_id_surface')
                    self.log.debug(info + "退出切换表盘页面成功")
                for m in range(1, 4):
                    app.device_longpress()
                    app.assert_getdevicepagename('face_pick_page', 'slide_view_view')
                    self.log.debug(info + "进入切换表盘页面成功")
                    time.sleep(1)
                    app.device_rightslide()
                    self.log.debug(info + '向右滑动成功')
                    app.saturn_inputclick("160", "160", "160", "160")
                    self.log.debug(info + "点击表盘成功")
                    time.sleep(1)
                    app.assert_getdevicepagename('home_page', 'home_id_surface')
                    self.log.debug(info + "退出切换表盘页面成功")
            except:
                self.log.error(info + '切换表盘在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac8, self.section, self.port, uuid, info)

    def smoke9(self):
        info = "Process-9"
        self.port = int(self.init_port) + 16
        self.systemPort = int(self.init_systemPort) + 16
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
        app.devices_bind(self.mac9, self.section, info)
        app.devices_baileys_init(info)
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
                    # app.call_back_devices_baileys_init(info)
                self.log.debug(info + '滑动屏幕次数：' + str(i))
                app.device_downslide()
                app.assert_getdevicepagename('home_page', 'home_id_up')
                self.log.debug(info + '向下滑动成功')
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + "向上滑动成功")
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + "向上滑动成功")
                app.device_downslide()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + '向下滑动成功')
                app.device_rightslide()
                app.assert_getdevicepagename('home_page', 'home_id_left')
                self.log.debug(info + "向右滑动成功")
                app.device_leftslide()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_0')
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_1')
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_2')
                self.log.debug(info + "向左滑动成功")
                app.device_leftslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_3')
                self.log.debug(info + "向左滑动成功")
                app.device_rightslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_2')
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_1')
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                app.assert_getdevicepagename('home_page', 'home_id_right_0')
                self.log.debug(info + "向右滑动成功")
                app.device_rightslide()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + "向右滑动成功")
            except:
                self.log.error(info + '滑动屏幕在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac9, self.section, self.port, uuid, info)

    def smoke10(self):
        info = "Process-10"
        self.port = int(self.init_port) + 18
        self.systemPort = int(self.init_systemPort) + 18
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
        self.driver = app.open_application(self.port)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '绑定解绑次数：' + str(i))
                self.driver1 = app.devices_bind(self.mac10, self.section, info)
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
                app.devices_click('解绑')
                self.log.debug(info + u'解绑成功')
                time.sleep(10)
                self.driver1.keyevent(4)
                self.driver1.keyevent(4)
                time.sleep(30)
                self.log.debug(info + u'等待设备重启')
            except:
                self.log.error(info + u'绑定解绑在第N次运行失败：' + str(i))
                if app.object_exist(u"绑定失败"):
                    self.log.error(info + u'绑定失败')
                self.driver1 = app.open_application(self.port)
                self.log.debug(info + '启动IDT')


    def smoke11(self):
        info = "Process-11"
        self.port = int(self.init_port) + 20
        self.systemPort = int(self.init_systemPort) + 20
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
        self.driver = app.open_application(self.port)
        app.devices_bind(self.mac11, self.section, info)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '重启次数：' + str(i))
                app.device_reboot()
                time.sleep(60)
            except:
                self.log.error(info + '重启在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac11, self.section, self.port, uuid, info)

    def smoke12(self):
        info = "Process-12"
        self.port = int(self.init_port) + 22
        self.systemPort = int(self.init_systemPort) + 22
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
        self.driver = app.open_application(self.port)
        app.devices_bind(self.mac12, self.section, info)
        size = self.driver.get_window_size()
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
                    self.driver.keyevent(4)
                    app.devices_click('SATURN_APP')
                    app.tv_getDevicesLog()
                    app.adb_pull(uuid, info)
                    self.driver.keyevent(4)
                    app.devices_click('SATURN_设备')
                    # app.call_back_devices_baileys_init(info)
                self.log.debug(info + '安装表盘发送消息次数：' + str(i))
                self.driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_installSurface()
                self.log.debug(info + '安装表盘')
                app.tv_send_notification1('{"appMessage": {"appId": "app.wx", "text": "1ryeex' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                for j in range(1, 10):
                    app.tv_send_notification2()
                    self.log.debug(info + '发送消息')
                time.sleep(30)
                app.tv_deleteSurface()
                self.log.debug(info + '删除表盘')
                self.driver.keyevent(4)
                app.devices_click('SATURN_设备')
            except:
                self.log.error(info + '安装表盘发送消息在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac12, self.section, self.port, uuid, info)

    def smoke13(self):
        info = "Process-13"
        self.port = int(self.init_port) + 24
        self.systemPort = int(self.init_systemPort) + 24
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
        app.devices_bind(self.mac13, self.section, info)
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
                    # app.call_back_devices_baileys_init(info)
                self.log.debug(info + '安装表盘断开蓝牙次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_installSurface()
                self.log.debug(info + '安装表盘')
                time.sleep(10)
                app.tv_bluetoothcontrol()
                app.click_prompt_box()
                self.log.debug(info + '断开蓝牙')
                app.tv_bluetoothcontrol()
                app.click_prompt_box()
                self.log.debug(info + '打开蓝牙')
                time.sleep(30)
                if app.object_exist('SATURN_APP'):
                    app.devices_click('SATURN_APP')
                app.connect_status()
                app.devices_installsurface()
                self.log.debug(info + '重新安装表盘')
                time.sleep(10)
                app.tv_deleteSurface()
                self.log.debug(info + '删除表盘')
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.device_longpress()
                app.assert_getdevicepagename("face_pick_page", "slide_view_view")
                self.log.debug(info + '长按')
                app.device_rightslide()
                self.log.debug(info + '打开右滑')
                app.saturn_inputclick('160', '160', '160', '160')
                self.log.debug(info + '选择表盘')
            except:
                self.log.error(info + '安装表盘断开蓝牙在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac13, self.section, self.port, uuid, info)

    def smoke14(self):
        info = "Process-14"
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
        app.devices_bind(self.mac14, self.section, info)
        # app.devices_baileys_init(info)
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
                    app.call_back_devices_baileys_init(info)
                self.log.debug(info + '进出运动（室内）次数：' + str(i))
                app.device_upslide()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("180", "180", "180", "180")
                app.assert_getdevicepagename("sport_list", "view_all_type")
                self.log.debug(info + '点击运动icon成功')
                app.device_upslide()
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("180", "100", "180", "100")
                app.assert_getdevicepagename("sport_list", "view_gps_start")
                self.log.debug(info + '点击力量训练')
                app.saturn_inputclick("180", "230", "180", "230")
                time.sleep(3)
                app.assert_getdevicepagename("sports", "view_calculate_show")
                self.log.debug(info + '点击Start')
                time.sleep(150)
                app.device_home()
                app.assert_getdevicepagename("sports", "view_pause")
                self.log.debug(info + '退出运动模式')
                app.saturn_inputclick("90", "230", "90", "230")
                self.log.debug(info + '点击Complete')
                app.assert_getdevicepagename("sports", "view_result_show")
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_down')
                app.device_home()
                app.assert_getdevicepagename('home_page', 'home_id_surface')
                self.log.debug(info + '返回表盘页面')
            except:
                self.log.error(info + '进出运动（室内）在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac14, self.section, self.port, uuid, info)


    def smoke15(self):
        info = "Process-15"
        self.port = int(self.init_port) + 28
        self.systemPort = int(self.init_systemPort) + 28
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
        app.devices_bind(self.mac15, self.section, info)
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
                    app.call_back_devices_baileys_init(info)
                self.log.debug(info + '亮屏次数：' + str(i))
                app.device_upslide()
                app.device_home()
                app.assert_deviceisscreen(1)
                time.sleep(3)
                app.assert_deviceisscreen(0)
            except:
                self.log.error(info + '亮屏在第N次运行失败：' + str(i))
                app.call_back_baileys(self.mac15, self.section, self.port, uuid, info)

if __name__ == '__main__':
    multiprocessings = []
    t1 = multiprocessing.Process(target=Testsmoke().smoke1)
    # t2 = multiprocessing.Process(target=Testsmoke().smoke2)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke3)
    multiprocessings.append(t1)
    # multiprocessings.append(t2)
    # multiprocessings.append(t3)
    for t in multiprocessings:
        t.start()

