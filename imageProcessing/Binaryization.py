import cv2 as cv
import sys

img = cv.imread("./.data/seulgi4.jpg")

t, bin_img = cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
print("최적 임계값",t)
cv.imshow('R channel123', img)
cv.imshow('R channel', img[:,:,2])
cv.imshow('R channel2', img[:,:,1])
cv.imshow('R channel3', img[:,:,0])
cv.imshow('R channel binarization', bin_img)


cv.waitKey()
cv.destroyAllWindows()
