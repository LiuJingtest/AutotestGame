# decoding:utf-8
# coding:utf-8
from __future__ import division
import cv2.cv as cv
import os

def rotate_img(sourcename):
    """
    旋转图片
    :param sourcename:图片名
    :return:
    """
    img = cv.LoadImage(sourcename)
    timg = cv.CreateImage((img.height,img.width), img.depth, img.channels)
    cv.Transpose(img, timg)
    cv.Flip(timg, timg, flipMode=0)
    cv.SaveImage(sourcename[0:-4] + "_rotate.jpg", timg)

def get_coors(img, temp, size, app_size):
    """
    获取坐标点
    :param img: 需要获得坐标的图片图片
    :param temp: 模板图片
    :return:    匹配模板的中心点坐标
    """
    source = cv.LoadImage(img)
    template = cv.LoadImage(temp)
    thumb = img_resize(template,app_size[1]/size[0],app_size[0]/size[1])

    W, H = cv.GetSize(source)
    w, h = cv.GetSize(thumb)
    width = W - w + 1
    height = H - h + 1
    result = cv.CreateImage((width, height), 32, 1)  # result是一个矩阵，用于存储模板与源图像每一帧相比较后的相似值

    cv.MatchTemplate(source,thumb, result, cv.CV_TM_SQDIFF)  # 从矩阵中找到相似值最小的点，从而定位出模板位置
    (min_x, max_y, minloc, maxloc) = cv.MinMaxLoc(result)
    (x, y) = minloc

    # 以下语句用来显示匹配的结果，匹配的模板用红色的矩形标出
    # cv.Rectangle(source, (int(x), int(y)), (int(x) + w, int(y) + h), (0, 0, 255), 2, 0) #use red rectangle to notify the target
    # cv.ShowImage(img[0:-4] + "result", source)
    # cv.WaitKey()
    return x + w / 2, y + h / 2

def img_resize(img, w_fscale, h_fscale):
    """
    自适应放缩模板图片
    :param img: 图片
    :param w_fscale:    width缩放比例
    :param h_fscale:    height缩放比例
    :return:    返回缩放的图片
    """
    img_w, img_h = cv.GetSize(img)
    print cv.GetSize(img)
    thumb = cv.CreateImage((int(img_w * w_fscale), int(img_h * h_fscale)), 8, 3)
    cv.Resize(img, thumb)
    return thumb
