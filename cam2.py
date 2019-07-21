import cv2 
cap=cv2.VideoCapture(0)
while cap.isOpened() :
    status,frame=cap.read()
    #converting image frame in grey scale
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('livegrey',grey)
    if cv2.waitKey(10) & 0xfff == ord('q') :
        break

# destroy all windows
cv2.destroyAllWindows()
# to close cameras
cap.release()
