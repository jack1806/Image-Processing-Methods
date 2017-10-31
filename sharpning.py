
import sys

sys.path.append('/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/satyak/Desktop/Image/two.jpeg')


kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
im = cv2.filter2D(img, -1, kernel)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im),plt.title('After Sharpning')
plt.xticks([]), plt.yticks([])

plt.show()