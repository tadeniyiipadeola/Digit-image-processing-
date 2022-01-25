import cv2

img = cv2.imread("BMW.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Bimmer", img)

cv2.waitKey(0)
 
 
cv2.destroyAllWindows()