#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 17:35
# @Author : Greey
# @FileName: Test_Saturn(slide).py.py



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

@allure.feature('模拟Saturn设备操作场景')
@allure.description('重复滑动点击')
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
        self.mac = ["9C:F6:DD:38:1E:B3",
                    "9C:F6:DD:38:1F:8E",
                    "9C:F6:DD:38:1F:35",
                    "9C:F6:DD:38:1F:5E",
                    "9C:F6:DD:38:1D:96",
                    "9C:F6:DD:38:1E:E2"]
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
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")

    def test_ota(self):
        for i in range(0, len(self.mac)):
            try:
                print(self.mac[i])
                self.app.devices_bind_ota(self.mac[i], self.section)
                self.driver.keyevent(4)
                self.app.devices_click('SATURN_APP')
                self.app.click_prompt_box()
                self.app.click_prompt_box()
                self.app.click_prompt_box()
                self.app.tv_ota("1.3.0.277 277")
                text = self.app.getresult()
                while True:
                    time.sleep(1)
                    text = self.app.getresult()
                    if text == "set success":
                        break
                self.app.devices_click('解绑')
                # time.sleep(15)
                while self.app.object_exist("realme Watch 2") == False:
                    time.sleep(1)
                self.driver.keyevent(4)
                self.driver.keyevent(4)
            except:
                self.log.error(u'固件升级失败：' + self.mac[i])
                self.app.devices_click('解绑')
                while self.app.object_exist("realme Watch 2"):
                    time.sleep(1)
                self.driver.keyevent(4)
                self.driver.keyevent(4)



if __name__ == '__main__':
    pytest.main()