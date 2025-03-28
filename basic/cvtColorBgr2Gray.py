import cv2 as cv
import sys

img = cv.imread("./.data/seulgi.png")

if img is None:
    sys.exit("img is None")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray,dsize=(0,0),fx = 0.5,fy = 0.5)

cv.imwrite("seulgi_gray.png", gray)
cv.imwrite("seulgi_small.png", gray_small)

cv.imshow('color Image',img)
cv.imshow('Gray image', gray_small)

cv.waitKey()
cv.destroyAllWindows()