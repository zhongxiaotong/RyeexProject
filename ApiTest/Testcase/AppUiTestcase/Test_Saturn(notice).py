#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 19:21
# @Author : Greey
# @FileName: Test_Saturn(hrm_spo2).py


import pytest
import os
import time
import allure
from ApiTest.Common.Appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.feature('模拟设备端业务流程')
@allure.description('验证Saturn设备操作场景')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        self.mac = "9C:F6:DD:38:1A:F5"
        self.fuction = 'SATURN_设备'
        self.desired_caps = desired_caps
        self.app = App(desired_caps)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")

    @allure.story("模拟Saturn设备端操作验证")
    @allure.severity('blocker')
    @pytest.mark.smoke
    def test_wyzewatch_smoke(self):
        self.driver = self.app.open_app()
        self.app.devices_bind(self.mac, self.fuction)
        count = 1
        for i in range(1, 1000):
            try:
                self.log.debug(str(i))
                self.app.tv_send_notification('{"telephony": {"contact": "reeyx' + str(i) + '", "number": ' + str(i) + ', "status": "RINGING_UNANSWERABLE"}, "type": "TELEPHONY"}')
                self.driver.keyevent(4)
                self.app.devices_click('SATURN_设备')
                self.app.assert_getdevicepagename('remind')
                self.app.saturn_inputclick("240", "240", "240", "240")
                self.driver.keyevent(4)
                self.app.devices_click('SATURN_APP')
            except:
                count = 1 + count
                self.log.error(str(count))
                self.app.device_home()
                self.app.device_home()
                self.driver.keyevent(4)
                self.app.devices_click('SATURN_APP')
                time.sleep(3)

if __name__ == '__main__':
     pytest.main()
