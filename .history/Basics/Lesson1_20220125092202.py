import cv2

img = cv2.imread("BMW.jpg", cv2.IMREAD_ANYCOLOR)

cv2.imshow("Bimmer", img)

cv2.waitKey(0)
 