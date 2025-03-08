import cv2 as cv
import sys

img = cv.resize(cv.imread("./.data/seulgi2.jpg"),dsize = (0,0),fx = 0.5, fy=0.5)

if img is None:
    sys.exit("img is None")

brushsize=2

LColor,RColor = (255,0,0),(0,0,255)

def painting(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),brushsize,LColor,-1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),brushsize,RColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),brushsize,LColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),brushsize,RColor,-1)
    cv.imshow('seulgi',img)

cv.namedWindow('seulgi')
cv.imshow('seulgi',img)

cv.setMouseCallback('seulgi',painting)
while (True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
