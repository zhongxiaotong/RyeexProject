#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/6/11 18:22
# @Author : Greey
# @FileName: File.py


import zipfile
import os,time
import json
from shutil import copyfile
import shutil


class File(object):

    def __init__(self, zip_src='D:\log'):
        self.zip_src = zip_src           #C:\Test_Script\Project-Pycharm\ApiTest
        self.filespath = 'C:\\runner'
        self.unzip_src = self.zip_src + '\\' + os.path.splitext(self.get_pathfiles())[0]        #原稿哈
            # os.path.splitext(self.get_pathfiles())[0] 返回的数值是 res
            #self.zip_src的数值是C:\Test_Script\Project-Pycharm\ApiTest
            #所以self.unzip_src =  C:\Test_Script\Project-Pycharm\ApiTest\res


    def get_pathfiles(self):
        filenames = os.listdir(self.zip_src)    #返回 C:\Test_Script\Project-Pycharm\ApiTest目录下的所有文件

        if filenames:           #加入filenames不为空，执行下面的语句
            for filename in filenames:      #循环
                if '.zip' in filename:      #如果有.zip结尾的文件在里面
                    return filename             #返回这个.zip的文件,就是返回 res.zip

    def unzip_file(self):
        srcfile = self.zip_src + '\\' + self.get_pathfiles()    #C:\Test_Script\Project-Pycharm\ApiTest\res.zip

        list = []
        r = zipfile.is_zipfile(srcfile)                 #判断这个文件是一个压缩包,是就返回True，否就返回False
        try:
            if r:
                fz = zipfile.ZipFile(srcfile, 'r')      #如果是一个压缩包，那么就创建一个ZipFile（）类对象，操作模式是r(读取)
                for file in fz.namelist():              #fz.namelist()返回这个压缩包里面的所有文件: [u'baileys.zip', u'changelog.md', u'history.json', u'res_all.1_zip', u'url.txt']
                    # print(file)
                    fils = fz.extract(file, self.unzip_src)     #将这个压缩包解压到指定的文件路径上,解压路径为 :C:\Test_Script\Project-Pycharm\ApiTest\res
                    list.append(fils)           #用列表把这些包的路径全部装起来

            return list     #[u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\baileys.zip', u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\changelog.md', u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\history.json', u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\res_all.1_zip', u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\url.txt']
        except:
            raise

    def get_mcuversion(self):               #获取固件版本
        configfile = self.unzip_src + "\\config.json"       #根据路径找到config.json文件:C:\Test_Script\Project-Pycharm\ApiTest\res\config.json

        # configfile =r"C:\Test_Script\Project-Pycharm\ApiTest\res\baileys\config.json"
        try:
            if configfile:      #假如C:\Test_Script\Project-Pycharm\ApiTest\res\config.json存在，执行下面的语句
                with open(configfile, 'r') as f:    #
                    f_dict = json.load(f)       #读取json文件
                    print(f_dict['version'])

                    return f_dict['version']        #获取C:\Test_Script\Project-Pycharm\ApiTest\res\baileys\config.json文件里面的版本号信息
        except:
            raise

    def rename_zipname(self):
        filepaths = self.unzip_file()   #[u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\baileys.zip',
                                        # u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\changelog.md',
                                        #  u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\history.json',
                                        #  u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\res_all.1_zip',
                                        #  u'C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\url.txt']

        newfilepath_mcu = self.unzip_src + "\\" + self.get_mcuversion().encode('utf-8')
            #C:\\Test_Script\\Project-Pycharm\\ApiTest\\res\\


        newfilepath_resource = self.unzip_src + "\\" + self.get_mcuversion().encode('utf-8').split('.')[3]
            #self.get_mcuversion().encode('utf-8').split('.')[3]版本号切片，如：0.1.32.11012 返回的是11012
            #这行代码得：以0.1.32.11012为例，返回 C:\Test_Script\Project-Pycharm\ApiTest\res\baileys\11012


        for oldfilepath in filepaths:
            if '.fw.bin' in oldfilepath:
                os.rename(oldfilepath, newfilepath_mcu)
                #C:\Test_Script\Project-Pycharm\ApiTest\res\baileys\0.1.32.11012

        for oldfilepath in filepaths:
            if '.res' in oldfilepath:
                os.rename(oldfilepath, newfilepath_resource)
                #C:\Test_Script\Project-Pycharm\ApiTest\res\baileys\11012

        print(newfilepath_mcu)
        print(newfilepath_resource)

        return newfilepath_mcu, newfilepath_resource

    def remove_file(self, filename):
            os.remove(filename)

    def rmtree_file(self, filename):
        shutil.rmtree(filename)

    def get_file(self):
        filespath = self.filespath + '\\' + 'Recent_res'        #C:\runner\Recent_res
        filelist = os.listdir(filespath)    #找到C:\runner\Recent_res底下所有的文件或者文件夹

        filepath = filespath + '\\' + filelist[0]   #C:\runner\Recent_res\11103

        return filepath     #C:\runner\Recent_res\11103

    def mkdir_file(self):                         #必须有初始资源包
        filepath = self.filespath + '\\' + 'Recent_res'
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
        else:
            self.rmdir_file(filepath)
        return filepath

    def rmdir_file(self, filepath):
        filelist = os.listdir(filepath)
        if filelist:
            for f in filelist:
                os.remove(filepath + '\\' + f)


    def copy_file(self, source, target):
        if self.unzip_src:
            copyfile(source, target)

if __name__ == '__main__':
    r = File(zip_src="C:\Test_Script\Project-Pycharm\ApiTest")
    # A.rename_zipname()
    # A.get_pathfiles()

    r.rename_zipname()
    # print(A.zip_src)
    # print(os.path.splitext(A.get_pathfiles())[0])
    # print(A.zip_src+"\\"+os.path.splitext(A.get_pathfiles())[0])


