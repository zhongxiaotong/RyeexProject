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
        self.log.info('初始化测试数据')
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.init_port = 4723
        self.init_systemPort = 8200
        self.section = 'SATURN_设备'
        # self.mac1 = '9C:F6:DD:38:1F:88'
        # self.mac2 = '9C:F6:DD:38:1F:8E'
        # self.mac10 = '9C:F6:DD:38:1E:E2'
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
        self.mac12 = '9C:F6:DD:38:1F:DF'
    def smoke1(self):
        info = "Process-1"
        self.port = self.init_port
        self.systemPort = self.init_systemPort
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[0]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        app.open_application(self.port)
        app.devices_bind(self.mac1, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                # count = 0
                # while True:
                #     if "reboot_cnt" in app.getresult():
                #         rebort_cnts.append(app.getdevice()[2])
                #         self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                #         break
                #     else:
                #         count += 1
                #         time.sleep(1)
                #         self.log.debug(info + "获取重启次数失败，继续获取")
                #         if count >= 15:
                #             raise(info + "获取重启次数超时")
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                # print("rebort_cnts:" + str(rebort_cnts))
                # print(str(rebort_cnts[i]))
                # print(str(rebort_cnts[i-1]))
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    app.call_back_devices_init(info)
                self.log.debug(info + '心率运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("160", "50", "160", "50")
                self.log.debug(info + "点击心率icon成功")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + "进入心率功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（心率-上级页面）")
                app.device_home()
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '心率在第N次运行失败：' + str(i))
                app.call_back(self.mac1, self.section, self.port, self.uuid, info)
    def smoke2(self):
        info = "Process-2"
        self.port = int(self.init_port) + 2
        self.systemPort = int(self.init_systemPort) + 2
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[1]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        app.open_application(self.port)
        app.devices_bind(self.mac2, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                # print("rebort_cnts:" + str(rebort_cnts))
                # print(str(rebort_cnts[i]))
                # print(str(rebort_cnts[i-1]))
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    app.call_back_devices_init(info)
                self.log.debug(info + '血氧运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("270", "50", "270", "50")
                self.log.debug(info + "点击血氧icon成功")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + "进入血氧功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回上级页面成功（血氧-上级页面）")
                app.device_home()
                self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '血氧在第N次运行失败：' + str(i))
                app.call_back(self.mac2, self.section, self.port, self.uuid, info)

    def smoke3(self):
        info = "Process-3"
        print(info)
        self.port = int(self.init_port) + 4
        self.systemPort = int(self.init_systemPort) + 4
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[2]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        app.open_application(self.port)
        app.devices_bind(self.mac3, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
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
                app.call_back(self.mac3, self.section, self.port, self.uuid, info)


    def smoke4(self):
        info = "Process-4"
        self.port = int(self.init_port) + 6
        self.systemPort = int(self.init_systemPort) + 6
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[3]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(self.mac4, self.section, info)
        i = 0
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    app.call_back_devices_init(info)
                self.log.debug(info + '运动中发送消息运行次数：' + str(i))
                app.device_upslide()
                self.log.debug(info + '向上滑动成功')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '点击运动icon成功')
                # app.assert_getdevicepagename('sport_list')
                # self.log.debug(info + '进入运动应用成功')
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
                app.call_back(self.mac4, self.section, self.port, self.uuid, info)

    def smoke5(self):
        info = "Process-5"
        self.port = int(self.init_port) + 8
        self.systemPort = int(self.init_systemPort) + 8
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[4]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
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
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
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
                app.call_back(self.mac5, self.section, self.port, self.uuid, info)

    def smoke6(self):
        info = "Process-6"
        print(info)
        self.port = int(self.init_port) + 10
        self.systemPort = int(self.init_systemPort) + 10
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[5]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
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
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
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
                app.call_back(self.mac6, self.section, self.port, self.uuid, info)


    def smoke7(self):
        info = "Process-7"
        self.port = int(self.init_port) + 12
        self.systemPort = int(self.init_systemPort) + 12
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[6]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
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
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
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
                app.call_back(self.mac7, self.section, self.port, self.uuid, info)

    def smoke8(self):
        info = "Process-8"
        self.port = int(self.init_port) + 14
        self.systemPort = int(self.init_systemPort) + 14
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[3]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
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
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    app.call_back_devices_init(info)
                # print("frist:" + rebort_cnts[i-1])
                # print("second:" + rebort_cnts[i])
                # print("rebort_cnts:" + str(rebort_cnts))
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
                # app.device_upslide()
                # self.log.debug(info + '向上滑动成功')
                # app.saturn_inputclick("270", "50", "270", "50")
                # self.log.debug(info + "点击血氧icon成功")
                # app.assert_getdevicepagename("spo2")
                # self.log.debug(info + "进入血氧功能成功")
                # app.device_home()
                # app.device_home()
                # self.log.debug(info + "返回主页面")
            except:
                self.log.error(info + '切换表盘在第N次运行失败：' + str(i))
                app.call_back(self.mac8, self.section, self.port, self.uuid, info)

    def smoke9(self):
        info = "Process-9"
        self.port = int(self.init_port) + 16
        self.systemPort = int(self.init_systemPort) + 16
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[4]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
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
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
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
                app.call_back(self.mac9, self.section, self.port, self.uuid, info)

    def smoke10(self):
        info = "Process-10"
        self.port = int(self.init_port) + 18
        self.systemPort = int(self.init_systemPort) + 18
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[0]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        # app.devices_bind(self.mac10, self.section, info)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '绑定解绑次数：' + str(i))
                app.devices_bind_ota(self.mac10, self.section, info, self.port, self.uuid)
                app.device_clickDID()
                self.log.debug(info + u'获取设备标识')
                if "page_name" in app.getresult():
                    self.log.debug(info + u'绑定成功')
                    if app.object_exist("解绑"):
                        app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
                    self.log.debug(info + u'解绑成功')
                    app.implicitly_wait("realme Watch 2", 60)
                    driver.keyevent(4)
                    driver.keyevent(4)
                    time.sleep(20)
                    self.log.debug(info + u'等待设备重启成功')
                else:
                    self.log.error(info + u'绑定失败')
            except:
                self.log.error(info + u'绑定解绑在第N次运行失败：' + str(i))
                if app.object_exist("绑定失败"):
                    self.log.error(info + '绑定失败')
                    driver.keyevent(4)
                self.log.debug(info + '异常处理----------')


    def smoke11(self):
        info = "Process-11"
        self.port = int(self.init_port) + 20
        self.systemPort = int(self.init_systemPort) + 20
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[1]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        # app.devices_bind(self.mac10, self.section, info)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '绑定解绑次数：' + str(i))
                app.devices_bind_ota(self.mac10, self.section, info, self.port, self.uuid)
                app.device_clickDID()
                self.log.debug(info + u'获取设备标识')
                if "page_name" in app.getresult():
                    self.log.debug(info + u'绑定成功')
                    if app.object_exist("解绑"):
                        app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
                    self.log.debug(info + u'解绑成功')
                    # app.implicitly_wait("realme Watch 2", 60)
                    time.sleep(10)
                    driver.keyevent(4)
                    driver.keyevent(4)
                    time.sleep(20)
                    self.log.debug(info + u'等待设备重启成功')
                else:
                    self.log.error(info + u'绑定失败')
            except:
                self.log.error(info + u'绑定解绑在第N次运行失败：' + str(i))
                if app.object_exist("绑定失败"):
                    self.log.error(info + '绑定失败')
                    driver.keyevent(4)
                self.log.debug(info + '-----------异常处理----------')


    def smoke12(self):
        info = "Process-12"
        print(info)
        self.port = int(self.init_port) + 22
        self.systemPort = int(self.init_systemPort) + 22
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[7]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(5)
        app.open_application(self.port)
        app.devices_bind(self.mac12, self.section, info)
        rebort_cnts = []
        app.device_clickDID()
        rebort_cnts.append(app.getdevice()[2])
        for i in range(1, 1000):
            try:
                app.device_clickDID()
                self.log.debug(info + "获取设备标识")
                if "reboot_cnt" in app.getresult():
                    rebort_cnts.append(app.getdevice()[2])
                    self.log.debug(info + "获取重启次数：" + str(app.getdevice()[2]))
                else:
                    rebort_cnts.append('1000')                                                                               #防止执行失败。该轮元素轮空
                    self.log.debug(info + "获取重启次数失败")
                if str(rebort_cnts[i]) > str(rebort_cnts[i-1]):
                    self.log.error(info + "-----------------------------------------设备出现重启----------------------------------------------------:" + str(i))
                    app.call_back_devices_init(info)
                self.log.debug(info + '进入各个应用次数：' + str(i))
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
                app.call_back(self.mac12, self.section, self.port, self.uuid, info)

