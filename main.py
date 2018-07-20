import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('test.png',0)
img = cv.GaussianBlur(img, (25, 25),0)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
opening = cv.morphologyEx(th2, cv.MORPH_OPEN, kernel)


sobely = cv.Sobel(opening,cv.CV_64F,0,1,ksize=7)

cv.imshow('',sobely)
cv.waitKey(0)
cv.destroyAllWindows()
