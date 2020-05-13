import cv2
import numpy as np
#from matplotlib import pyplot

img = cv2.imread('Ovar.jpg')
res = cv2.resize(img,None,fx=0.5, fy=2, interpolation = cv2.INTER_CUBIC)

#OR
# height, width = img.shape[:2]
# res = cv2.resize(img,(2 * width, 2 * height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('image',img)
cv2.imshow('res_image',res)

cv2.waitKey(0)
cv2.destroyAllWindows()