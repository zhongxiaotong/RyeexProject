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
        self.zip_src = zip_src
        self.filespath = 'C:\\runner'
        self.unzip_src = self.zip_src + '\\' + os.path.splitext(self.get_pathfiles())[0]


    def get_pathfiles(self):
        filenames = os.listdir(self.zip_src)    #

        if filenames:
            for filename in filenames:
                if '.zip' in filename:
                    return filename

    def unzip_file(self):
        srcfile = self.zip_src + '\\' + self.get_pathfiles()
        list = []
        r = zipfile.is_zipfile(srcfile)
        try:
            if r:
                fz = zipfile.ZipFile(srcfile, 'r')
                for file in fz.namelist():
                    fils = fz.extract(file, self.unzip_src)
                    list.append(fils)
            return list
        except:
            raise

    def get_mcuversion(self):
        configfile = self.unzip_src + "\\config.json"
        try:
            if configfile:
                with open(configfile, 'r') as f:
                    f_dict = json.load(f)
                    f.close()
                    return f_dict['version']
        except:
            raise

    def rename_zipname(self):
        filepaths = self.unzip_file()
        newfilepath_mcu = self.unzip_src + "\\" + self.get_mcuversion().encode('utf-8')
        newfilepath_resource = self.unzip_src + "\\" + self.get_mcuversion().encode('utf-8').split('.')[3]
        for oldfilepath in filepaths:
            if '.fw.bin' in oldfilepath:
                os.rename(oldfilepath, newfilepath_mcu)
        for oldfilepath in filepaths:
            if '.res' in oldfilepath:
                os.rename(oldfilepath, newfilepath_resource)
        return newfilepath_mcu, newfilepath_resource

    def remove_file(self, filename):
            os.remove(filename)

    def rmtree_file(self, filename):
        shutil.rmtree(filename)

    def get_file(self):
        filespath = self.filespath + '\\' + 'Recent_res'
        filelist = os.listdir(filespath)
        filepath = filespath + '\\' + filelist[0]
        return filepath

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
    A = File()
    # A.rename_zipname()
    A.get_pathfiles()