import cv2 as cv
import sys

img = cv.resize(cv.imread("./.data/seulgi2.jpg"),dsize=(0,0),fx=0.5, fy =0.5)

if img is None:
    sys.exit("img is None")

def draw(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
    
    cv.imshow("seulgi",img)

cv.namedWindow("seulgi")



cv.imshow("seulgi",img)

cv.setMouseCallback("seulgi",draw)

while True:
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break