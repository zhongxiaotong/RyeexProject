#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file_path=r"C:\Test_Script\RyeexProject\ApiTest\Log\2021-10-18.log"

file_list=[]

f=io.open(file_path,"r")
print(f.readlines())
for a in f.readlines():
    print(a)
    # if "Process-1" in a:
    #     print(a)
        # file_list.append(a.encode('gb2312'))
        # if "获取重启次数".decode("utf-8") in a:
        #     print(a)
# print(file_list)

f.close()