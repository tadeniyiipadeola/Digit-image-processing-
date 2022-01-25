import numpy as np
import cv2

img = cv2.imread("BMW.jpg")

cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)

cv2.imshow("img", img)

cv2.waitKey(10)
 
 
cv2.destroyAllWindows()


def image_shape():
   img = cv2.imread('BNW>jpg')
   print("The size of the image is ",img.shape)
   
def create_black_image():
   black_image = np.zero((300,300), np.uint8)
   