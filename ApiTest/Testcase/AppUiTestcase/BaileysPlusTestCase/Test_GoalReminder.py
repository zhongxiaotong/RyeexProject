#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/8/13 11:35
# @Author : Greey
# @FileName: Test_GoalReminder.py

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
@allure.description('1：设置目标提醒为5000步；2：向上滑动，点击设置icon，打开目标提醒；3：增加步数，检查是否有目标提醒页面；4：关闭目标提醒；5：返回表盘页面')
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

    @allure.title("目标提醒")
    @allure.story("正常流程")
    @allure.severity('blocker')
    @pytest.mark.baileysplus
    def test_goalremind(self):
        self.driver = self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)
        self.driver.keyevent(4)
        self.app.devices_click('SATURN_APP')
        self.app.click_prompt_box()
        self.app.click_prompt_box()
        self.app.click_prompt_box()
        self.app.tv_setgoalstep('5000')
        self.driver.keyevent(4)
        self.app.devices_click('SATURN_设备')
        self.app.device_upslide()
        self.app.device_upslide()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')
        self.app.saturn_inputclick("320", "400", "320", "400")
        self.app.assert_getdevicepagename("setting_page", "list_view")
        self.app.saturn_inputclick("180", "270", "180", "270")
        self.app.assert_getdevicepagename("setting_notification", "list_view")
        self.app.saturn_inputclick("180", "190", "180", "190")
        self.app.device_home()
        self.app.assert_getdevicepagename("setting_page", "list_view")
        self.app.device_home()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')
        self.app.device_home()
        self.app.assert_getdevicepagename('home_page', 'home_id_surface')
        self.app.device_addstep('5000')
        self.app.device_clickDID()
        count = 1
        while 'remind' not in self.app.getresult():
            time.sleep(0.5)
            count += 1
            self.app.device_clickDID()
            if count >= 30:
                raise
        self.app.device_home()
        self.app.device_upslide()
        self.app.device_upslide()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')
        self.app.saturn_inputclick("320", "400", "320", "400")
        self.app.assert_getdevicepagename("setting_page", "list_view")
        self.app.saturn_inputclick("180", "270", "180", "270")
        self.app.assert_getdevicepagename("setting_notification", "list_view")
        self.app.saturn_inputclick("180", "190", "180", "190")
        self.app.device_home()
        self.app.assert_getdevicepagename("setting_page", "list_view")
        self.app.device_home()
        self.app.assert_getdevicepagename('home_page', 'home_id_down')
        self.app.device_home()
        self.app.assert_getdevicepagename('home_page', 'home_id_surface')


if __name__ == '__main__':
     pytest.main()