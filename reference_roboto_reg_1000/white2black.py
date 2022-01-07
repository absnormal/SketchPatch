import numpy
import cv2

img = cv2.imread("./all.png", 0)

invert = cv2.bitwise_not(img)

cv2.imwrite("./allW.png", invert)
