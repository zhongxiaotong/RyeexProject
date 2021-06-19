#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/6/11 18:22
# @Author : Greey
# @FileName: test.py


import zipfile
import os

def unzip_file(zip_src, filename):
    srcfile = zip_src + '\\' + filename
    r = zipfile.is_zipfile(srcfile)
    if r:
        fz = zipfile.ZipFile(srcfile, 'r')
        for file in fz.namelist():
            fz.extract(file, zip_src)

zip_src = "C:\\Users\\EDZ\\Downloads"
filename = "realme1.3.0.503.zip"


path = "C:\\Users\\EDZ\\Downloads"
datanames = os.listdir(path)
for i in datanames:
    print(i)

# unzip_file(zip_src, filename)
#
# os.rename("C:\\Users\\EDZ\\Downloads\\1.3.0.503.fw.bin", "C:\\Users\\EDZ\\Downloads\\1.3.0.503")

os.remove("C:\\Users\\EDZ\\Downloads\\1.3.0.503")
