import cv2
# starting camera
cap=cv2.VideoCapture(0)
# to check camera is started or not
if cap.isOpened():
    print("camera is ready to click")
else :
    print("check your web cam drivers")
# now we can read input from camera
# it will take first picture
print(cap.read())
# now showing captured input
status,img=cap.read()
cv2.imshow('liveimage',img)
cv2.waitKey(0)
# to close camera
cap.release()

