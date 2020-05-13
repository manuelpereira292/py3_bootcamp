import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Ovar.jpg')
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(RGB_img),plt.title('Original')
plt.subplot(122),plt.hist(img.ravel(),12,[0,12]),plt.title('Histogram')
plt.show()