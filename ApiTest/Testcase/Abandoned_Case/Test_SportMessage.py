#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/9 15:04
# @Author : Greey
# @FileName: Test_SportMessage.py

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

@allure.epic("设备自动化")
@allure.feature('模拟设备端业务流程')
@allure.description('运动中发消息')
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

    @allure.title("运动中发消息")
    @allure.story("正常流程")
    @allure.severity('blocker')
    # @pytest.mark.smoke
    def test_sportmessage(self):
        self.driver = self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)
        self.app.device_upslide()
        self.app.saturn_inputclick("160", "160", "160", "160")
        self.app.saturn_inputclick("160", "300", "160", "300")
        self.app.saturn_inputclick("160", "160", "160", "160")
        self.driver.keyevent(4)
        self.app.devices_click('SATURN_APP')
        self.app.click_prompt_box()
        self.app.click_prompt_box()
        self.app.click_prompt_box()
        self.app.tv_send_notification('{"appMessage": {"appId": "app.wx", "text": "ryeex", "title": "ryeex"}, "type": "APP_MESSAGE"}')
        time.sleep(3)
        self.app.tv_send_notification('{"sms": {"contact": "ryeex", "content": "ryeex", "sender": "110"}, "type": "SMS"}')
        time.sleep(3)
        self.app.tv_send_notification('{"telephony": {"contact": "ryeex", "number": "110", "status": "RINGING_UNANSWERABLE"}, "type": "TELEPHONY"}')
        self.driver.keyevent(4)
        self.app.devices_click('SATURN_设备')
        self.app.assert_getdevicepagename("remind")
        self.app.device_home()
        self.app.assert_getdevicepagename("sports")
        self.app.device_home()
        self.app.saturn_inputclick("80", "160", "80", "160")
        self.app.saturn_inputclick("280", "280", "280", "280")
        self.app.assert_getdevicepagename("home_page")
        self.app.device_home()

if __name__ == '__main__':
     pytest.main()