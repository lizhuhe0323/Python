#coding: UTF-8
import os
import pygame
from pygame.locals import *

pygame.init()
text = u"PythonTab中文网"
#设置字体和字号
font = pygame.font.SysFont('Microsoft YaHei', 64)
#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))
#保存图片
pygame.image.save(ftext, "/home/lizhuhe/pythontab.jpg")