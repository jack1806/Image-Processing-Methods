# Created By jack_1806

# 13 Aug 2017


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

p = imread("first.jpg",0)
p = resize(p,(800,500))
q = imread("second.jpg",0)
q = resize(q,(800,500))
r = add(p,q)
write("answer.jpg",r)
smooth(r)
sharp(r)
