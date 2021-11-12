#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/20 11:34
# @Author : Greey
# @FileName: Test_StopWatch.py


import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.epic("设备自动化")
@allure.feature('模拟设备端业务流程')
@allure.description('1：向上滑动，点击秒表icon；2：检查秒表是否在运行状态；3：点击重试，检查秒表是否新增一条记录；4：点击暂停，检查秒表是否暂停计时；5：返回表盘页面')
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

    @allure.title("秒表")
    @allure.story("正常流程")
    @allure.severity('blocker')
    @pytest.mark.baileys
    def test_stopwatch(self):
        self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)

        # self.app.devices_click('SATURN_设备')
        # time.sleep(15)
        # self.app.device_home()
        # self.app.device_home()
        # self.app.device_home()

        self.app.device_upslide()
        time.sleep(1)
        self.app.device_upslide()
        time.sleep(1)
        self.app.device_upslide()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')
        self.app.saturn_inputclick("180", "100", "180", "100")
        self.app.assert_getdevicepagename('appctr_stopwatch', 'view_start')
        self.app.saturn_inputclick("180", "350", "180", "350")
        self.app.assert_getdevicepagename('appctr_stopwatch', 'view_on')
        self.app.assert_getdevicesstopwatchstatus(2, 0)
        self.app.saturn_inputclick("270", "400", "270", "400")
        self.app.assert_getdevicesstopwatchstatus(2, 1)
        self.app.saturn_inputclick("90", "400", "90", "400")
        self.app.assert_getdevicesstopwatchstatus(1, 1)
        self.app.saturn_inputclick("270", "400", "270", "400")
        self.app.assert_getdevicepagename('appctr_stopwatch', 'view_start')
        self.app.device_upslide()
        self.app.device_home()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')
        self.app.device_upslide()
        self.app.device_home()
        self.app.assert_getdevicepagename('home_page', 'home_id_surface')

if __name__ == '__main__':
     pytest.main()