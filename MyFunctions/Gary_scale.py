import numpy as np
import cv2
def gray_Image(img_path):
    gray = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)
    kernel_size = (2,2)
    psf = np.ones(kernel_size) / np.prod(kernel_size)
    deblurred = cv2.filter2D(gray, -1, psf)
    img_path='temp\\gray_image.jpg'
    cv2.imwrite(img_path, deblurred)
    return img_path
