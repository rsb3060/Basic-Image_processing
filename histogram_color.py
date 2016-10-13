import cv2
import numpy as np
from matplotlib import pyplot as plt 
img = cv2.imread('bookpage.jpg',1)
cv2.imshow("old image",img)
b,g,r=cv2.split(img)
##Now we need to flatten the image(put into single array,bins number of
##equal width value, range of value

histb,bins = np.histogram(b.flatten(),256,[0,256])
histg,bins = np.histogram(g.flatten(),256,[0,256])
histr,bins = np.histogram(r.flatten(),256,[0,256])

##this is to find cummalitive density function
cdfb = histb.cumsum()
cdfg = histg.cumsum()
cdfr = histr.cumsum()
##to convert it into probablity or 0 to 1 range
cdf_normalized_b = cdfb * histb.max()/ cdfb.max()
cdf_normalized_g = cdfg * histg.max()/ cdfg.max()
cdf_normalized_r = cdfr * histr.max()/ cdfr.max()

plt.plot(cdf_normalized_b, color = 'b')
plt.plot(cdf_normalized_g, color = 'g')
plt.plot(cdf_normalized_r, color = 'r')
plt.hist(b.flatten(),256,[0,256], color = 'b')
plt.hist(g.flatten(),256,[0,256], color = 'g')
plt.hist(r.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

##Now we need to change the value in each bin point or pixel point
##for all pixel which has intensity 200 will be mapped to to new one
##or will be multiplied by 0 to 1
cdf_m_b = np.ma.masked_equal(cdfb,0)
cdf_m_g = np.ma.masked_equal(cdfg,0)
cdf_m_r = np.ma.masked_equal(cdfr,0)

##process of equalization
cdf_m_b = (cdf_m_b- cdf_m_b.min())*256/(cdf_m_b.max()-cdf_m_b.min())
cdf_m_g = (cdf_m_g- cdf_m_g.min())*256/(cdf_m_g.max()-cdf_m_g.min())
cdf_m_r = (cdf_m_r- cdf_m_r.min())*256/(cdf_m_r.max()-cdf_m_r.min())
##changing the intensity value as per change required according to equalisation
cdf_b = np.ma.filled(cdf_m_b,0).astype('uint8')
cdf_g = np.ma.filled(cdf_m_g,0).astype('uint8')
cdf_r= np.ma.filled(cdf_m_r,0).astype('uint8')
comp_b = cdf_b[b]
comp_g = cdf_g[g]
comp_r = cdf_r[r]

img2=cv2.merge([comp_r,comp_g,comp_b])

cv2.imshow("newimage",img2)

##displaying the histogram of new images
b,g,r=cv2.split(img2)

histb,bins = np.histogram(b.flatten(),256,[0,256])
histg,bins = np.histogram(g.flatten(),256,[0,256])
histr,bins = np.histogram(r.flatten(),256,[0,256])

cdfb = histb.cumsum()
cdfg = histg.cumsum()
cdfr = histr.cumsum()

cdf_normalized_b = cdfb * histb.max()/ cdfb.max()
cdf_normalized_g = cdfg * histg.max()/ cdfg.max()
cdf_normalized_r = cdfr * histr.max()/ cdfr.max()

plt.plot(cdf_normalized_b, color = 'b')
plt.plot(cdf_normalized_g, color = 'g')
plt.plot(cdf_normalized_r, color = 'r')
plt.hist(b.flatten(),256,[0,256], color = 'b')
plt.hist(g.flatten(),256,[0,256], color = 'g')
plt.hist(r.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()



