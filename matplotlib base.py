# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/Python/photo/2.jpg', 1)
img2 = img[:, :, ::-1]
plt.imshow(img2, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()


cv2.destroyAllWindows()
