'''
1.  zoom out a particular area of any image

'''


import cv2
filename = 'p1.jpg'
W = 1000.
oriimg = cv2.imread(filename)
height, width, depth = oriimg.shape
imgScale = W/width
newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
newimg = cv2.resize(oriimg,(int(newX),int(newY)))
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
#cv2.imwrite("resizeimg.jpg",newimg)

#newimg1=cv2.resize(oriimg[10:50,10:50],None,fx=newX*5,fy=newY*5,interpolation=cv2.INTER_LINEAR)
#cv2.imshow("show ",newimg1)
#cv2.waitKey(0)