import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Ovar.jpg')

ROI = img[300:400, 400:600]
img[0:100, 0:200] = ROI

plt.imshow(img)
plt.show()