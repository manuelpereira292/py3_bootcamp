import cv2
import numpy as np

img = cv2.imread('Ovar.jpg',0)

# Create SURF object. You can specify params here or later.
# Here set Hessian Threshold to 400
surf = cv2.xfeatures2d.SURF_create(400)

# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)
len(kp) 
#  699
# 1199 keypoints is too much to show in a picture. We reduce it to some 50 to draw it on an image. While matching, we may need all those features, but not now. So we increase the Hessian Threshold.

# Check present Hessian threshold
print( surf.getHessianThreshold() )
# 400.0

# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.setHessianThreshold(50000)

# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img,None)
print( len(kp) )
# 47
# It is less than 50. Let's draw it on the image.

img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

# Check upright flag, if it False, set it to True
print( surf.getUpright() )
# False
surf.setUpright(True)

# Recompute the feature points and draw it
kp = surf.detect(img,None)
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()
#All the orientations are shown in same direction. 
# It is faster than previous. If you are working on cases where orientation is not a problem (like panorama stitching) etc, this is better.

# Find size of descriptor
print( surf.descriptorSize() )
# 64

# That means flag, "extended" is False.
surf.getExtended()
#  False

# So we make it to True to get 128-dim descriptors.
surf.setExtended(True)
kp, des = surf.detectAndCompute(img,None)
print( surf.descriptorSize() )
# 128

print( des.shape )
# (47, 128)