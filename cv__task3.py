'''
1. find the difference between two images
2. add two image and make a single image
'''
import cv2
img1=cv2.imread('p1.jpg')
img2=cv2.imread('p2.jpg')
diff=img1-img2
cv2.imshow("difference",diff)
cv2.waitKey(0)
add=img1+img2
cv2.imshow('addition',add)
cv2.waitKey(0)