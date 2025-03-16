import skimage
import numpy as np
import cv2 as cv

orig = cv.imread('./.data/frieren.png')
cv.imshow('img',orig)
# 이미지를 그레이스케일로 변환 (findContours는 단일 채널 이미지 필요)
gray = cv.cvtColor(orig, cv.COLOR_BGR2GRAY)  # 추가: 이미지를 그레이스케일로 변환
# 이진화 수행
_, img = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)  # 추가: 이진화 처리
# img = 255 - np.uint8(orig) * 255  # 제거: 이 코드는 3채널 이미지에 적용 불가능

cv.imshow('Horse', img)

contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# 변경: img는 이미 그레이스케일이므로 BGR로 변환할 필요 없음
img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # 수정: 그레이스케일 → BGR 변환 유지
cv.drawContours(img2, contours, -1, (255,0,255), 2)
cv.imshow('Horse with contour', img2)

# 추가: contours가 비어있는지 확인
if len(contours) > 0:  # 추가: 외곽선이 있는지 확인
    contour = contours[0]

    m = cv.moments(contour)
    area = cv.contourArea(contour)
    # 추가: 0으로 나누기 방지
    if m['m00'] != 0:  # 추가: 0으로 나누기 방지
        cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
        perimeter = cv.arcLength(contour, True)
        roundness = (4.0 * np.pi * area)/(perimeter * perimeter)
        print('area=', area, '\n center=', cx, cy, '\n perimeter', perimeter, 'roundness', roundness)

        img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        contour_approx = cv.approxPolyDP(contour, 8, True)
        cv.drawContours(img3, [contour_approx], -1, (0,255,0), 2)

        hull = cv.convexHull(contour)
        hull = hull.reshape(1, hull.shape[0], hull.shape[2])
        cv.drawContours(img3, hull, -1, (0,0,255), 2)

        cv.imshow('horse with line segments and convex hull', img3)
else:
    print("외곽선을 찾을 수 없습니다.")  # 추가: 외곽선이 없는 경우 메시지 출력

cv.waitKey()
cv.destroyAllWindows()