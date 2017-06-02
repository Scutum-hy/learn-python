# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('D:/Python/photo/1.jpg')
px = img[100, 100]
print px
blue = img[100, 100, 0]
print blue
print img.item(10, 10, 2)
img.itemset((10, 10, 2), 105)
print img.item(10, 10, 2)
