#Lesson 2 is about cropping o slicing youre image
import cv2
import numpy as np

def load_display(image):
   cv2.namedWindow("Test", cv2.WINDOW_AUTOSIZE)
   cv2.imshow("Test", image)
   cv2.waitKey(0)
   #cv2.destroyWindow("Test")

def sliceimagefront(image):
   sliceBMW = cv2.imread(image)
#    load_display(sliceBMW)
   front = sliceBMW[0:543, 0:407]
   load_display(front)
   return front
   status = cv2.imwrite("front_bmw.jpg", front)
   print(status)

   
def sliceimageback(image):
   sliceBMW = cv2.imread(image)
#    load_display(sliceBMW)
   back = sliceBMW[0:543, 407:]
   load_display(back)
   return back
   status = cv2.imwrite("back_bmw.jpg", front)
   print(status)

def merge(image1, image2):
#    sliceBMW = cv2.imread(image1)
#    front = sliceBMW[0:543, 407:]
   load_display(image1)

#    sliceBMW = cv2.imread(image2)
#    back = sliceBMW[0:543, 0:407]
   load_display(image2)

   merge = np.concatenate((image1,image2), axis=1)
   load_display(merge)
   
if __name__ == "__main__":
#    sliceimagefront("BMW.jpg")
#    sliceimagefront("BMW.jpg")
#    sliceimageback('BMW X5.jpg')
#    sliceimageback('BMW.jpg')
   merge(sliceimagefront("BMW.jpg"), sliceimageback('BMW X5.jpg'))
   