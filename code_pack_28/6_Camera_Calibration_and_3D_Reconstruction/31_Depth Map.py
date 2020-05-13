import numpy as np
import cv2

# Load the left and right images in gray scale
imgLeft = cv2.imread('tsukuba_l.png', 0)
imgRight = cv2.imread('tsukuba_r.png', 0)

# Initialize the stereo block matching object 
stereo = cv2.StereoBM_create(numDisparities=32, blockSize=13)

# Compute the disparity image
disparity = stereo.compute(imgLeft, imgRight)

# Normalize the image for representation
min = disparity.min()
max = disparity.max()
disparity = np.uint8(255 * (disparity - min) / (max - min))

# Display the result
cv2.imshow('disparity', np.hstack((imgLeft, imgRight, disparity)))
cv2.waitKey(0)
cv2.destroyAllWindows()
