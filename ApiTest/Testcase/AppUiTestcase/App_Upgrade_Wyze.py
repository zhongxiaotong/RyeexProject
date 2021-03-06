#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/9/25 16:30
# @Author : Greey
# @FileName: App_Upgrade_Wyze.py



import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.feature('设备升级专项测试(beta-test)')
@allure.description('验证WyzeBand升级场景')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        desired_caps = Yamlc(yaml_path).get_yaml_data(3, "Model", "desired_caps")
        self.desired_caps = desired_caps
        self.app = App(desired_caps)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        print("Test End")

    @allure.story("设备升级")
    @allure.severity('blocker')
    def test_upgradewyze_smoke(self):
        self.driver = self.app.open_app()
        # self.app.click_prompt_box()
        if self.app.object_exist("zyang3647@gmail.com") == False:
            self.app.login_wyze("zyang3647@gmail.com", "Yxz@2020")
        self.app.upgrade_wyze("1.0.7.81")
        self.app.upgrading()
        time.sleep(5)
        self.app.upgrade_wyze_again("1.0.7.78")
        self.app.upgrading()
        self.app.close_app()

if __name__ == '__main__':
     pytest.main()

