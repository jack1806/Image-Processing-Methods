import sys
import cv2
import numpy as np

img = cv2.imread("second.jpg", 0)

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imwrite("dilation.jpg",img_dilation)
cv2.imwrite("erosion.jpg",img_erosion)

