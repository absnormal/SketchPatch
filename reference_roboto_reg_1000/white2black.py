import numpy
import cv2

img = cv2.imread("./Z.png", 0)

invert = cv2.bitwise_not(img)

cv2.imwrite("./Zw.png", invert)
