# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('D:/Python/photo/1.jpg', 1)
cv2.namedWindow('first', cv2.WINDOW_NORMAL)
cv2.imshow('first', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('yuan.png', img)
    cv2.destroyAllWindows()
