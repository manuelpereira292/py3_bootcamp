import numpy as np
import cv2

img = cv2.imread('Ovar.jpg',0)

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = img.copy()
for marker in kp:
	img2 = cv2.drawMarker(img2, tuple(int(i) for i in marker.pt), color=(0, 255, 0))

cv2.imshow('ORB (Oriented FAST and Rotated BRIEF)',img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
