#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 17:35
# @Author : Greey
# @FileName: Test_Application.py.py



#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 19:21
# @Author : Greey
# @FileName: Test_Spo2.py


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
@allure.description('进出各个应用')
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

    @allure.title('进出各个应用')
    @allure.story("正常流程")
    @allure.severity('blocker')
    # @pytest.mark.smoke
    def test_application(self):
        self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)
        self.app.device_upslide()
        self.app.saturn_inputclick("50", "50", "50", "50")
        self.app.assert_getdevicepagename("activity")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("160", "50", "160", "50")
        self.app.assert_getdevicepagename("hrm")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("270", "50", "270", "50")
        self.app.assert_getdevicepagename("spo2")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("50", "160", "50", "160")
        self.app.assert_getdevicepagename("sleep")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("160", "160", "160", "160")
        self.app.assert_getdevicepagename("sport_list")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("270", "160", "270", "160")
        self.app.assert_getdevicepagename("sports_record")
        self. app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("50", "270", "50", "270")
        self.app.assert_getdevicepagename("alarm")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("160", "270", "160", "270")
        self.app.assert_getdevicepagename("weather")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("270", "270", "270", "270")
        self.app.assert_getdevicepagename("appctr_stopwatch")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.device_upslide()
        self.app.saturn_inputclick("50", "50", "50", "50")
        self.app.assert_getdevicepagename("appctr_timer")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("160", "50", "160", "50")
        self.app.assert_getdevicepagename("music")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("270", "50", "270", "50")
        self.app.assert_getdevicepagename("camera")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("50", "160", "50", "160")
        self.app.assert_getdevicepagename("meditation")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("160", "160", "160", "160")
        self.app.assert_getdevicepagename("findphone")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("270", "160", "270", "160")
        self.app.assert_getdevicepagename("iot_link")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.saturn_inputclick("50", "270", "50", "270")
        self.app.assert_getdevicepagename("setting_page")
        self.app.device_home()
        self.app.assert_getdevicepagename("home_page")
        self.app.device_home()

if __name__ == '__main__':
     pytest.main()
