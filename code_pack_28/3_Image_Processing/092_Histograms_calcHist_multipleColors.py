import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Ovar.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.subplot(122),plt.plot(histr,color = col),plt.title('Histogram')
    plt.xlim([0,256])


RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(RGB_img),plt.title('Original')
plt.show()