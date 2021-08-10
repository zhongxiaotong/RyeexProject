# -*- coding: utf-8 -*-
# @Time : 2020/8/18 10:05
# @Author : Greey
# @FileName: Run.py

import os
import win32com.client
from Common.Log import MyLog
import pytest
from Common.Feishu import FeiShutalkChatbot
from Common.File import *
import datetime
import socket
import argparse
from Common.Firmware import Firmware

# C = ReadConfig()
# on_off = C.get_configdata("EMAIL", "on_off")

def check_exsit(process_name):                                                                                        #判断某个进程是否存在
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        os.system('TASKKILL /F /IM "%s"' % process_name)
        print '%s is exists' % process_name
    else:
        print '%s is not exists' % process_name

class AllTest(object):

    def __init__(self):
        global on_off
        on_off = 'on'
        self.log = MyLog()
        check_exsit("java.exe")
        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        current_path = os.path.abspath(__file__)
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)
        grandfather_path = os.path.abspath(os.path.dirname(current_path))
        self.case_path = father_path + '\\Testcase\\AppUiTestcase'
        self.firmwareUpdate_path = grandfather_path + "\\" + "Testcase\\AppUiTestcase\\FirmwareUpdate.py"
        # self.temp_path = 'C:\\runner\\temp'
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--taskname", type=str, help=u"固件路径", default='baileys')
        args = parser.parse_args()
        taskname = args.taskname
        zip_src = os.path.curdir
        if not os.path.abspath(zip_src):
            zip_src = os.path.abspath(os.curdir)
        # if not os.path.abspath(self.temp_path):
        #     os.mkdir(self.temp_path)
        # os.chdir(self.temp_path)                           #切换临时工作路径
        result = list(Firmware(zip_src).get_firmware())
        File(zip_src).rmtree_file(result[3])                #删除解压包
        try:
            self.log.info("********TEST START** ******")
            pytest.main(['-s', '--mcu=' + result[0], '--resoure=' + result[1], '--diff=' + result[2], self.firmwareUpdate_path, '--alluredir', './Report/xml'])
            pytest.main(['-m', taskname, self.case_path, '--alluredir', './Report/xml'])
            # pytest.main(['C:\Users\EDZ\PycharmProjects\Autotest_platform\Project-Pycharm\ApiTest\Testcase\AppUiTestcase\Test_ZGetDevicesLog.py', '--alluredir', './Report/xml'])
            os.system('allure generate ./Report/xml -o ./Report/html --clean')                 #将报告转换成HTML
        except:
            self.log.error(u'测试用例执行失败，请检查')
        finally:
            currentdate = datetime.datetime.now().strftime('%Y-%m-%d')
            msg = currentdate + '--************--自动化测试报告--************--：http://' + self.ip + ':22222/index.html'
            self.log.info("*********TEST END*********")
            # send test report by feishu
            if on_off == 'on':
                webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/b79d0ddf-2bc0-4739-af5a-272de35b524e"
                FeiShutalkChatbot(webhook).send_text(msg)
            os.system('allure serve ./Report/xml --port 22222')
        #
        #
        #     elif on_off == u'off':
        #         self.logger.info("Doesn't send report email to developer.")
        #     else:
        #         self.logger.info("Unknow state.")


if __name__ == '__main__':
    AllTest().run()






