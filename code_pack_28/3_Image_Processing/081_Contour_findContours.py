import cv2
import numpy as np

img = cv2.imread('star.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)

print(contours)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()