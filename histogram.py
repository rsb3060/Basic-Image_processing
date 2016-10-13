import cv2
import numpy as np
from matplotlib import pyplot as plt 
img = cv2.imread('bookpage.jpg',0)
cv2.imshow("old_image",img)
##Now we need to flatten the image(put into single array,bins number of
##equal width value, range of value
hist,bins = np.histogram(img.flatten(),255,[0,255])

##this is to find cummalitive density function
cdf = hist.cumsum()

##to convert it into probablity or 0 to 1 range
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),255,[0,255], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

##Now we need to change the value in each bin point or pixel point
##for all pixel which has intensity 200 will be mapped to to new one
##or will be multiplied by 0 to 1
cdf_m = np.ma.masked_equal(cdf,0)
##process of equalization
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
##changing the intensity value as per change required according to equalisation
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

cv2.imshow("newimage",img2)

hist,bins = np.histogram(img2.flatten(),255,[0,255])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),255,[0,255], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

print(cdf_m)
cv2.waitKey(0)
cv2.destroyAllWindows()



