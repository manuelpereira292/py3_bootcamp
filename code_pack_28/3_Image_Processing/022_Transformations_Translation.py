import cv2
import numpy as np
from matplotlib import pyplot

img = cv2.imread('Ovar.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

pyplot.subplot(121),pyplot.imshow(img),pyplot.title('Input')
pyplot.subplot(122),pyplot.imshow(dst),pyplot.title('Output')
pyplot.show()