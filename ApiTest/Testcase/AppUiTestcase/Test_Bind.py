#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 19:21
# @Author : Greey
# @FileName: Test_Saturn(hrm_spo2).py


import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.feature('模拟设备端业务流程')
@allure.description('绑定解绑')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.init_port = 4723
        self.init_systemPort = 8200
        self.port = self.init_port
        self.systemPort = self.init_systemPort
        self.section = 'SATURN_设备'
        desired_caps = self.dictdatas[0]['desired_caps']
        self.mac = "9C:F6:DD:38:1F:5E"
        uuid = App(desired_caps).getdevices_uuid()[0]
        andriod_version = App(desired_caps).getdevice_version(uuid)
        desired_caps['deviceName'] = uuid
        desired_caps['platformVersion'] = andriod_version
        desired_caps['systemPort'] = self.systemPort
        App(desired_caps).start_appium(self.port, int(self.port) + 1, uuid)
        self.app = App(desired_caps)
        time.sleep(2)
        self.driver = self.app.open_application(self.port)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        self.app.close_app()                                                                                           #关闭App
        print("Test End")

    @allure.story("模拟设备端操作验证")
    def test_bind(self):
        for i in range(1, 1000):
            try:
                self.log.debug(u'绑定解绑运行次数：' + str(i))
                self.app.devices_bind_ota(self.mac, self.section)
                self.log.debug(u'绑定成功')
                self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
                self.log.debug(u'解绑成功')
                while self.app.object_exist("realme Watch 2") == False:
                    time.sleep(0.5)
                self.driver.keyevent(4)
                self.driver.keyevent(4)
                time.sleep(20)
                self.log.debug(u'等待设备重启成功')
            except:
                self.log.error(u'绑定解绑在第N次运行失败：' + str(i))
                self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
                while self.app.object_exist("realme Watch 2") == False:
                    time.sleep(0.5)
                self.driver.keyevent(4)
                self.driver.keyevent(4)
if __name__ == '__main__':
     pytest.main()
