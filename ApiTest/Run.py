# -*- coding: utf-8 -*-
# @Time : 2020/8/18 10:05
# @Author : Greey
# @FileName: Run.py

import os
import win32com.client
from ApiTest.Common.Log import MyLog
import pytest
from ApiTest.Common.Feishu import FeiShutalkChatbot
import datetime
import socket

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
        on_off = 'off'
        self.log = MyLog()
        check_exsit("java.exe")
        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        # current_path = os.path.abspath(__file__)
        # father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")
        # report_path = father_path + "\\" + "Config\Config.ini"
        # self.report_path = report_path.replace("\\", "/")
    def run(self):
        try:
            self.log.info("********TEST START** ******")
            pytest.main(['-m', 'smoke', '--alluredir', './Report/xml'])
            # pytest.main(['C:\Users\EDZ\PycharmProjects\Autotest_platform\Project-Pycharm\ApiTest\Testcase\AppUiTestcase\Test_ZGetDevicesLog.py', '--alluredir', './Report/xml'])
            os.system('allure generate ./Report/xml -o ./Report/html --clean')                 #将报告转换成HTML
        except:
            self.log.error(u'测试用例执行失败，请检查')
        finally:
            currentdate = datetime.datetime.now().strftime('%Y-%m-%d')
            msg = currentdate + 'CI自动化测试报告：http://' + self.ip + ':11111/index.html'
            self.log.info("*********TEST END*********")
            # send test report by feishu
            if on_off == 'on':
                webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/3d927bee-4ab5-4b87-8c01-ca1374179b27"
                FeiShutalkChatbot(webhook).send_text(msg)
            os.system('allure serve ./Report/xml --port 11111')
        #
        #
        #     elif on_off == u'off':
        #         self.logger.info("Doesn't send report email to developer.")
        #     else:
        #         self.logger.info("Unknow state.")


if __name__ == '__main__':
    AllTest().run()






