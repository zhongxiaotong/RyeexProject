#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 11:19
# @Author : Greey
# @FileName: Test_AFirmwareUpdate.py

import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from ApiTest.Common.File import *
from ApiTest.Common.Diff import *
from selenium.webdriver.common.by import By

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

@allure.epic("设备自动化")
@allure.feature('模拟设备端业务流程')
@allure.description('固件升级')
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
        time.sleep(5)
        self.log.debug(u'初始化测试数据')
        src = File().rename_zipname()
        self.newfilenpath_mcu = src[0]
        self.newfilepath_resource = src[1]
        self.log.debug(u'解压zip包')
        print(u'解压zip包')
        filename_res = os.path.basename(self.newfilepath_resource)
        oldfilename_res = os.path.basename(File().get_file())
        parentfile = os.path.abspath(os.path.join(self.newfilepath_resource, ".."))
        grandfatherfile = os.path.abspath(os.path.join(self.newfilepath_resource, "../.."))
        self.diff_res = parentfile + '\\' + oldfilename_res + '-' + filename_res
        diff_res(self.newfilepath_resource, File().get_file(), self.diff_res)
        self.log.debug(u'获取差分资源包')
        if os.path.getsize(self.diff_res) != 0:
            self.res_flag = True
        else:
            self.res_flag = False
        self.log.debug(u'判断是否有差分资源')
        print(u'获取差分资源包')
        self.app.wake_phonescreen(uuid)
        self.log.debug(u'唤醒解锁屏幕')
        print(u'唤醒解锁屏幕')
        self.app.adb_push(uuid, self.newfilenpath_mcu)                          #固件包
        self.app.adb_push(uuid, self.newfilepath_resource)                      #资源包
        self.app.adb_push(uuid, self.diff_res)                                      #差分资源
        self.log.debug(u'下发固件/资源到手机')
        print(u'下发固件/资源到手机')
        filepath = File().mkdir_file()
        File().copy_file(self.newfilepath_resource, filepath + '\\' + filename_res)
        self.log.debug(u'每次保存最新的资源包到Recent_res')
        print(u'每次保存最新的资源包到Recent_res')
        File().rmtree_file(parentfile)
        File().remove_file(grandfatherfile + '\\' + File().get_pathfiles())
        self.log.debug(u'删除旧的固件/资源包')
        print(u'删除旧的固件/资源包')

    def teardown(self):
        # self.app.find_elementby(By.XPATH, "//*[@text='解绑']").click()
        # self.app.close_app()                                                                                           #关闭App
        print("Test End")


    @allure.title("固件升级")
    @allure.story("正常流程")
    @allure.severity('blocker')
    @pytest.mark.smoke
    def test_firmwareupdate(self):
        filename_mcu = os.path.basename(self.newfilenpath_mcu)
        filename_res = os.path.basename(self.newfilepath_resource)
        diff_res = os.path.basename(self.diff_res)
        self.driver = self.app.open_application(self.init_port)
        self.app.devices_bind(self.mac, self.fuction, self.info)
        self.driver.keyevent(4)
        self.app.devices_click('SATURN_APP')
        if self.res_flag:
            self.app.devices_ota(filename_mcu, diff_res, '0')               #差分升级
        else:
            self.app.devices_ota(filename_mcu, '0', '0')
        # self.app.devices_ota(filename_mcu, filename_res, '1')             #全资源升级
        self.driver.keyevent(4)
        self.app.devices_click('SATURN_设备')
        self.app.devices_init(self.info)

if __name__ == '__main__':
     pytest.main()
