import cv2 
cap=cv2.VideoCapture(0)
while cap.isOpened() :
    status,frame=cap.read()
    #converting image frame in grey scale
    #grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # now we can draw all tools pattern
    #line
    cv2.line(frame,(0,0),(100,100),(0,255,0),5)
    # rectangle
    cv2.rectangle(frame,(50,50),(250,300),(0,0,255),2)
    cv2.imshow('livegrey',frame)
    if cv2.waitKey(0) & 0xff == ord('q') :
        break

# destroy all windows
cv2.destroyAllWindows()
# to close cameras
cap.release()
