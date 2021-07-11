import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def empty(a):
    pass

status = ["No Mask",""]
count = 0

object_detector= cv2.createBackgroundSubtractorMOG2()

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,179,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)



while True:
    success,img = cap.read()

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")


    lower = np.array([1,0,255])
    upper = np.array([179,3,255])
    mask = cv2.inRange(imgHSV,lower,upper)

    contors,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contors:
        # Calculate Area and remove small elements

        area = cv2.contourArea(cnt)
        print(area)
        if area > 300:
            # cv2.drawContours(highwayvideo, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(img,"Mask OK",(250,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,color=(0,255,0))
            count = 1


        if area < 10:
            cv2.putText(img, status[count], (250, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, color=(0, 255, 255))





    cv2.imshow("Camera",img)
    cv2.imshow("Mask", mask)
    #cv2.imshow("imgHSV", imgHSV)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break