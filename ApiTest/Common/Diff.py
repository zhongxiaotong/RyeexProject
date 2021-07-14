#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/7/3 15:12
# @Author : Greey
# @FileName: Diff.py.py
# -*- coding: utf-8 -*-

import io
import os
import time
import math
import base64
import hashlib
import hmac
import argparse

def getTimestamp(ms=False):
    if ms:
        return int(round(time.time() * 1000))
    else:
        return int(time.time())

def int_to_hex(int_number):
    if len(hex(int_number)) % 2 != 0:
        return '0{0:X}'.format(int_number)
    else:
        return '{0:X}'.format(int_number)

def byte_to_hex(bins, toLower=True):
    # ret = ''.join(["%02X" % x for x in bins]).strip()
    ret = bins.encode('hex').strip()
    if toLower:
        ret = ret.upper()
    return ret

def hex_to_int(hexStr):
    return int(hexStr, 16)

def hex_to_byte(hexStr):
    # return bytes.fromhex(hexStr)
    return hexStr.decode('hex')

def reverse_hex(hexStr):
    i = 0
    ret = ''
    while i < len(hexStr):
        ret = ''.join([hexStr[i:i + 2], ret])
        i = i + 2
    return ret

def md5(msg):
    sh = hashlib.md5()
    sh.update(msg)
    ret = sh.hexdigest()
    return ret.upper()

def leftPadding(string, length, padding):
    strLen = len(string)
    num = length - strLen
    if num > 0:
        for i in range(num):
            string = ''.join([padding, string])
    return string

def calculate_diff(source, target):
    diffList = []
    source_files = source.getObjectFileList()
    target_files = target.getObjectFileList()
    for item in source_files:
        delFlag = True
        for itemTarget in target_files:
            if item["name"] == itemTarget["name"]:
                delFlag = False
                if item["version"] != itemTarget["version"]:
                    diffList.append(itemTarget)
                break
        if delFlag:
            diffList.append({
                "name": item["name"],
                "version": ""
            })
    for item in target_files:
        hasFlag = False
        for itemOrig in source_files:
            if item["name"] == itemOrig["name"]:
                hasFlag = True
                break
        if not hasFlag:
            diffList.append({
                "name": item["name"],
                "version": item["version"]
            })
    return diffList

def create_diff_file(files, source_bin):
    source = b""
    targetFileList = source_bin.getFileList()
    for item in files:
        if item["version"] == '':
            source = b''.join([source, FirmResourceObject.getDeleteBinary(item["name"])])
        else:
            for fileObj in targetFileList:
                if fileObj.getName() == item["name"]:
                    source = b''.join([source, fileObj.toBinary()])
    return source

def calculate_firmware_diffv(source_file_bin, target_file_bin):
    source_file = FirmResourceBin(source_file_bin)
    target_file = FirmResourceBin(target_file_bin)

    filelist = calculate_diff(source=FirmResourceBin(source_file_bin),
        target=FirmResourceBin(target_file_bin))
    data = create_diff_file(filelist, target_file)

    return data

def writefile(filepath, data):
    if filepath:
        with open(filepath, "w") as f:
            f.write(data)
            f.close()
        return file

def readfile(filepath):
    if filepath:
        with open(filepath, "rb") as f:
            file = f.read()
            f.close()
        return file


class FirmResourceBin:

    def __init__(self, binary):
        self.binary = binary
        self.fileList = []
        self.explain()

    def explain(self):
        source = self.binary
        self.fileList = []
        while len(source) >= 8:
            head = byte_to_hex(source[:8])
            source = source[8:]

            magic = head[:4]
            if magic != 'ADDE':
                continue
            nameLen = hex_to_int(reverse_hex(head[4:8]))
            contentLen = hex_to_int(reverse_hex(head[8:]))

            fileName = source[:nameLen].decode()
            source = source[nameLen:]
            fileContent = source[:contentLen]
            source = source[contentLen:]

            self.fileList.append(FirmResourceObject(fileName, fileContent))

    def getFileList(self):
        return self.fileList

    def getObjectFileList(self):
        fileList = []
        for file in self.getFileList():
            fileList.append({
                "name": file.getName(),
                "version": file.getVersion()
            })
        return fileList

class FirmResourceObject:

    def __init__(self, name, content):
        self.name = name.strip('\x00')
        self.content = content
        self.version = md5(self.content)

    def toBinary(self):
        nameHex = byte_to_hex(self.name.encode())
        if nameHex[-2:] != '00':
            nameHex = ''.join([nameHex, '00'])
        name = hex_to_byte(nameHex)
        nameLen = len(name)
        contentLen = len(self.content)
        output = hex_to_byte('ADDE')
        output = b''.join([output, hex_to_byte(reverse_hex(leftPadding(int_to_hex(nameLen), 4, '0')))])
        output = b''.join([output, hex_to_byte(reverse_hex(leftPadding(int_to_hex(contentLen), 8, '0')))])
        output = b''.join([output, name])
        output = b''.join([output, self.content])
        return output

    def getName(self):
        return self.name

    def getContent(self):
        return self.content

    def getVersion(self):
        return self.version

    @staticmethod
    def getDeleteBinary(name):
        nameHex = byte_to_hex(name.encode())
        if nameHex[-2:] != '00':
            nameHex = ''.join([nameHex, '00'])
        name = hex_to_byte(nameHex)
        nameLen = len(name)
        contentLen = 0
        output = hex_to_byte('ADDE')
        output = b''.join([output, hex_to_byte(reverse_hex(leftPadding(int_to_hex(nameLen), 4, '0')))])
        output = b''.join([output, hex_to_byte(reverse_hex(leftPadding(int_to_hex(contentLen), 8, '0')))])
        output = b''.join([output, name])
        return output

def diff_res(source_bin, target_bin, save_bin):
    readfile(source_bin)
    readfile(source_bin)
    data = calculate_firmware_diffv(source_bin, target_bin)
    writefile(save_bin, data)



# if __name__ == '__main__':
#     diff_res('D:\\log\\381', 'D:\\log\\425', 'D:\\log\\381-425')





























