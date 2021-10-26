#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 11:19
# @Author : Greey
# @FileName: Test_FirmwareUpdateAll.py

import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from ApiTest.Common.File import *
from ApiTest.Common.Diff import *
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.epic("设备自动化")
@allure.feature('模拟设备端业务流程')
@allure.description('全资源升级，最新版本')
class TestClass():
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        self.desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        self.mac = Yamlc(yaml_path).get_yaml_data(2, "Model", "mac")
        self.fuction = 'SATURN_APP'
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

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")


    @allure.title("固件升级：全资源升级")
    @allure.story("正常流程")
    @allure.severity('blocker')
    @pytest.mark.ota
    def test_firmwareupdate(self, mcu, resoure, diff):
        filename_mcu = os.path.basename(mcu)
        filename_res = os.path.basename(resoure)
        diff_res = os.path.basename(diff)
        self.driver1 = self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)

        # self.app.devices_click('SATURN_设备')
        # time.sleep(10)

        # if os.path.getsize(diff) != 0:
        #     self.app.devices_ota(filename_mcu, diff_res, '0')               #差分升级
        # else:
        #     self.app.devices_ota(filename_mcu, '0', '0')
        self.app.devices_ota(filename_mcu, filename_res, '1')             #全资源升级
        self.driver1.keyevent(4)
        self.app.devices_click('SATURN_设备')
        # self.app.devices_baileys_init(self.info)

if __name__ == '__main__':
     pytest.main()
