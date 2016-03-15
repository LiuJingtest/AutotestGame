# decoding:utf-8
# coding:utf-8
from __future__ import division
import xlrd

def read_script(filename, sheetname):
    """
    读取脚本所在的excel
    :param filename: 脚本所在的excel的路径及名字
    :return: 返回截图所用手机的分辨率，脚本列表
    """
    workbook = xlrd.open_workbook(filename)
    booksheet = workbook.sheet_by_name(sheetname)
    i = 0
    size = []
    script = []
    while 1:
        row_data = booksheet.row_values(i)
        i += 1
        if row_data[0] == '截图分辨率'.decode('UTF-8'):
            size = [int(row_data[1]),int(row_data[2])]
        if row_data[0] != '截图分辨率'.decode('UTF-8') and row_data[0] != 'over' and row_data[0] != '是否截图'.decode('UTF-8'):
            map1 = {
                'type': row_data[1],
                'time': row_data[2],
                'img_name': row_data[3],
                'shoot': row_data[0]
            }
            script.append(map1)
        if row_data[0] == 'over':
            break
    return size, script
