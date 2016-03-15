# coding:utf-8
from appium import webdriver
import server_utils as ser
import excel_utils as ex
import img_utils as img
import time
import threading
import json
import os

class Driver(threading.Thread):
    """
    启动appium与手机app所对应的driver
    """
    def __init__(self, udid, port):
        # self.android
        threading.Thread.__init__(self)
        self.driver = None
        self.udid = udid
        self.port = port
        self.desired_caps = {}

    def set_desiredcaps(self):
        """
        设置参数
        :return:
        """
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4.2',
            'deviceName': self.udid,
            'appPackage': 'com.supernano.mt',
            'appActivity': 'com.supernano.mt.UnityPlayerNativeActivity',
            'udid': self.udid,
            'newCommandTimeout': 300
        }

    def run(self):
        """
        启动driver
        :return:
        """
        self.set_desiredcaps()
        #if s["flag"] == 1:
        self.driver = webdriver.Remote(s['romete_url'] + ':' + str(self.port)+'/wd/hub', self.desired_caps)
       # else:
          #  self.driver = webdriver.Remote(s['romete_url'] + ':' + s['romete']['port'] +'/wd/hub', self.desired_caps)
        time.sleep(s['app_waittime'])
        print "开始执行脚本"
        self.scriptDo()
        self.driver.quit()

    def get_driver(self):
        """
        返回driver
        :return: driver
        """
        return self.driver

    def getSize(self):
        """
        获取手机分辨率
        :return: 返回分辨率数组
        """
        app_size = [self.driver.get_window_size().get('width'), self.driver.get_window_size().get('height')]
        return app_size

    def scriptDo(self):
        """
        excel脚本执行函数
        （暂时只有点击的操作，后续有需求再更新）
        :return:
        """
        app_size = self.getSize()
        size, script = ex.read_script(os.getcwd() + '\script' + '\\' + s['script'], s['sheetname'])
        print size, app_size

        for j in range(0,len(script)):
            if script[j]['shoot'] == 'Y':
                self.driver.get_screenshot_as_file(os.getcwd() + '\script\img' + '\\' + self.udid + '_' + 'res.jpg')
            if script[j]['type'] == 'click':
                img.rotate_img(os.getcwd() + '\script\img' + '\\' + self.udid + '_' + 'res.jpg')
                print script[j]['img_name']
                x, y = img.get_coors(os.getcwd() + '\script\img' + '\\' + self.udid + '_' + 'res_rotate.jpg', script[j]['img_name'], size, app_size)
                self.driver.tap([(x, y)], 500)
            time.sleep(script[j]['time'])


s = json.load(file("config.json"))


