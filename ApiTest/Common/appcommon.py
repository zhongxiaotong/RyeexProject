#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/9/12 17:12
# @Author : Greey
# @FileName: Appcommon.py

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import Log
from selenium.webdriver.common.by import By
import time
import allure
from appium.webdriver.common.touch_action import TouchAction
import random
import os
from Readyaml import Yamlc
import json
import commands


current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")                                  #获取上级目录
yaml_path_setting = father_path + "\\" + "Testdata\\setting.yaml"


class App(object):

    # 初始化设备参数
    def __init__(self, desired_caps):
        self.desired_caps = desired_caps
        self.log = Log.MyLog()

    @allure.step("打开app")
    def open_app(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return self.driver

    @allure.step("打开app")
    def open_application(self, port):
        self.driver = webdriver.Remote('http://localhost:' + str(port) + '/wd/hub', self.desired_caps)
        return self.driver

    #不同的driver
    @allure.step("打开Setting")
    def open_setting(self, desired_caps):
        self.driver2 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return self.driver2

    @staticmethod
    def start_appium(port, bootstrap, udid):
        a = os.popen('netstat -ano | findstr "%s" ' % port)
        time.sleep(2)
        t1 = a.read()
        if "LISTENING" not in t1:
            os.system("start /b appium -a 127.0.0.1 -p %s -bp %s -U %s" % (port, bootstrap, udid))

    @staticmethod
    def stop_appium(self):  # 关闭所有的appium进程
        os.system("start /b taskkill /F /t /IM Appium.exe")

    @allure.step("结束app进程")
    def close_app(self):
        self.driver.quit()


    @allure.step("结束setting进程")
    def close_setting(self):
        self.driver2.quit()

    # @allure.step("截图")
    # def get_screenshot(self, file_path):
    #     sleep(5)
    #     self.file_path = file_path
    #     if (os.path.exists(self.file_path) == False):                                       # 判断路径是否存在
    #         os.makedirs(self.file_path)
    #     now = time.strftime('%Y-%m-%d %H_%M_%S')
    #     filename = self.file_path + '\\' + now + '.png'
    #     self.driver.get_screenshot_as_file(filename)
    #     self.fp = open(filename, 'rb').read()
    #     return self.fp

    # 重写元素定位方法
    def find_elementby(self, *loc):
        try:
            WebDriverWait(self.driver, 120).until(lambda driver: driver.find_element(*loc).is_displayed())             #隐式等待
            sleep(0.5)
            return self.driver.find_element(*loc)
        except:
            self.log.error(u'app页面未能找到该元素%s' % loc[1])
            return False

    # 重写元素定位方法（不同的driver）
    def find_elementby2(self, *loc):
        try:
            WebDriverWait(self.driver2, 120).until(lambda driver: driver.find_element(*loc).is_displayed())            #隐式等待
            sleep(0.5)
            return self.driver2.find_element(*loc)
        except:
            self.log.error(u'app页面未能找到该元素%s' % loc[1])
            return False

    def swpe(self, start_x, start_y, end_x, end_y):
        '''
        - start_x - 开始滑动的x坐标
        - start_y - 开始滑动的y坐标
        - end_x - 结束点x坐标
        - end_y - 结束点y坐标
        - duration - 持续时间，单位毫秒
        '''
        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
        time.sleep(5)
        # for i in range(2):    ###增加滑动次数，因为有时滑动不明显。这一步很有效果。2可以是更改的，如果滑动的少，可以增加滑动次数的。
        #     time.sleep(5)
        #     self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def assert_notin_text(self, expecttext='BleError'):
        time.sleep(1)
        text = self.find_elementby(By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ryeex.sdk.demo:id/tv_result']").text.encode("utf-8")
        # text = self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @resource-id='com.ryeex.sdk.demo:id/tv_result']").text.encode("utf-8")
        if len(text) != 0:
            try:
                assert str(expecttext) not in str(text)
            except:
                self.log.error(u'App页面Response验证失败%s' % text)
                raise
        else:
            self.log.error(u'设备回调为空值')
            raise

    def assert_in_text(self, expecttext):
        time.sleep(1)
        text = self.find_elementby(By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ryeex.sdk.demo:id/tv_result']").text.encode("utf-8")
        if len(text) != 0:
            try:
                assert expecttext in text
            except:
                self.log.error(u'Response验证失败,实际返回结果%s，预期返回结果%s' % (text, expecttext))
                raise
        else:
            self.log.error(u'设备回调为空值')
            # self.driver.keyevent(4)
            # time.sleep(200)
            # self.devices_click('SATURN_设备')


    def assert_getdevicedeltams(self):
        if self.getdevice():
            delta_ms = self.getdevice()[0]
            try:
                assert(int(delta_ms) <= 2000)
            except:
                self.log.warning(u'设备响应时间超时%s' % delta_ms)
                # raise
        else:
            self.log.error(u'delta_ms为空')


    def assert_getdevicepagename(self, target_pagename):
        if self.getdevice():
            page_name = self.getdevice()[1]
            try:
                assert(target_pagename == page_name)
            except:
                self.log.error(u'验证失败：当前页面为%s.预期页面为%s' %(page_name, target_pagename))
                raise
        else:
            self.log.error(u'page_name为空')

    def getdevice(self):
        time.sleep(1)
        text = self.find_elementby(By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ryeex.sdk.demo:id/tv_result']").text.encode("utf-8")
        if len(text) != 0:
            delta_ms = text.split(',')[1].split(':')[2]               #delta_ms:ui线程上次进入的时间戳距离现在过了多久
            page_name = text.split(',')[3].split(':')[1]
            # if page_name == 'remind':                                                                                 #退出提醒页面
            #     self.device_home()
            return delta_ms, page_name
        else:
            self.log.error(u'设备回调为空值')
            raise

    def assert_connect_status(self):
        text = self.find_elementby(By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='com.ryeex.sdk.demo:id/tv_connect_status']").text
        if len(text.encode("utf-8")) != 0:
            state = text[-3:]
            try:
                assert(state == u'已连接')
            except:
                self.log.error(u'设备已断开连接%s' % text)
                raise
        else:
            self.log.error(u'设备回调为空值')
            raise

    def object_exist(self, text):
        loc = '//*[@text="' + text + '"]'
        flag = True
        try:
            WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element(By.XPATH, loc).is_displayed())
            return flag
        except:
            flag = False
            return flag

    def object_exist_xpath(self, xpath):
        flag = True
        try:
            WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element(By.XPATH, xpath).is_displayed())
            return flag
        except:
            flag = False
            return flag


    def getid(self):
        L = []
        M = []
        for i in range(5):
             L.append(random.randint(0, 9))
             if len(L) >= 5:
                     break
        for d in L:
            M.append(str(d))
        S = ''.join(M)
        return S

    def getdevices_uuid(self):
        try:
            r = os.popen("adb devices")
            text = r.read()
            r.close()
            if len(text.split('\n')) == 3:
                self.log.error(u"设备列表为空")
            # num = len(text.split('\n'))
            if len(text.split('\n')) == 4:
                devices1 = text.split('\n')[1].split('\t')[0]
                return devices1
            if len(text.split('\n')) == 5:
                devices1 = text.split('\n')[1].split('\t')[0]
                devices2 = text.split('\n')[2].split('\t')[0]
                return devices1, devices2
            if len(text.split('\n')) == 6:
                devices1 = text.split('\n')[1].split('\t')[0]
                devices2 = text.split('\n')[2].split('\t')[0]
                devices3 = text.split('\n')[3].split('\t')[0]
                return devices1, devices2, devices3
            if len(text.split('\n')) == 7:
                devices1 = text.split('\n')[1].split('\t')[0]
                devices2 = text.split('\n')[2].split('\t')[0]
                devices3 = text.split('\n')[3].split('\t')[0]
                devices4 = text.split('\n')[4].split('\t')[0]
                return devices1, devices2, devices3, devices4
            if len(text.split('\n')) == 8:
                devices1 = text.split('\n')[1].split('\t')[0]
                devices2 = text.split('\n')[2].split('\t')[0]
                devices3 = text.split('\n')[3].split('\t')[0]
                devices4 = text.split('\n')[4].split('\t')[0]
                devices5 = text.split('\n')[5].split('\t')[0]
                return devices1, devices2, devices3, devices4, devices5
        except:
            self.log.error(u"请检查设备是否成功连接电脑")
            raise

    def getdevice_version(self, uuid):
        try:
            r = os.popen('"adb -P 5037 -s ' + uuid + 'shell getprop ro.build.version.release"')
            text = r.read()
            r.close()
            return text
        except:
            self.log.error(u"请检查设备是否成功连接电脑")
            raise


    # def bind_devices(self):
    #     if self.object_exist("2C:AA:8E:00:AB:95") == False:
    #         self.driver.close_app()
    #         self.restart_bluetooth()                                                                       #重启蓝牙
    #         self.driver = self.open_app()
    #         self.click_prompt_box()
    #         if self.object_exist("2C:AA:8E:00:AB:95") == False:
    #             self.driver.keyevent(4)                                                                                #模拟返回键
    #             self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="解绑"]').click()
    #     self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="2C:AA:8E:00:AB:95"]').click()
    #     if self.object_exist("绑定失败"):
    #         self.driver.keyevent(4)
    #         self.driver.keyevent(4)
    #         self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="解绑"]').click()
    #         self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="2C:AA:8E:00:AB:95"]').click()
    #     # self.app.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="请在设备上点击确认"]')
    #     # self.app.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="绑定成功"]')
    #     # self.app.find_elementby(By.XPATH, '//*[@class="android.widget.Button" and @text="完成"]').click()

    #重启蓝牙
    def restart_bluetooth(self, desired_caps_setting):
        self.driver2 = App.open_setting(desired_caps_setting)
        time.sleep(1)
        self.find_elementby2(By.XPATH, '//android.widget.TextView[@text="蓝牙"]').click()
        time.sleep(1)
        self.find_elementby2(By.XPATH, '//android.widget.TextView[@text="蓝牙"]').click()
        time.sleep(1)
        self.find_elementby2(By.XPATH, '//*[@class="android.widget.Switch" and @resource-id="com.android.settings:id/switch_widget"]').click()
        time.sleep(1)
        self.find_elementby2(By.XPATH, '//*[@class="android.widget.Switch" and @resource-id="com.android.settings:id/switch_widget"]').click()
        # self.driver2.keyevent(3)                                                                                       #模拟home键
        self.close_setting()

###-------------------------------------------------------------------业务脚本----------------------------------------------------------------------###
    @allure.step("saturn坐标输入")
    def saturn_inputclick(self, sx, sy, ex, ey):
        # self.assert_connect_status()
        self.input_data('{"method":"tp_move","sx":"' + sx + '","sy":"' + sy + '","ex":"' + ex + '","ey":"' + ey + '","duration":"50","interval":"50"}')
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='坐标点击/滑动']").click()
        self.clear_text()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()

    @allure.step("saturn坐标滑动")
    def saturn_inputslide(self, sx, sy, ex, ey):
        # self.assert_connect_status()
        self.input_data('{"method":"tp_move","sx":"' + sx + '","sy":"' + sy + '","ex":"' + ex + '","ey":"' + ey + '","duration":"2000","interval":"50"}')
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='坐标点击/滑动']").click()
        self.clear_text()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()



    def brandy_inputclick(self, x, y):
        # self.assert_connect_status()
        self.input_data('{"id": ' + self.getid() + ', "method": "touch", "gesture": "click", "pos": {"x": "' + x + '", "y": "'+ y + '"}}')
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='坐标点击/滑动']").click()
        self.clear_text()
        self.assert_in_text(expecttext='ok')

    @allure.step("点击上滑")
    def device_upslide(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='上滑']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        # self.log.debug(u'向上滑动成功')

    @allure.step("点击下滑")
    def device_downslide(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='下滑']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        # self.log.debug(u'向下滑动成功')

    @allure.step("点击左滑")
    def device_leftslide(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='左滑']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        # self.log.debug(u'向左滑动成功')

    @allure.step("点击右滑")
    def device_rightslide(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='右滑']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        # self.log.debug(u'向右滑动成功')


    @allure.step("点击HOME")
    def device_home(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='HOME']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        # self.log.debug(u'HOME键成功')

    @allure.step("点击LONG HOME")
    def device_longhome(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='LONG HOME']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        self.assert_getdevicepagename("power")
        # self.log.debug(u'长按HOME键成功')

    @allure.step("点击长按")
    def device_longpress(self):
        self.assert_connect_status()
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='长按']").click()
        self.assert_in_text(expecttext='ok')
        self.device_clickDID()
        self.assert_getdevicepagename("face_pick_page")
        # self.log.debug(u'长按')

    @allure.step("点击获取设备标识")
    def device_clickDID(self):
        self.find_elementby(By.XPATH, "//android.widget.Button[@text='获取设备标识']").click()
        self.assert_getdevicedeltams()


    def devices_click(self, text):
        self.find_elementby(By.XPATH, '//*[@text="' + text + '"]').click()

    @allure.step("绑定设备")
    def devices_bind(self, mac, selection):
        desired_caps_setting = Yamlc(yaml_path_setting).get_yaml_data(1, "Model", "desired_caps")
        time.sleep(1)
        self.devices_click(selection)
        time.sleep(1)
        while self.object_exist(mac + "  正在连接...") :
            time.sleep(1)
        if self.object_exist(mac + "  已连接") == False:
            self.devices_click('解绑')
            self.click_prompt_box()
            if (self.object_exist("realme Watch 2") or self.object_exist("WYZE") or self.object_exist("hey+")) == False:
                self.close_app()
                self.restart_bluetooth(desired_caps_setting)                                                            #重启蓝牙
                self.driver = self.open_app()
                self.devices_click(selection)
                self.devices_click('解绑')
            while self.object_exist(mac) == False:
                time.sleep(1)
            self.devices_click(mac)
            while self.object_exist("请在设备上点击确认") == False:
                time.sleep(1)
            self.devices_click('完成')
            self.devices_click(selection)
            self.saturn_inputclick("160", "240", "160", "240")
            self.driver.keyevent(4)
            self.devices_click(selection)


    @allure.step("登录wyze")
    def login_wyze(self, email_address, password):
        self.find_elementby(By.XPATH, '//android.widget.TextView[@text="Login"]').click()
        self.find_elementby(By.XPATH, '//android.widget.EditText[@text="Email address"]').click()
        self.find_elementby(By.XPATH, '//android.widget.EditText[@text="Email address"]').send_keys(email_address)
        self.find_elementby(By.XPATH, '//android.widget.EditText[@text="Password"]').click()
        self.find_elementby(By.XPATH, '//android.widget.EditText[@text="Password"]').send_keys(password)
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/rl_login"]').click()
        time.sleep(5)

    @allure.step("wyze升级")
    def upgrade_wyze(self, version):
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/wyze_main_item_nickname"]').click()
        time.sleep(3)
        if self.object_exist("Enable Background Service") == False:
            while self.find_elementby(By.XPATH, 'com.hualai:id/tv_home_screen_connect_fail_info'):
                self.find_elementby(By.XPATH, 'com.hualai:id/tv_home_screen_connect_fail_info').click()
                time.sleep(5)
        # self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/btn_okey"]').click()
        # self.click_prompt_box()
        self.find_elementby(By.XPATH, '//android.widget.ImageView[@resource-id="com.hualai:id/iv_home_screen_title_setting"]').click()
        if self.object_exist("Please keep the device close to the band while updating") == True:
           self.driver.keyevent(4)
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/rl_more_device_data"]').click()
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/rl_settings_device_fwer_update"]').click()
        el = self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/tv_title_name"]')
        TouchAction(self.driver).tap(el).perform()
        TouchAction(self.driver).tap(x=360, y=92).perform()
        TouchAction(self.driver).tap(x=360, y=92).perform()
        self.find_elementby(By.XPATH, '//android.widget.EditText[@text="Please select the targeted version"]').send_keys(version)
        self.find_elementby(By.XPATH, '//android.widget.TextView[@text="Ok"]').click()
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/lottie_animation"]')

    @allure.step("wyze再次升级")
    def upgrade_wyze_again(self, version):
        self.object_exist("Enable Background Service")
        self.find_elementby(By.XPATH, '//android.widget.ImageView[@resource-id="com.hualai:id/iv_home_screen_title_setting"]').click()
        if self.object_exist("Please keep the device close to the band while updating") == True:
           self.driver.keyevent(4)
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/rl_more_device_data"]').click()
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/rl_settings_device_fwer_update"]').click()
        el = self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/tv_title_name"]')
        TouchAction(self.driver).tap(el).perform()
        TouchAction(self.driver).tap(x=360, y=92).perform()
        TouchAction(self.driver).tap(x=360, y=92).perform()
        self.find_elementby(By.XPATH, '//android.widget.EditText[@text="Please select the targeted version"]').send_keys(version)
        self.find_elementby(By.XPATH, '//android.widget.TextView[@text="Ok"]').click()
        self.find_elementby(By.XPATH, '//*[@resource-id="com.hualai:id/lottie_animation"]')

    @allure.step("等待升级")
    def upgrading(self):
        while self.object_exist("Please keep the device close to the band while updating"):
            time.sleep(1)
        while self.object_exist("Hooray! The update is complete!"):
            time.sleep(1)
        self.object_exist("Enable Background Service")

    @allure.step("忽略提示框")
    def click_prompt_box(self):
        if self.object_exist("总是允许") == True:
            self.find_elementby(By.XPATH, '//*[@text="不再询问"]').click()
            self.find_elementby(By.XPATH, '//*[@text="总是允许"]').click()

    def input_data(self, value):
        self.find_elementby(By.XPATH, '//*[@text="数据输入"]').click()
        self.find_elementby(By.XPATH, '//*[@text="数据输入"]').send_keys(value)


    def clear_text(self):
        self.driver.press_keycode(29, 28672)                                                                            #键盘模拟选中所有删除
        self.driver.press_keycode(112)                                                                                  #键盘模拟选中所有删除
        # context = adr.get_attribute('text')
        # self.edittextclear(context)

    def edittextclear(self, value):
        self.driver.keyevent(123)    #123代表光标移动到末尾键
        for i in range(0, len(value)):
            self.driver.keyevent(67)  #67退格键


    @allure.step("设备信息")
    def tv_device_info(self):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设备信息"]').click()
        self.assert_notin_text()

    @allure.step("设备电量")
    def tv_device_property(self):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设备电量"]').click()
        self.assert_notin_text()

    @allure.step("活动数据")
    def tv_device_activity(self):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="活动数据"]').click()
        self.assert_notin_text()

    @allure.step("数据同步")
    def tv_device_data(self):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="数据同步"]').click()
        self.assert_notin_text()

    @allure.step("查找手环")
    def tv_find_device(self):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="查找手环"]').click()
        time.sleep(5)
        self.assert_notin_text()

    @allure.step("重启手环")
    def tv_reboot_device(self, text):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="重启手环"]').click()
        self.assert_notin_text()
        self.find_elementby(By.XPATH, '//*[@class="android.widget.Button" and @text="' + text + '"]').click()
        time.sleep(10)


    @allure.step("发送通知")
    def tv_send_notification(self, value):
        # value = json.dumps(value)
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="发送通知"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取应用排序")
    def tv_app_list(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取应用排序"]').click()
        self.assert_in_text(keyword)

    @allure.step("设置应用排序")
    def tv_set_app_list(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置应用排序"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取勿扰模式")
    def tv_getDoNotDisturb(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取勿扰模式"]').click()
        self.assert_in_text(keyword)

    @allure.step("设置勿扰模式")
    def tv_setDoNotDisturb(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置勿扰模式"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取抬腕亮屏")
    def tv_getDeviceRaiseToWake(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取抬腕亮屏"]').click()
        self.assert_in_text(keyword)

    @allure.step("设置抬腕亮屏")
    def tv_setDeviceRaiseToWake(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置抬腕亮屏"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取心率检测")
    def tv_getHeartRateDetect(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取心率检测"]').click()
        self.assert_in_text(keyword)

    @allure.step("设置心率检测")
    def tv_setHeartRateDetect(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置心率检测"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取屏幕亮度")
    def tv_getDeviceBrightness(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取屏幕亮度"]').click()
        self.assert_in_text(keyword)

    @allure.step("设置屏幕亮度")
    def tv_setDeviceBrightness(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置屏幕亮度"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取震动开关")
    def tv_getHomeVibrateSetting(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取震动开关"]').click()
        self.assert_in_text(keyword)

    @allure.step("设置震动开关")
    def tv_setHomeVibrateSetting(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置震动开关"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("设置解锁方式")
    def tv_setUnlock(self, value):
        self.input_data(value)
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="设置解锁方式"]').click()
        self.assert_notin_text()
        self.clear_text()

    @allure.step("获取解锁方式")
    def tv_getUnlock(self, keyword):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="获取解锁方式"]').click()
        self.assert_in_text(keyword)

    @allure.step("解绑")
    def tv_unbind(self):
        self.find_elementby(By.XPATH, '//*[@class="android.widget.TextView" and @text="解绑"]').click()