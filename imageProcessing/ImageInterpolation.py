import cv2 as cv


img = cv.imread("./.data/frieren.png")
patch = img[250:350,170:270,:]

img = cv.rectangle(img, (170,250),(270,350),(255,0,0),3)

patch1 = cv.resize(patch,dsize=(0,0),fx=5,fy=5, interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch,dsize=(0,0),fx=5,fy=5, interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch,dsize=(0,0),fx=5,fy=5, interpolation=cv.INTER_CUBIC)
patch4 = cv.resize(patch,dsize=(0,0),fx=5,fy=5, interpolation=cv.INTER_LANCZOS4)

cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)
cv.imshow('Resize lanczos4', patch4)


cv.waitKey()
cv.destroyAllWindows()