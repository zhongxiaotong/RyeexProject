#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/14 0014 17:16
# @Author  : ZXT
# @File    : Baileys_All_Upgrade.py

#全资源升级的测试


import multiprocessing
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
import re


current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../../..")              #获取上上级目录
yaml_path = father_path + "\\" + "ApiTest\\Testdata\\app.yaml"



class AllUpgrade():
    def __init__(self):
        self.log = MyLog()
        # self.desired_caps = Yamlc(yaml_path).get_yaml_data(1, "Model", "desired_caps")
        self.fuction = 'SATURN_APP'
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.init_port = 4723
        self.init_systemPort = 8200
        self.driver = None
        self.desired_cap = self.dictdatas[0]['desired_caps']
        self.mcu=r"C:\Users\zyang\Desktop\all_res\0.1.35.90.bin"
        self.resoure=r"C:\Users\zyang\Desktop\all_res\0.1.35.90.res"

        self.uuids = App(self.desired_cap).getdevices_uuid()


        self.mac1 = '2C:AA:8E:09:D3:AA'  #!
        self.mac2 = '98:80:BB:03:0F:ED' #
        self.mac3 ='98:80:BB:03:0E:EE'  #
        self.mac4 = '98:80:BB:03:0E:C1'  #!
        self.mac5 = '2C:AA:8E:09:D3:22'  #!
        self.mac6 = '2C:AA:8E:09:D3:30' #!
        self.mac7 = '98:80:BB:03:0F:1B'  #!
        # ############################
        self.mac8 = 'CC:CC:CC:CC:BB:E5'
        self.mac9 = '2C:AA:8E:09:D0:CD'#
        self.mac10 = '2C:AA:8E:09:D3:30'
        self.mac11 = 'CC:CC:CC:CC:BB:E5'
        self.mac12 = '2C:AA:8E:09:D1:5F'
        self.mac13 = '2C:AA:8E:09:D3:30'
        self.mac14 = 'CC:CC:CC:CC:BB:E5'
        self.mac15 = '98:80:BB:03:0F:EE'
        #---------------------------------------------------
        self.smoke01_mac=self.mac1  #
        self.smoke02_mac=self.mac2  #
        self.smoke03_mac=self.mac3  #
        self.smoke04_mac=self.mac4  #
        self.smoke05_mac=self.mac5  #   !!!!!!
        self.smoke06_mac=self.mac6
        self.smoke07_mac=self.mac7
        # #===========================================================
        self.smoke08_mac=self.mac8
        #
        self.smoke09_mac=self.mac6  #
        self.smoke10_mac=self.mac7  #
        self.smoke11_mac=self.mac11
        self.smoke12_mac=self.mac12
        self.smoke13_mac=self.mac13
        self.smoke14_mac=self.mac14
        self.smoke15_mac=self.mac15
        ####################################################################
        self.smoke01_uuid=self.uuids[0]
        self.smoke02_uuid=self.uuids[1]
        # self.smoke03_uuid=self.uuids[2]
        # self.smoke04_uuid=self.uuids[1]
        # self.smoke05_uuid=self.uuids[2]
        # self.smoke06_uuid=self.uuids[3]
        # self.smoke07_uuid=self.uuids[4]
        # self.smoke08_uuid=self.uuids[7]
        # self.smoke09_uuid=self.uuids[5]
        # self.smoke10_uuid=self.uuids[6]
        # self.smoke11_uuid=self.uuids[10]
        # self.smoke12_uuid=self.uuids[11]
        # self.smoke13_uuid=self.uuids[12]
        # self.smoke14_uuid=self.uuids[13]
        # self.smoke15_uuid=self.uuids[14]


    def get_devices(self):
        r=os.popen("adb devices")
        devices_text=r.read()
        print(devices_text)
        device_count=re.findall("(device)",devices_text)
        if device_count ==[]:
            print("没有安卓设备连接")
        else:

            device_list=re.findall("(.*)	device",devices_text)
            return device_list

    def mobile_file_update(self):
        device_list=self.get_devices()
        self.port = self.init_port
        self.systemPort =self.init_systemPort

        for uuid in device_list:
            # andriod_version = App(self.desired_cap).getdevice_version(uuid)
            # print( "设备ID:" + uuid)
            # print("安卓版本:" + andriod_version)
            # self.desired_cap['deviceName'] = uuid
            # self.desired_cap['platformVersion'] = "platformVersion"
            # self.desired_cap['systemPort'] = "systemPort"
            # App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
            # app = App(self.desired_cap)
            # app.adb_push(self.mcu)         #往手机里面放入固件包
            # app.adb_push(self.resoure)     #往手机里面放入匹配的资源包
            # time.sleep(10)
            # app.stop_appium(self.port)

            # int(self.port)+2
            # int(self.init_systemPort)+2
            print(uuid)

            os.system('adb -s {} push '.format(uuid) + str(self.mcu) + ' /sdcard/Android/data/com.ryeex.sdk.demo/files/Update_File')   #分发固件
            time.sleep(3)
            os.system('adb -s {} push '.format(uuid) + str(self.resoure) + ' /sdcard/Android/data/com.ryeex.sdk.demo/files/Update_File')   #分发资源
            time.sleep(3)
        time.sleep(10)


    def all_upgrade(self,uuid,num,mac):

        info = "upgrade-"+str(num)
        self.port = int(self.init_port)+num*2
        self.systemPort = int(self.init_systemPort)+num*2

        andriod_version = App(self.desired_cap).getdevice_version(uuid)

        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)

        self.desired_cap['deviceName'] = uuid
        self.desired_cap['platformVersion'] = andriod_version
        self.desired_cap['systemPort'] = self.systemPort
        App(self.desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(self.desired_cap)
        time.sleep(5)
        driver = app.open_application(self.port)
        app.devices_bind(mac, self.fuction, info)


        self.log.debug(u'初始化测试数据')
        filename_mcu = os.path.basename(self.mcu)
        filename_res = os.path.basename(self.resoure)



        app.devices_ota(filename_mcu, filename_res, '1')  # 全资源升级
        print("1111111111111111111111111111111111111111111111111111111")
        time.sleep(10)
        # driver.keyevent(4)
        # app.devices_click('SATURN_设备')


    def test_upgrade01(self):
        self.all_upgrade(uuid=self.smoke01_uuid,num=0,mac=self.smoke01_mac)

    def test_upgrade02(self):
        self.all_upgrade(uuid=self.smoke02_uuid,num=1,mac=self.smoke02_mac)

    def test_upgrade03(self):
        self.all_upgrade(uuid=self.smoke03_uuid,num=2,mac=self.smoke03_mac)

    def test_upgrade04(self):
        self.all_upgrade(uuid=self.smoke04_uuid,num=3,mac=self.smoke04_mac)

    def test_upgrade05(self):
        self.all_upgrade(uuid=self.smoke05_uuid,num=4,mac=self.smoke05_mac)

    def test_upgrade06(self):
        self.all_upgrade(uuid=self.smoke06_uuid,num=5,mac=self.smoke06_mac)

    def test_upgrade07(self):
        self.all_upgrade(uuid=self.smoke07_uuid,num=6,mac=self.smoke07_mac)

    def test_upgrade08(self):
        self.all_upgrade(uuid=self.smoke08_uuid,num=7,mac=self.smoke08_mac)

    def test_upgrade09(self):
        self.all_upgrade(uuid=self.smoke09_uuid,num=8,mac=self.smoke09_mac)

    def test_upgrade10(self):
        self.all_upgrade(uuid=self.smoke10_uuid,num=9,mac=self.smoke10_mac)

    def test_upgrade11(self):
        self.all_upgrade(uuid=self.smoke11_uuid,num=10,mac=self.smoke11_mac)

    def test_upgrade12(self):
        self.all_upgrade(uuid=self.smoke12_uuid,num=11,mac=self.smoke12_mac)

    def test_upgrade13(self):
        self.all_upgrade(uuid=self.smoke13_uuid,num=12,mac=self.smoke13_mac)

    def test_upgrade14(self):
        self.all_upgrade(uuid=self.smoke14_uuid,num=13,mac=self.smoke14_mac)

    def test_upgrade15(self):
        self.all_upgrade(uuid=self.smoke15_uuid,num=14,mac=self.smoke15_mac)




if __name__ == '__main__':
    # r=AllUpgrade()
    # r.mobile_file_update()

    multiprocessings = []
    t1=multiprocessing.Process(target=AllUpgrade().test_upgrade01)
    t2=multiprocessing.Process(target=AllUpgrade().test_upgrade02)
    t3=multiprocessing.Process(target=AllUpgrade().test_upgrade03)
    # t4=multiprocessing.Process(target=AllUpgrade().test_upgrade04)
    # t5=multiprocessing.Process(target=AllUpgrade().test_upgrade05)
    # t6=multiprocessing.Process(target=AllUpgrade().test_upgrade06)
    # t7=multiprocessing.Process(target=AllUpgrade().test_upgrade07)
    # t8=multiprocessing.Process(target=AllUpgrade().test_upgrade08)
    # t9=multiprocessing.Process(target=AllUpgrade().test_upgrade09)
    # t10=multiprocessing.Process(target=AllUpgrade().test_upgrade10)
    # t11=multiprocessing.Process(target=AllUpgrade().test_upgrade11)
    # t12=multiprocessing.Process(target=AllUpgrade().test_upgrade12)
    # t13=multiprocessing.Process(target=AllUpgrade().test_upgrade13)
    # t14=multiprocessing.Process(target=AllUpgrade().test_upgrade14)
    # t15=multiprocessing.Process(target=AllUpgrade().test_upgrade15)
    multiprocessings.append(t1)
    multiprocessings.append(t2)
    # multiprocessings.append(t3)
    # multiprocessings.append(t4)
    # multiprocessings.append(t5)
    # multiprocessings.append(t6)
    # multiprocessings.append(t7)
    # multiprocessings.append(t8)
    # multiprocessings.append(t9)
    # multiprocessings.append(t10)
    # multiprocessings.append(t11)
    # multiprocessings.append(t12)
    # multiprocessings.append(t13)
    # multiprocessings.append(t14)
    # multiprocessings.append(t15)
    # print(multiprocessings)
    # time.sleep(10000)
    for t in multiprocessings:
        t.start()





    #===================================================================================================================
    #
    # class_dir=dir(AllUpgrade())
    # # print(class_dir)
    # mac_list=[]
    # device_list=[]
    #
    # for dir_num in class_dir:
    #     # print(dir_num)
    #     new_dir_num=re.findall("^(mac.*)",dir_num)
    #     device_num=re.findall("^(smoke.*_uuid)",dir_num)
    #     if new_dir_num !=[]:
    #         # print(new_dir_num)
    #         mac_list.append(new_dir_num[0])
    #
    #     if device_num !=[]:
    #         # print(device_num)
    #         device_list.append(device_num[0])
    #
    # # print(mac_list)
    # # print(device_list)
    #
    # print(len(device_list))
    # multiprocessings = []
    # for run_count in range(len(device_list)):
    #      num =run_count
    #      uuid = device_list[num]
    #      mac=mac_list[num]
    #      multiprocessings.append(multiprocessing.Process(target=AllUpgrade().all_upgrade01,args=(uuid,int(num),mac)))


    # for t in multiprocessings:
    #     t.start()