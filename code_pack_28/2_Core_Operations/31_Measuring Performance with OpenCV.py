import cv2

e1 = cv2.getTickCount()

# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

img1 = cv2.imread('Ovar.jpg')
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)  # 1.7040968s

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()