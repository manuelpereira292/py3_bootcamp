import cv2
import numpy as np
from matplotlib import pyplot

img = cv2.imread('Ovar.jpg',-1)
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))

pyplot.subplot(121),pyplot.imshow(img),pyplot.title('Input')
pyplot.subplot(122),pyplot.imshow(dst),pyplot.title('Output')
pyplot.show()