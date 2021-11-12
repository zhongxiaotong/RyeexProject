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

def get_now_time():
    now_time=datetime.datetime.now().strftime('%Y\%m\%d\%H\%M\%S')
    today = datetime.date.today()
    return today


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
        current_path = os.path.abspath(__file__)    #返回执行文件的绝对路径，C:\Test_Script\Project-Pycharm\ApiTest\Run.py
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)
                    #os.path.sep:路径分隔符  就是\
                    #os.path.dirname(current_path) 获取执行文件的路径，就是：  C:\Test_Script\Project-Pycharm\ApiTest
                    #os.path.dirname(current_path) + os.path.sep :返回的数据     C:\Test_Script\Project-Pycharm\ApiTest\
                    #最终结果：os.path.abspath(os.path.dirname(current_path) + os.path.sep)  返回的数据   C:\Test_Script\Project-Pycharm\ApiTest


        self.case_path = father_path + '\\Testcase\\AppUiTestcase'  #C:\Test_Script\Project-Pycharm\ApiTest\Testcase\AppUiTestcase
        # self.temp_path = 'C:\\runner\\temp'

    def run(self):
        parser = argparse.ArgumentParser()  #使用 argparse 的第一步是创建一个 ArgumentParser 对象。
                                            #ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息。

        parser.add_argument("--taskname", type=str, help=u"固件路径", default='baileys')    #给一个 ArgumentParser 添加程序参数信息是通过调用 add_argument() 方法完成的
                            #type 命令行参数应当被转换成的类型
                            #help 一个词选项作用的简单描述
                            #default 当参数未在命令行中出现使用的值



        args = parser.parse_args()      #ArgumentParser 通过 parse_args() 方法解析参数

        taskname = args.taskname    #如果没有传参数，那么taskname的值就为baileys

        zip_src = os.path.curdir        #返回一个“。”代表当前目录,这一步就是获取现在的文件路径

        if not os.path.abspath(zip_src):        #如果当前py文件的上级路径不存在，就执行下面的语句，如果上级路径存在，忽略下面语句

            zip_src = os.path.abspath(os.curdir)    #获取现在运行的脚本的上级路径，即   C:\Test_Script\Project-Pycharm\ApiTest
        # if not os.path.abspath(self.temp_path):
        #     os.mkdir(self.temp_path)
        # os.chdir(self.temp_path)           https://github.com/ryeex/Automation_Test.git                #切换临时工作路径

        result = list(Firmware(zip_src).get_firmware())     #C:\Test_Script\Project-Pycharm\ApiTest 路径作为参数调用Firmware().get_firmware()方法，调用的结果用列表装起来

        try:
            self.log.info("********TEST START** ******")
            pytest.main(['-m', 'ota', '--mcu=' + result[0], '--resoure=' + result[1], '--diff=' + result[2], self.case_path, '--alluredir', './Report/xml'])
                #在路径 C:\Test_Script\Project-Pycharm\ApiTest\Testcase\AppUiTestcase 上，执行带有ota标签的所有的测试用例



            pytest.main(['-m', taskname, self.case_path, '--alluredir', './Report/xml'])        #生成allure的json格式的路径.
                #在路径C:\Test_Script\Project-Pycharm\ApiTest\Testcase\AppUiTestcase 上，执行带有baileys标签的测试用例


            # pytest.main(['-m', "debugging", self.case_path, '--alluredir', './Report/xml'])   #用来调试不通过的测试用例
            #"--html={}\\test{}.html"
            # pytest.main(['-m', "debugging", self.case_path, '--alluredir', './Report/xml',r"--html=C:\Test_Script\Project-Pycharm\ApiTest\Report\test_report\test.html"])


            # pytest.main(['C:\Users\EDZ\PycharmProjects\Autotest_platform\Project-Pycharm\ApiTest\Testcase\AppUiTestcase\Test_ZGetDevicesLog.py', '--alluredir', './Report/xml'])
            os.system('allure generate ./Report/xml -o ./Report/html --clean-alluredir')        #在cmd下面运行，生成测试报告                 #将报告转换成HTML
        except:
            self.log.error(u'测试用例执行失败，请检查')
        finally:
            version = os.path.basename(result[0])
            File(zip_src).rmtree_file(result[3])                #删除解压包
            currentdate = datetime.datetime.now().strftime('%Y-%m-%d')
            msg = currentdate + '-' + taskname + version + '版本测试报告：http://' + self.ip + ':22222/index.html'
            # msg = currentdate + '-' + taskname + "  外网-多版本测试报告功能调试  " + '版本测试报告：http://' + self.ip + ':22222/index.html'
            self.log.info("*********TEST END*********")
            # send test report by feishu
            if on_off == 'on':
                webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/8dcfa304-0d45-4bf2-8a2d-d38b45867101"     #  测试大群

                # webhook="https://open.feishu.cn/open-apis/bot/v2/hook/39256e63-236c-42bd-a636-35e027d2667f"       #私人调试群

                FeiShutalkChatbot(webhook).send_text(msg)
            elif on_off == 'off':
                self.log.info("Doesn't send report feishu to developer.")
            else:
                self.log.info("Unknow state.")
            os.system('allure serve ./Report/xml --port 22222')


if __name__ == '__main__':
    AllTest().run()






