#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 14:37
# @Author : Greey
# @FileName: Test_Reset.py


import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.epic("设备自动化")
@allure.feature('模拟设备端业务流程')
@allure.description('1：向上滑动，点击重置icon；2：等待设备重置，初始化设备')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        self.desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        self.mac = Yamlc(yaml_path).get_yaml_data(2, "Model", "mac")
        self.fuction = 'SATURN_设备'
        self.info = "Process-1"
        self.init_port = 4723
        self.init_systemPort = 8200
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.desired_cap = self.dictdatas[0]['desired_caps']
        self.uuids = App(self.desired_cap).getdevices_uuid()
        uuid = self.uuids[0]
        andriod_version = App(self.desired_cap).getdevice_version(uuid)
        print(self.info + "设备ID:" + uuid)
        print(self.info + "安卓版本:" + andriod_version)
        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.init_systemPort
        App(self.desired_cap).start_appium(self.init_port, int(self.init_port) + 1, uuid)
        self.app = App(self.desired_cap)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")

    @allure.title("设备重置")
    @allure.story("正常流程")
    @allure.severity('blocker')
    @pytest.mark.baileys
    def test_reset(self):
        self.driver = self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)

        # self.app.devices_click('SATURN_设备')
        # time.sleep(15)
        # self.app.device_home()
        # self.app.device_home()
        # self.app.device_home()

        self.app.device_upslide()
        self.app.device_upslide()
        self.app.device_upslide()
        self.app.device_upslide()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')  #功能页面
        self.app.saturn_inputclick("180", "350", "180", "350")      #点击设置页面
        self.app.assert_getdevicepagename("setting_page", "list_view")      #判断是否进入了设置页面
        self.app.device_upslide()
        self.app.saturn_inputclick("180", "320", "180", "320")      #点击通用
        self.app.assert_getdevicepagename("setting_general", "list_view")       #判断进入通用页面
        self.app.device_upslide()
        self.app.saturn_inputclick("180", "370", "180", "370")          #点击重置按钮
        self.app.assert_getdevicepagename("setting_reset_realme", 'list_view') #确定是否弹出重置确认弹窗
        self.app.devices_inputclick("300", "350", "300", "350")
        time.sleep(100)
        self.app.devices_bind(self.mac, self.fuction, self.info)
        # self.app.devices_baileys_init(self.info)

if __name__ == '__main__':
     pytest.main()