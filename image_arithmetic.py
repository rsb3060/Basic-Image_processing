import cv2
import numpy as np
import matplotlib.pyplot as plt


img1=cv2.imread('R:\WAllpaper\p2.jpg',1)
img2=cv2.imread('R:\WAllpaper\p3.jpg',1)
img3=cv2.imread('R:\WAllpaper\p1.jpg',1)

#add=img1+img2
#add=cv2.add(img1,img2)
#add=cv2.addWeighted(img1,0.6,img2,0.4,0)
print(img1.shape)
print(img2.shape)
#print(add.shape)

rows,cols,channels=img3.shape
roi=img1[0:rows,0:cols]

cv2.imshow("1",img3)
#logo image is load
img2gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imshow("2",img2gray)
#logo image is grey scaled

ret,mask=cv2.threshold(img2gray,50,255,cv2.THRESH_BINARY)
cv2.imshow("3",mask)
#logo image is masked i.e. if color of pixel greater than threshold it is 1
#we get white pixel which are needed to be shown or important  
##for light background it is cv2.THRESH_BINARY_INV
##for dark background it is cv2.THRESH_BINARY


mask_inv=cv2.bitwise_not(mask)
cv2.imshow("4",mask_inv)
#we inversed the mask to get unnessary pixel as white or 1

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
cv2.imshow("5",img1_bg)
#in roi we take the value of original pixel of roi if that pixel need not
#be changed so masked with inversed_masked and 0(black) if that pixel need to be chaged


img2_fg=cv2.bitwise_and(img3,img3,mask=mask)
cv2.imshow("6",img2_fg)
## now we take the logo portions image as original which are need not be canged
#and black for unnessary pixel

dst=cv2.add(img1_bg,img2_fg)
cv2.imshow("7",dst)
##we add img_fg,img_bg as bg contain black for those which need to be replaced
##and fg contain color to be replace

img1[0:rows,0:cols]=dst
cv2.imshow("8",img1)
## imgae pixel are changed

cv2.waitKey(0)
cv2.destroyAllWindows()
 
