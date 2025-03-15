import cv2 as cv
img = cv.imread('./.data/seulgi3.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

grad_x = cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)
grad_y = cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

edge_strength = cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)

cv.imshow('gray', gray)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)
cv.imshow('edge_strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()