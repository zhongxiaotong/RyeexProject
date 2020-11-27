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
@allure.description('验证Brandy设备操作场景')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        desired_caps2 = Yamlc(yaml_path).get_yaml_data(2, "Model", "desired_caps")
        self.wyzeband_mac = "2C:AA:8E:8F:03:52"
        self.desired_caps = desired_caps
        self.app = App(desired_caps)
        self.app_setting = App(desired_caps2)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        self.app.close_app()                                                                                           #关闭App
        print("Test End")

    @allure.story("模拟Brandy设备端操作验证")
    @allure.severity('blocker')
    @pytest.mark.smoke
    def test_wyzewatch_smoke(self):
        self.driver = self.app.open_app()
        time.sleep(1)
        for i in range(1, 100):
            self.app.devices_click('BRANDY_设备')
            time.sleep(1)
            while self.app.object_exist(self.wyzeband_mac + "  正在连接...") :
                time.sleep(1)
            if self.app.object_exist(self.wyzeband_mac + "  已连接") == False:
                self.app.devices_click('解绑')
                self.app.click_prompt_box()
                if (self.app.object_exist("realme Watch Saturn") or self.app.object_exist("WYZE") or self.app.object_exist("hey+")) == False:
                    self.app.close_app()
                    self.app_setting.restart_bluetooth()                                                                       #重启蓝牙
                    self.driver = self.app.open_app()
                    self.app.devices_click('BRANDY_设备')
                    self.app.devices_click('解绑')
                while self.app.object_exist(self.wyzeband_mac) == False:
                    time.sleep(1)
                self.app.devices_click(self.wyzeband_mac)
                while self.app.object_exist("请在设备上点击确认") == False:
                    time.sleep(1)
                self.app.devices_click('完成')
                self.app.devices_click('BRANDY_设备')
                self.app.brandy_inputclick("160", "240")
                self.driver.keyevent(4)
                self.app.devices_click('BRANDY_设备')
                try:
                    self.log.debug(u'运行次数：' + str(i))
                    assert(self.app.object_exist(self.wyzeband_mac + "  已连接"))
                    self.device_clickDID()
                    self.app.assert_getdevicepagename('home_page')
                    self.log.debug(u'进入表盘主页面成功')
                    self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
                    self.log.debug(u'解绑成功')
                except:
                    self.log.error(u'绑定解绑第N次运行失败：' + str(i))
                time.sleep(6)
                self.driver.keyevent(4)
                self.driver.keyevent(4)

if __name__ == '__main__':
     pytest.main()
