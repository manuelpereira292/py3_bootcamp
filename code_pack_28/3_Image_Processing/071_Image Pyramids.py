import cv2
import numpy as np,sys

img = cv2.imread('Ovar.jpg')
lower_reso = cv2.pyrDown(img)
higher_res = cv2.pyrUp(img)

cv2.imshow('Base', img)
cv2.imshow('Lower Res',lower_reso)
cv2.imshow('Higher Res',higher_res)

cv2.waitKey(0)
cv2.destroyAllWindows()