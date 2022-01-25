import cv2

img = cv2.imread("BMW.jpg")

cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)

cv2.imshow("img", img)

cv2.waitKey(10)
 
 
cv2.destroyAllWindows()