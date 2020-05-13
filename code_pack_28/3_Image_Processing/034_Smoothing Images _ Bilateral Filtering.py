import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bot.png')
blur = cv2.blur(img,(5,5))
gaussian_blur =  cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.subplot(232),plt.imshow(blur),plt.title('Blurred')
plt.subplot(233),plt.imshow(gaussian_blur),plt.title('Gaussian Blurred')
plt.subplot(234),plt.imshow(median),plt.title('Median Blurred')
plt.subplot(235),plt.imshow(bilateral),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()