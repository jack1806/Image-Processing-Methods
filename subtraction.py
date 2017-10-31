from PIL import Image
from numpy import *

im1 = Image.open('/home/satyak/Desktop/Image/one.jpeg')
im2 = Image.open('/home/satyak/Desktop/Image/two.jpeg')

im1arr = asarray(im1)
im2arr = asarray(im2)

sub = im1arr - im2arr

resultImage = Image.fromarray(sub)
resultImage.save('/home/satyak/Desktop/Image/subtracted.jpeg')

