import cv2
import numpy as np
from matplotlib import pyplot as plt

gray_img = cv2.imread('Bridge_25_de_Abril.JPG', 0 ) #cv2.IMREAD_GRAYSCALE)
imS = cv2.resize(gray_img, (1024,768))
cv2.imshow('25_de_Abril',imS)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.hist(gray_img.ravel(),256,[0,256])
# hist = cv2.calcHist([gray_img],[0],None,[64],[0,64])
# plt.hist(gray_img.ravel(),64,[0,64])

plt.title('Histogram for gray scale picture')
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit 
cv2.destroyAllWindows()