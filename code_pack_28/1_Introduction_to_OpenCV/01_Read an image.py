#pip install opencv-python

import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('Ovar.jpg',cv2.IMREAD_UNCHANGED)
# img = cv2.imread('Ovar.jpg',cv2.IMREAD_GRAYSCALE)

#Display an image
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()