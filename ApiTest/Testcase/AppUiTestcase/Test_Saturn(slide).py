#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/9 15:04
# @Author : Greey
# @FileName: Test_Saturn(slide).py

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

@allure.feature('模拟Saturn设备操作场景')
@allure.description('重复测试about功能（1000次）')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        desired_caps2 = Yamlc(yaml_path).get_yaml_data(2, "Model", "desired_caps")
        self.wyzeband_mac = "2C:AA:8E:8F:02:32"
        # self.wyzeband_mac = "2C:AA:8E:8F:02:75"
        # self.wyzeband_mac = "9C:F6:DD:38:19:59"
        # self.wyzeband_mac = "9C:F6:DD:38:18:75"
        self.desired_caps = desired_caps
        self.app = App(desired_caps)
        self.app_setting = App(desired_caps2)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")

    @allure.story("点击about，成功显示设备基础信息")
    @allure.step("1:向右滑动屏幕，点击设置图标，检查是否进入setting页面。2：向上滑动屏幕，点击about按钮，检查是否进入about页面。")
    @allure.severity('critical')
    @pytest.mark.smoke
    def test_about_smoke(self):
        self.driver = self.app.open_app()
        time.sleep(1)
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
            self.app.saturn_inputclick("160", "240", "160", "240")
            self.driver.keyevent(4)
            self.app.devices_click('BRANDY_设备')
        time.sleep(1)
        for i in range(1, 100):
            try:
                self.log.info(u'滑动/点击运行次数：' + str(i))
                self.app.device_upslide()
                self.log.debug(u"向上滑动成功")
                self.app.device_downslide()
                self.log.debug(u"向下滑动成功")
                self.app.device_leftslide()
                self.log.debug(u"向左滑动成功")
                self.app.device_upslide()
                self.log.debug(u"向上滑动成功")
                self.app.device_rightslide()
                self.log.debug(u"向右滑动成功")
                self.app.device_longpress()
                self.log.debug(u"长按成功")
                self.app.assert_getdevicepagename("face_pick_page")
                self.log.debug(u"进入切换表盘页面成功")
                self.app.device_leftslide()
                self.log.debug(u"向左滑动成功")
                self.app.device_leftslide()
                self.log.debug(u"向左滑动成功")
                self.app.device_rightslide()
                self.log.debug(u"向右滑动成功")
                self.app.device_rightslide()
                self.log.debug(u"向右滑动成功")
                self.app.device_home()
                self.log.debug(u"Home键返回")
                self.app.assert_getdevicepagename("home_page")
                self.log.debug(u"点击退出切换表盘页面成功")
            except:
                self.log.error(u'滑动/点击在第N次运行失败：' + str(i))
                self.app.device_home()
                self.log.debug(u"返回主页面")



if __name__ == '__main__':
    pytest.main()