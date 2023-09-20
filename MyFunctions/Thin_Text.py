import numpy as np
import cv2
def thin_font(img_path):
    image = cv2.imread(img_path)
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    img_path="temp/thin_txt.jpg"
    cv2.imwrite(img_path, image)
    return img_path