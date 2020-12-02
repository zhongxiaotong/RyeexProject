#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/9 15:04
# @Author : Greey
# @FileName: Test_Brandy(slide).py

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
@allure.description('重复滑动点击')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        self.mac = "9C:F6:DD:38:1B:81"
        self.fuction = 'BRANDY_设备'
        self.desired_caps = desired_caps
        self.app = App(desired_caps)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")

    @allure.story("模拟设备滑动点击")
    @allure.step("1:模拟设备滑动点击")
    @allure.severity('critical')
    @pytest.mark.smoke
    def test_slide_smoke(self):
        self.driver = self.app.open_app()
        self.app.devices_bind(self.mac, self.fuction)
        self.app.device_upslide()
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