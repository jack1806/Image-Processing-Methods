
import sys

sys.path.append('/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/satyak/Desktop/Image/one.jpeg')

blur = cv2.blur(img,(5,5))#Averaging

#blur = cv2.GaussianBlur(img,(5,5),0)#Applying gaussian filter

#blur = cv2.medianBlur(img,5)#Applying median filter


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('After Smoothing')
plt.xticks([]), plt.yticks([])

plt.show()