import cv2
# from create_image import load_display
import numpy as np

def load_display(image):
    cv2.namedWindow("Test", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Test", image)
    cv2.waitKey(0)


def create_white_box_black_background():
    box = np.zeros((100, 100), np.uint8)
    shape = box.shape

    for i in range(shape[0]):
        for j in range(shape[1]):
            if i in range(25, 75) and j in range(25,75):
                box[i,j] = 255

    return box

def roi_image():
    kennysmall = cv2.imread("kennysmall.jpg")
    load_display(kennysmall)
    kennyface = kennysmall[125:325, 90:250]
    load_display(kennyface)


def change_image_brightness(image, parameter):
    output_image = image.copy()

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            adjusted = (parameter + output_image[row, col])
            if adjusted > 255.0:
                adjusted = 255.0
            if adjusted < 0:
                adjusted = 0
            output_image[row, col] = np.uint8(adjusted)
    load_display(output_image)
    return output_image

def invert_image(image):
    output_image = image.copy()

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
                output_image[row, col] = 255 - output_image[row, col]

    return output_image

if __name__ == '__main__':
    kenny_dark = cv2.imread("Lenna.png")
    # bright_ex = change_image_brightness(kenny_dark, 20)
    load_display(kenny_dark)