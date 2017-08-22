import cv2
from cameo import filters

img = cv2.imread("resource/detail.png")

filters.strokeEdges(img, img)
curveFilter = filters.FindEdgesFilter()
curveFilter.apply(img, img)

cv2.imwrite("/Users/wangjuewei/Desktop/canny.jpg", img)

