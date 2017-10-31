from cv2 import *
import numpy as np

def write(s,i):
	imwrite(s,i)

def sharp(image):
	k1 = np.zeros((3,3),np.float32)
	k2 = np.ones((3,3),np.float32)/9.0
	k1[1,1] = 2.0
	k1 -= k2
	write("Sharpen.jpg",filter2D(image,-1,k1))

def smooth(image):
	fltr = np.ones((3,3),np.float32)/9.0
	dst = filter2D(image,-1,fltr)
	write("Smooth.jpg",dst)

p = imread("first.jpg")
p = resize(p,(800,500))
q = imread("second.jpg")
q = resize(q,(800,500))
s = imread("third.jpg")
s = resize(s,(800,500))
r = add(p,q)
r2 = add(r,s)
write("tmp.jpg",r2)
write("answer.jpg",r)
for i in r:
	for j in i:
		j+=255
write("dbt.jpg",r)
smooth(r)
sharp(r)
