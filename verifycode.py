#coding: UTF-8
import os
import pygame
from pygame.locals import *
import random

seed = "1234567890abcdefghigklmnopqrstuvwxyzABCDEGHIJKLMNOPQRSTUVWXYZ"
pygame.init()
text = str(random.choice(seed)+random.choice(seed)+random.choice(seed)+random.choice(seed))
#设置字体和字号
font = pygame.font.SysFont('Microsoft YaHei', 64)
#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))
#保存图片
pygame.image.save(ftext, "/home/lizhuhe/pythontab.jpg")

typein = input('input your verify code:')

if typein == text:
    print ("OK!")
else:
    print ("Error!")