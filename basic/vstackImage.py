import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("None")

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        print("exit")
        break

    cv.imshow("video",frame)

    key = cv.waitKey(1)

    if key == ord("c"):
        frames.append(frame)
    elif key == ord("q"):
        break

if len(frames)>1:
    imgs = frames[0]
    for i in range(1,min(3,len(frames))):
        imgs = np.vstack((imgs,frames[i]))
    
    imgs2 = cv.resize(imgs,dsize=(0,0), fx=0.5,fy=0.5)
    cv.imshow('vstackImage', imgs2)

    cv.waitKey() 

    cv.destroyAllWindows()