import cv2

img = cv2.imread("resource/car.jpeg", 0)

cv2.imwrite("/Users/wangjuewei/Desktop/canny.jpg", cv2.Canny(img, img.shape[1], img.shape[0]))
cv2.imshow("canny", cv2.imread("/Users/wangjuewei/Desktop/canny.jpg"))

cv2.waitKey()
cv2.destroyAllWindows()
