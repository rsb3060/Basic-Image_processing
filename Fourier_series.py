import cv2
import numpy as np
from matplotlib import pyplot as plt 
img = cv2.imread('dav27d.jpg',0)


##for performing fourier transform using numpy
f = np.fft.fft2(img)
##for taking the image to centre
fshift = np.fft.fftshift(f)
##to present magnitude of the component which is given by above 

magnitude_spectrum = 20*np.log(np.abs(fshift))

##to represnt original signal
##original_spectrum=20*np.log(np.abs(fshift))


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
##plt.subplot(122),plt.imshow(original_spectrum, cmap = 'gray')
##plt.title('original Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()



