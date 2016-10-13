import numpy as np
import cv2
img=cv2.imread('R:\WAllpaper\p2.jpg',1)



#Region of image

peack_face=img[33:100,70:185]
img[0:67,0:115]=peack_face
cv2.imshow("peack",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
