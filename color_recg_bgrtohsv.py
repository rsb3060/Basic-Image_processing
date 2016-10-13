import cv2
import numpy as np
green = np.uint8([[[59, 60, 80]]])
green2 = np.uint8([[[23, 28, 28]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
hsv_green2 = cv2.cvtColor(green2,cv2.COLOR_BGR2HSV)
print hsv_green
print hsv_green2

