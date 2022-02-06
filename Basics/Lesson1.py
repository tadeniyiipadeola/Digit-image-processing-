import cv2
import numpy as np


img = cv2.imread("BMW.jpg")
img2 = cv2.imread("BMW X5.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.waitKey(0)
# cv2.destroyAllWindows("img")
# cv2.destroyAllWindows("img2")


def image_shape():
   img = cv2.imread('BNW.jpg')
   print("The size of the image is ", img.shape)
   
def create_black_image():
   black_image = np.zeros((300,300), np.uint8)
   return black_image

def create_white_image():
   white_image = np.ones((300, 300), np.uint8)*255
   return white_image

def load_display(image):
   cv2.namedWindow("Test", cv2.WINDOW_AUTOSIZE)
   cv2.imshow("Test", image)
   cv2.waitKey(0)
   # cv2.destroyWindow("Test")

def sliceimage():
   sliceBMW = cv2.imread('BMW X5.jpg')
   load_display(sliceBMW)
   bmw_shape = sliceBMW.shape
   print(bmw_shape)
   half = bmw_shape[1]//2
   print(half)
   front = sliceBMW[0:543, 0:407]
   load_display(front)

if __name__ == "__main__":
   # white_image = create_white_image()
   # load_display(white_image)

   # black_image = create_black_image()
   # load_display(black_image)
   sliceimage()