#pip install opencv-contrib-python
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Ovar.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find the keypoints with FAST
kp = fast.detect(img,None)
print(kp[0])

# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
print( brief.descriptorSize() )
print( des.shape )
print(kp[0])