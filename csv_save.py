import numpy as np
import cv2
import graphlab


img=cv2.imread('R:\WAllpaper\p2.jpg',1)
height, width = img.shape[:2]
b,g,r=cv2.split(img)
with open('R:\WAllpaper\image_data.csv',"w") as f:
    out_str="Height,Width,Red,Green,Blue"
    out_str += "\n"
    f.write(out_str)
    for i in range(height):
        for j in range(width):
            out_str=""
            out_str += str(i)
            out_str += ","+str(j)
            out_str += ","+str(r[i,j])
            out_str += ","+str(g[i,j])
            out_str += ","+str(b[i,j])
            out_str += "\n"
            f.write(out_str)

f.close()
s=graphlab.SFrame('R:\WAllpaper\image_data.csv')
print(s)


