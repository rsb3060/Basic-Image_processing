import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('R:\WAllpaper\p2.jpg',1)
cv2.line(img,(0,0),(249,155),(255,255,255),15)
cv2.rectangle(img,(0,0),(249,155),(0,255,0),15)
cv2.circle(img,(145,50),55,(255,0,0),-1)
pts=np.array([[10,5],[145,50],[185,70],[249,155]],np.int32)
#pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font=cv2.FONT_ITALIC

cv2.putText(img,"peackok",(100,33),font,1,(200,255,255),5,cv2.LINE_4)
peack_face=img[33:100,70:185]

cv2.imshow("peack",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

