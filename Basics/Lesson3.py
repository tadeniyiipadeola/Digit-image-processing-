# for this lesson We will be concatrnating to images using the cv2.hconcat function
from Lesson2 import load_display

import cv2
import numpy as np

def sliceimagefront(image):
   sliceBMW = cv2.imread(image)
   front = sliceBMW[0:543, 0:407]
   load_display(front)
   return front

def sliceimageback(image):
   sliceBMW = cv2.imread(image)
#    load_display(sliceBMW)
   back = sliceBMW[0:543, 407:]
   load_display(back)
   return back


def merge(image1, image2):
   merge = np.concatenate((image1,image2), axis=1)
   load_display(merge)
   cv2.imwrite('out.png', merge)

   
if __name__ == "__main__":
   merge(sliceimagefront("BMW.jpg"), sliceimageback('BMW X5.jpg'))