#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/27 14:54
# @Author : Greey
# @FileName: Firmware.py


from File import *
from Diff import *
from Log import MyLog
from appcommon import *

class Firmware(object):
    def __init__(self, zip_src):
        self.log = MyLog()
        F = File(zip_src)
        self.F = F
        src = F.rename_zipname()
        self.newfilepath_mcu = src[0]
        self.newfilepath_resource = src[1]
        self.log.debug(u'解压zip包并且重命名')

    def get_firmware(self):
        filename_res = os.path.basename(self.newfilepath_resource)
        oldfilename_res = os.path.basename(self.F.get_file())
        parentfile = os.path.abspath(os.path.join(self.newfilepath_resource, ".."))
        grandfatherfile = os.path.abspath(os.path.join(self.newfilepath_resource, "../.."))
        self.diff_res = parentfile + '\\' + oldfilename_res + '-' + filename_res
        diff_res(self.F.get_file(), self.newfilepath_resource, self.diff_res)
        self.log.debug(u'获取差分资源包')
        # if os.path.getsize(self.diff_res) != 0:
        #     self.res_flag = True
        # else:
        #     self.res_flag = False
        # self.log.debug(u'判断是否有差分资源')
        print(u'获取差分资源包')
        App.wake_phonescreen()
        self.log.debug(u'唤醒解锁屏幕')
        print(u'唤醒解锁屏幕')
        App.adb_push(self.newfilepath_mcu)                          #固件包
        App.adb_push(self.newfilepath_resource)                      #资源包
        App.adb_push(self.diff_res)                                  #差分资源
        self.log.debug(u'下发固件/资源到手机')
        print(u'下发固件/资源到手机')
        filepath = self.F.mkdir_file()
        self.F.copy_file(self.newfilepath_resource, filepath + '\\' + filename_res)
        self.log.debug(u'每次保存最新的资源包到Recent_res')
        print(u'每次保存最新的资源包到Recent_res')
        # self.F.rmtree_file(parentfile)
        # self.F.remove_file(grandfatherfile + '\\' + self.F.get_pathfiles())
        # self.log.debug(u'删除旧的固件/资源包')
        # print(u'删除旧的固件/资源包')
        return self.newfilepath_mcu, self.newfilepath_resource, self.diff_res, parentfile                       #parentfile 解压包路径