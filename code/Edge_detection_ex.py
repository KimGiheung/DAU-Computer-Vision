import cv2 as cv
import numpy as np
import skimage
import time

import skimage.future
# img     = cv.imread('C:\\Users\\ewqds\\Documents\\GitHub\\DAU-Computer-Vision\\data\\soccer.jpg')
# gray    = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# grad_x  = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)  #applicate sobel calculator
# grad_y  = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)
# #1. 에지 검출
# sobel_x = cv.convertScaleAbs(grad_x)
# sobel_y = cv.convertScaleAbs(grad_y)

# edge_strength=cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0) #에지 강도 계산

# cv.imshow('Original', gray)
# cv.imshow('sobelx', sobel_x)
# cv.imshow('sobely', sobel_y)
# cv.imshow('edge strength', edge_strength)

# # 2. 캐니 에지
# canny1=cv.Canny(gray,50,  150)   # Tlow는 50, Tigh는 150으로 설정
# canny2=cv.Canny(gray,100, 200)   # Tlow는 100, Tigh는 200으로 설정

# cv.imshow('Canny1', canny1)
# cv.imshow('Canny2', canny2)

# # 3. 직선 검출-1
# contour, hierarcgy = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# lcontour = []
# for i in range(len(contour)):
#     if contour[i].shape[0]>100: #길이가 100보다 크면
#         lcontour.append(contour[i])
# cv.drawContours(img, lcontour, -1, (0,255,0), 3)

# cv.imshow('Original with contours', img)
# cv.imshow('Canny', canny2)


# # 3. 직선 검출-2
# img     = cv.imread('C:\\Users\\ewqds\\Documents\\GitHub\\DAU-Computer-Vision\\data\\apples.jpg')
# gray    = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# apples  = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=150, param2=20, minRadius=50, maxRadius=120)

# for i in apples[0]:
#     cv.circle(img, (int(i[0]),int(i[1])), int(i[2]), (255,0,0), 2)
# cv.imshow('Apple detection', img)

img = skimage.data.coffee()
# cv.imshow('Coffe', cv.cvtColor(img, cv.COLOR_RGB2BGR))

# slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=600)
# sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
# sp_img1 = np.uint8(sp_img1*255.0)

# slic2 = skimage.segmentation.slic(img, compactness=80, n_segments=600)
# sp_img2 = skimage.segmentation.mark_boundaries(img, slic2)
# sp_img2 = np.uint8(sp_img2*255.0)

# cv.imshow('slic compact 20', cv.cvtColor(sp_img1, cv.COLOR_RGB2BGR))
# cv.imshow('slic compact 80', cv.cvtColor(sp_img2, cv.COLOR_RGB2BGR))


# # 최적화 분할: 정규화 절단 알고리즘을 이용한 영역 분할
# start = time.time()

# slic = skimage.segmentation.slic(img, compactness=20, n_segments=600, start_label=1)

# g = skimage.graph.rag_mean_color(img, slic, mode='similarity')
# ncut = skimage.graph.cut_normalized(slic, g)
# print(img.shape, 'image를 분할하는 데', time.time()-start, '초 소요')

# marking = skimage.segmentation.mark_boundaries(img, ncut)
# ncut_coffee = np.uint8(marking*255.0)

# cv.imshow('Normalized cut', cv.cvtColor(ncut_coffee, cv.COLOR_RGB2BGR))

# # 5. 대화식 분할
# # GrabCut을 이용한 대화식 분할
# src = skimage.data.coffee()

# mask = np.zeros(src.shape[:2], np.uint8)
# bgdModel = np.zeros((1,65), np.float64)
# fgdModel = np.zeros((1,65), np.float64)
# iterCount = 1
# mode = cv.GC_INIT_WITH_RECT

# rc = cv.selectROI(src)

# cv.grabCut(src, mask, rc, bgdModel, fgdModel, iterCount, mode)

# mask2 = np.where((mask==0)|(mask==2), 0, 1).astype('uint8')
# dst = src*mask2[:, :, np.newaxis]

# cv.imshow('dst', dst)

# def on_mouse(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.circle(dst, (x, y), 3, (255, 0, 0), -1)
#         cv.circle(mask, (x, y), 3, cv.GC_FGD, -1)
#         cv.imshow('dst', dst)
#     elif event == cv.EVENT_RBUTTONDOWN:
#         cv.circle(dst, (x, y), 3, (0, 0, 255), -1)
#         cv.circle(mask, (x, y), 3, cv.GC_FGD, -1)
#         cv.imshow('dst', dst)
#     elif event == cv.EVENT_MOUSEMOVE:
#         if flags & cv.EVENT_FLAG_LBUTTON:
#             cv.circle(dst, (x, y), 3, (255, 0, 0), -1)
#             cv.circle(mask, (x, y), 3, cv.GC_BGD, -1)
#             cv.imshow('dst', dst)
#         elif flags & cv.EVENT_FLAG_RBUTTON:
#             cv.circle(dst, (x, y), 3, (0, 0, 255), -1)
#             cv.circle(mask, (x, y), 3, cv.GC_BGD, -1)
#             cv.imshow('dst', dst)

# cv.setMouseCallback('dst', on_mouse)

# while True:
#     key = cv.waitKey()
#     if key ==13:
#         cv.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv.GC_INIT_WITH_MASK)
#         mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
#         dst = src*mask2[:, :, np.newaxis]
#         cv.imshow('dst', dst)
#     elif key == 27:
#         break

# 6. 영역 특징
# 이진 영역의 특징
orig = skimage.data.horse()
img = 255 - np.uint8(orig)*255
cv.imshow("Horse", img)

contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

img2 = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.drawContours(img2, contours, -1, (255, 0, 255), 2)
cv.imshow('Horse with contour', img2)

contour = contours[0]

m = cv.moments(contour)
area = cv.contourArea(contour)
cx, cy = m['m10']/m['m00'], m['m01']/m['m10']
perimeter = cv.arcLength(contour, True)
roundness = (4.0*np.pi*area)/(perimeter*perimeter)
print("area:", area, f'midpoint: ({cx}, {cy})', 'perimeter:', perimeter, 'roundness:', roundness)

img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

contour_approx = cv.approxPolyDP(contour, 8, True)
cv.drawContours(img3, [contour_approx], -1, (0, 255, 0), 2)

hull = cv.convexHull(contour)
hull = hull.reshape(1, hull.shape[0], hull.shape[2])
cv.drawContours(img3, hull, -1, (0, 0, 255), 2)

cv.imshow('Horse with line', img3)


cv.waitKey()
cv.destroyAllWindows()