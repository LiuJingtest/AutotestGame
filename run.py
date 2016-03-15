# coding:utf-8
from utils import driver_utils as dr,excel_utils as ex,server_utils as ser,img_utils as img
import json

if __name__ == '__main__':
    #s = json.load(file("config.json"))
    server = ser.Servers()
    print server.create_cmd()
    server.start_appium()
    num = server.get_devices()
    port = server.get_port()
    list_driver = []
    for i in range(0,len(num)):
        list_driver.append(dr.Driver(num[i],port[i]))
        list_driver[i].start()
