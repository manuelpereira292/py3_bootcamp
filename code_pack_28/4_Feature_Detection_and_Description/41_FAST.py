import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Ovar.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = img.copy()
for marker in kp:
	img2 = cv2.drawMarker(img2, tuple(int(i) for i in marker.pt), color=(0, 255, 0))

# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
cv2.imshow('Total Keypoints with nonmaxSuppression',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = img.copy()
for marker in kp:
	img3 = cv2.drawMarker(img3, tuple(int(i) for i in marker.pt), color=(0, 255, 0))

cv2.imshow('Total Keypoints without nonmaxSuppression',img3)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
