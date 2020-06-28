import os
from math import *
import math




def rotate(angle, x, y):
    """
    基于原点的弧度旋转
    :param angle:   弧度
    :param x:       x
    :param y:       y
    :return:
    """
    rotatex = math.cos(angle) * x - math.sin(angle) * y
    rotatey = math.cos(angle) * y + math.sin(angle) * x
    return rotatex, rotatey


def xy_rorate(theta, x, y, centerx, centery):
    """
    针对中心点进行旋转
    :param theta:
    :param x:
    :param y:
    :param centerx:
    :param centery:
    :return:
    """
    r_x, r_y = rotate(theta, x - centerx, y - centery)
    return centerx + r_x, centery + r_y


def rec_rotate(x, y, width, height, theta):
    """
    传入矩形的x,y和宽度高度，弧度，转成QUAD格式
    :param x:
    :param y:
    :param width:
    :param height:
    :param theta:
    :return:
    """
    centerx = x + width / 2
    centery = y + height / 2

    x1, y1 = xy_rorate(theta, x, y, centerx, centery)
    x2, y2 = xy_rorate(theta, x + width, y, centerx, centery)
    x3, y3 = xy_rorate(theta, x, y + height, centerx, centery)
    x4, y4 = xy_rorate(theta, x + width, y + height, centerx, centery)

    return x1, y1, x3, y3, x4, y4, x2, y2


filePath = './text_gt/'
list_jpg = os.listdir(filePath)
for i in list_jpg:
    filename = os.path.join(filePath,i)

    f = open(filename, 'r')
    savestr = ''
    for line in f:
        line = line.strip()
        line = line.split(' ')
        line = list(map(float, line))
        x, y = line[2], line[3]
        w, h = line[4], line[5]
        # centralx=x+w/2
        # centraly = y + h / 2
        points = [x, y, x, y + h, x + w, y + h, x + w, y]
        pointsrotate = rec_rotate(x, y, w, h, line[-1])
        savestr = savestr + str(int(pointsrotate[0])) + ',' + str(int(pointsrotate[1])) + ',' + str(
            int(pointsrotate[2])) + ',' + str(int(pointsrotate[3])) + ',' + str(int(pointsrotate[4])) + ',' + str(
            int(pointsrotate[5])) + ',' + str(int(pointsrotate[6])) + ',' + str(int(pointsrotate[7])) + ',' + 'text\n'
    savename = 'gt_'+i[4:-2] + 'txt'
    savef = open(savename, 'w')
    savef.write(savestr)
    savef.close()