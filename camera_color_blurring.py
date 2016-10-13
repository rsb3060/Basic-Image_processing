import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([150 ,150 ,50])
    upper_red = np.array([180,255,150])

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)


    

    kernel=np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(res,-1,kernel)
    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    bilateral=cv2.bilateralFilter(res,15,75,75)
##    cv2.imshow('hue',h)
##    cv2.imshow('saturation',s)
##   cv2.imshow('value',v)
##   cv2.imshow('hsv',hsv)
    
    cv2.imshow('bilatral',bilateral)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
