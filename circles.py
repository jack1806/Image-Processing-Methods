#!/usr/bin/python3

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to image")
args = vars(ap.parse_args())

print("Now Starting..")

if args["image"] is None:
    loc = "images/"+str(input("Image location : "))
else:
    loc = args["image"]

im = cv2.imread(loc)
output = im.copy()
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 205, 255, cv2.THRESH_BINARY)

cv2.imwrite(loc.split(".")[0]+"_threshold.jpg", thresh)
print("Threshold image written in file system")

print("Getting circles from Threshold image.")
circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1.2, 15)

if circles is None:
    print("No Circles were found hence trying with the gray scale.")
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 15)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    print("Totally ", len(circles), "circles are found in the image.")
    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 1)
        cv2.rectangle(output, (x - 1, y - 1), (x + 1, y + 1), (0, 128, 255), -1)
    cv2.imshow("output", output)
    cv2.imwrite(loc.split(".")[0]+"_output.jpg", output)
    press = cv2.waitKey(0)
    if press == 'q':
        exit()
else:
    print("No Circles found hence no output file is generated")