if __name__ == '__main__':
    multiprocessings = []
    # t1 = multiprocessing.Process(target=Testsmoke().smoke1)
    # t2 = multiprocessing.Process(target=Testsmoke().smoke2)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke3)
    # t4 = multiprocessing.Process(target=Testsmoke().smoke4)
    # t5 = multiprocessing.Process(target=Testsmoke().smoke5)
    # t6 = multiprocessing.Process(target=Testsmoke().smoke6)
    # t7 = multiprocessing.Process(target=Testsmoke().smoke7)
    # t8 = multiprocessing.Process(target=Testsmoke().smoke8)
    # t9 = multiprocessing.Process(target=Testsmoke().smoke9)
    t10 = multiprocessing.Process(target=Testsmoke().smoke10)
    t11 = multiprocessing.Process(target=Testsmoke().smoke11)
    # t12 = multiprocessing.Process(target=Testsmoke().smoke12)
    # multiprocessings.append(t1)
    # multiprocessings.append(t2)
    # multiprocessings.append(t3)
    # multiprocessings.append(t4)
    # multiprocessings.append(t5)
    # multiprocessings.append(t6)
    # multiprocessings.append(t7)
    # multiprocessings.append(t8)
    # multiprocessings.append(t9)
    multiprocessings.append(t10)
    multiprocessings.append(t11)
    # multiprocessings.append(t12)
    for t in multiprocessings:
        t.start()

