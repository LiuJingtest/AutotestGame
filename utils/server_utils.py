# coding:utf-8

import cmd_utils as cmd
import multiprocessing
import os


class Servers:
    def __init__(self):
        self.deviceList = cmd.getDeivcesName()
        self.bootstrapPortList = self.port(2233)
        self.appiumPortList = self.port(4450)
        self.list_cmd = self.create_cmd()

    def start_appium(self):
        """
        启动appium服务
        :return:
        """
        self.kill_server("node.exe")
        if len(self.list_cmd) > 0:
            for t in range(0,len(self.list_cmd)):
                pro = multiprocessing.Process(target=cmd.call_cmd, args=(self.list_cmd[t],))
                pro.start()
                pro.join(5)

    def create_cmd(self):
        """
        根据设备列表与可用端口号创建启动appium服务的命令行命令
        :return:
        """
        list_cmd = []
        for i in range(0,len(self.deviceList)):
            deviceList = self.deviceList[i].replace('.','_')
            deviceList = self.deviceList[i].replace(':','_')
            command = "appium -p " + str(self.appiumPortList[i]) + " -bp " + str(self.bootstrapPortList[i]) + " -U " + \
                      self.deviceList[i] + " >" + os.getcwd() + "\log\\" + deviceList + ".log";
            list_cmd.append(command)
        return list_cmd

    def kill_server(self,servername):
        """
        杀死进程服务
        :param servername: 待杀死的服务名
        :return:
        """
        cmd.call_cmd("taskkill -F -im " + servername)

    def isPortUsed(self,portNum):
        """
        判断可用端口
        :param portNum: 待判断的起始端口
        :return: 被占用则返回True
        """
        portRes = cmd.call_cmd("netstat -aon|findstr " + str(portNum))
        if len(portRes) <= 0:
            return False
        else:
            return True

    def port(self,start):
        """
        根据设备的数量获取可用端口列表
        :param start: 起始端口号
        :return: 返回可用端口列表
        """
        portList = []
        while len(portList) != len(self.deviceList):
            if start >=0 and start <= 65535:
                if not self.isPortUsed(start):
                    portList.append(start)
                start += 1
        return portList

    def get_port(self):
        """
        获取appium与设备连接的端口列表
        :return:
        """
        list_port = []
        for t in range(0,len(self.list_cmd)):
            list_port.append(self.list_cmd[t][10:15].strip())
        return list_port

    def get_devices(self):
        """
        获取设备列表
        :return: 返回设备列表
        """
        return self.deviceList

