#Lesson 2 is about cropping o slicing youre image
import cv2

def load_display(image):
   cv2.namedWindow("Test", cv2.WINDOW_AUTOSIZE)
   cv2.imshow("Test", image)
   cv2.waitKey(0)
   #cv2.destroyWindow("Test")

def sliceimagefront(image):
   sliceBMW = cv2.imread(image)
   load_display(sliceBMW)
   front = sliceBMW[0:543, 0:407]
   load_display(front)
   
def sliceimageback(image):
   sliceBMW = cv2.imread(image)
   load_display(sliceBMW)
   front = sliceBMW[0:543, 407:]
   load_display(front)

   
if __name__ == "__main__":
   sliceimagefront("BMW X5.jpg")
   sliceimagefront("BMW.jpg")
   sliceimageback('BMW X5.jpg')
   sliceimageback('BMW.jpg')
   