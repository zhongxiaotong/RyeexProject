#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/6/11 18:22
# @Author : Greey
# @FileName: File.py


import zipfile
import os
import json


class File(object):

    def __init__(self):
        # self.zip_src = 'C:/runner/autotest'

        self.zip_src = 'D:\log'


    def get_pathfiles(self):
        filenames = os.listdir(self.zip_src)
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
                    fils = fz.extract(file, self.zip_src)
                    list.append(fils)
            return list
        except:
            raise

    def get_mcuversion(self):
        configfile = self.zip_src + "\\config.json"
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
        newfilename_mcu = self.zip_src + "\\" + self.get_mcuversion().encode('utf-8')
        newfilename_resource = self.zip_src + "\\" + newfilename_mcu.split('.')[3]
        for oldfilepath in filepaths:
            if '.fw.bin' in oldfilepath:
                os.rename(oldfilepath, newfilename_mcu)
        for oldfilepath in filepaths:
            if '.res' in oldfilepath:
                os.rename(oldfilepath, newfilename_resource)
        return newfilename_mcu, newfilename_resource

    def remove_file(self, filename):
        if self.zip_src:
            os.remove(self.zip_src + '\\' + filename)

    def mkdir_file(self):
        if self.zip_src:
            os.mkdir(self.zip_src + '\\' + 'Recent_res')

    def copy_file(self):
        if self.zip_src:
            os.copyfile


# if __name__ == '__main__':
#     A = File()
#     A.rename_zipname()
