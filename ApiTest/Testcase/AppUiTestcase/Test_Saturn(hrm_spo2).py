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
        self.mac = "9C:F6:DD:38:1B:81"
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
        self.app.device_upslide()
        self.log.debug(u"向上滑动")
        for i in range(1, 250):
            try:
                self.log.debug(u'血氧心率运行次数：' + str(i))
                self.app.saturn_inputclick("240", "80", "240", "80")
                self.app.assert_getdevicepagename("hrm")
                self.log.debug(u"进入心率功能")
                time.sleep(3)
                self.app.device_home()
                self.log.debug(u'点击home回到上级页面')
                self.app.saturn_inputclick("80", "240", "80", "240")
                self.app.assert_getdevicepagename("spo2")
                self.log.debug(u"进入血氧功能")
                time.sleep(3)
                self.app.device_home()
                self.log.debug(u'点击home回到上级页面')
            except:
                self.log.error(u'血氧心率在第N次运行失败：' + str(i))
                self.app.device_home()
                self.app.device_home()
                self.app.device_upslide()

if __name__ == '__main__':
     pytest.main()
