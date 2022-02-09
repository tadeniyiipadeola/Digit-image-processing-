from Lesson2 import load_display
import cv2
import numpy as np


def change_image_brightness(image, parameter):
    output_image = image.copy()

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            adjusted = (parameter + output_image[row, col])
            if any(adjusted) > 255.0:
                adjusted = 255.0
            if any(adjusted) < 0:
                adjusted = 0
            output_image[row, col] = np.uint8(adjusted)
    load_display(output_image)
    return output_image


if __name__ == '__main__':
    split = cv2.imread("kennysmall.jpg")
    load_display(split)
    change_image_brightness(split, 1)
