import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bot.png')
blur = cv2.blur(img,(5,5))
gaussian_blur =  cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.subplot(222),plt.imshow(blur),plt.title('Blurred')
plt.subplot(223),plt.imshow(gaussian_blur),plt.title('Gaussian Blurred')
plt.subplot(224),plt.imshow(median),plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()