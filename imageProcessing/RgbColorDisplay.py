import cv2 as cv
import sys

img = cv.resize(cv.imread("./.data/seulgi3.jpg"),dsize=(0,0),fx=0.3, fy=0.3)

if img is None:
    sys.exit("img is None")

cv.imshow("seulgi",img)

cv.imshow("seulgi upper left half",img[0:img.shape[0]//2, 0:img.shape[1]//2,:])

cv.imshow("seulgi Center half", img[img.shape[0]//4:3 * img.shape[0]//4, img.shape[1]//4:3 * img.shape[1]//4,:])

cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()