import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([45,50, 120])
    upper_red=np.array([180, 255, 155])

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
##    cv2.imshow('hue',h)
##    cv2.imshow('saturation',s)
##    cv2.imshow('value',v)
##    cv2.imshow('hsv',hsv)
    cv2.imshow('frame',res)
    cv2.imshow('gray',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
