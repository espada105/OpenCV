import cv2 as cv
import sys

img = cv.imread("./.data/seulgi.png")

if img is None:
    sys.exit('img is None')

cv.rectangle(img,(100,30),(400,400),(0,0,255),2)

cv.putText(img,'hisseulgi',(100,440),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv.imshow("Draw",img)

cv.waitKey()
cv.destroyAllWindows()