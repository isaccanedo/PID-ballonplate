import cv2 as cv
import numpy as np 

cap = cv.VideoCapture('imagetest.jpeg')
ret, frame = cap.read()

#cv.imshow("Og image", frame)
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
lower_value = np.array([00,125,90])
higher_value = np.array([50,255,255])
mask = cv.inRange(hsv, lower_value, higher_value)
circles = cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 2, 500, param1=300,param2=30,minRadius=30,maxRadius=40)
if type(circles) == np.ndarray and circles.size != 0:
    print("john")
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
            # draw the outer circle
            cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(frame,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles', frame)
k = cv.waitKey(0)
cap.release()