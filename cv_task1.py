'''
1. take  two image of same dimension
2.  cut the same part of image and replace it with each other

'''
import numpy as np
import cv2
img1=cv2.imread("p1.jpg")
img2=cv2.imread("p2.jpg")
cv2.imshow("image1",img1)
cv2.waitKey(0)
cv2.imshow("image2", img2)
cv2.waitKey(0)
y=int(0)
x=int(0)
h=int(100)
w=int(200)
# cropping img1
crop1 = img1[y:y+h, x:x+w]
tmp=crop1.copy()
cv2.imshow("cropped", tmp)
cv2.waitKey(0)
# cropping img2
crop2 = img2[y:y+h, x:x+w]
cv2.imshow("cropped", crop2)
cv2.waitKey(0)
#replacing images
img1[y:y+h, x:x+w]=crop2
cv2.imshow("image1", img1)
cv2.waitKey(0)
img2[y:y+h, x:x+w]=tmp
cv2.imshow("image2", img2)
cv2.waitKey(0)


# random replacement
