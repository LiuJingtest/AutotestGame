# coding:utf-8

import os
import time
import subprocess

def call_adb(command, *devicename):
    """
    运行adb命令
    :param command: 命令
    :param devicename: 设备名(可变参数)
    :return: 返回运行结果
    """
    getDeivcesName()
    command_result = ''
    if devicename == None:
         command_text = "adb -s %s" % (command)
    else:
        command_text = "adb -s %s %s" % (devicename, command)
    results = os.popen(command_text, "r")
    print results
    while 1:
        line = results.readline()
        print line
        if not line:
            break
        command_result += line
    return command_result

def call_cmd(command):
    """
    执行cmd命令
    :param command: cmd命令
    :return:    返回命令行返回值
    """
    command_result = ''
    command_text = "%s" % (command)
    results = os.popen(command_text, "r")
    while 1:
        line = results.readline()
        if not line:
            break
        command_result += line
    return command_result

def getDeivcesName():
    """
    获得手机驱动的名称
    :return:设备名
    """
    deviceName = []
    deviceText = os.popen('adb devices')
    textList = deviceText.readlines()
    for i in range(1,len(textList)-1):
        deviceName.append(textList[i].split()[0])
        print deviceName
    return deviceName


