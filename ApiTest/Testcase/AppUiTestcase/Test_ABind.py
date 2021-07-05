#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 19:21
# @Author : Greey
# @FileName: Test_Spo2.py


import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from ApiTest.Common.File import *
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.epic("设备自动化")
@allure.feature('模拟设备端业务流程')
@allure.description('1：启动测试工具IDT，2：点击SATURN_APP，3：点击解绑，选择设备mac地址绑定，4：设备点击确认，5：等待设备加载60秒')
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
        time.sleep(5)
        self.log.debug(u'初始化测试数据')
        self.newfilename_mcu = File().rename_zipname()[0]
        self.newfilename_resource = File().rename_zipname()[1]
        self.app.wake_phonescreen(uuid)
        self.app.adb_push(uuid, self.newfilename_mcu)
        self.app.adb_push(uuid, self.newfilename_resource)

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")


    @allure.title("绑定设备")
    @allure.story("正常流程")
    @allure.severity('blocker')
    @pytest.mark.smoke
    def test_bind(self):
        self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)
        self.app.devices_ota(version)
        self.app.devices_init(self.info)

if __name__ == '__main__':
     pytest.main()
