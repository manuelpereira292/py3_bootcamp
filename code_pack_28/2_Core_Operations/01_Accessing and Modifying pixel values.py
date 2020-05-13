import cv2
import numpy as np
img = cv2.imread('Ovar.jpg')

px = img[100,100]
print(px)
#   B   G   R - Blue Green Red
# [215 154  20]


img[100,100] = [255,255,255]
print(img[100,100])