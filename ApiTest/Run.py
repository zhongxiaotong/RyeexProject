# -*- coding: utf-8 -*-
# @Time : 2020/8/18 10:05
# @Author : Greey
# @FileName: Run.py

import os, ctypes, sys
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

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def admin_cmd(cmd):                                                             #获取管理员权限
    if is_admin():
        os.system(cmd)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

def check_exsit(process_name):                                                                                        #判断某个进程是否存在
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    # ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    if len(processCodeCov) > 0:
        admin_cmd('TASKKILL /F /T /IM "%s"' % process_name)
        print(u'结束' + process_name +u'进程')
    else:
        print(process_name + u'进程不存在')

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
        self.case_path = father_path + '\\Testcase\\AppUiTestcase'
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
        # os.chdir(self.temp_path)           https://github.com/ryeex/Automation_Test.git                #切换临时工作路径
        result = list(Firmware(zip_src).get_firmware())
        try:
            self.log.info("********TEST START** ******")
            pytest.main(['-m', 'ota', '--mcu=' + result[0], '--resoure=' + result[1], '--diff=' + result[2], self.case_path, '--alluredir', './Report/xml'])
            pytest.main(['-m', taskname, self.case_path, '--alluredir', './Report/xml'])
            # pytest.main(['C:\Users\EDZ\PycharmProjects\Autotest_platform\Project-Pycharm\ApiTest\Testcase\AppUiTestcase\Test_ZGetDevicesLog.py', '--alluredir', './Report/xml'])
            os.system('allure generate ./Report/xml -o ./Report/html --clean-alluredir')                 #将报告转换成HTML
        except:
            self.log.error(u'测试用例执行失败，请检查')
        finally:
            version = os.path.basename(result[0])
            File(zip_src).rmtree_file(result[3])                #删除解压包
            currentdate = datetime.datetime.now().strftime('%Y-%m-%d')
            msg = currentdate + '-' + taskname + version + '版本测试报告：http://' + self.ip + ':22222/index.html'
            self.log.info("*********TEST END*********")
            # send test report by feishu
            if on_off == 'on':
                webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/8dcfa304-0d45-4bf2-8a2d-d38b45867101"
                FeiShutalkChatbot(webhook).send_text(msg)
            elif on_off == 'off':
                self.log.info("Doesn't send report feishu to developer.")
            else:
                self.log.info("Unknow state.")
            os.system('allure serve ./Report/xml --port 22222')


if __name__ == '__main__':
    AllTest().run()






