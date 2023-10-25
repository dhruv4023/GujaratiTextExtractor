import cv2

import numpy as np
def nothing(x):
    pass

def dark_txt(img_path):
    print(img_path)
    # Load image
    image = cv2.imread(img_path)

    # Create trackbars for color change
    # Hue is from 0-179 for Opencv
    # cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
    # cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
    # cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
    # cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
    # cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
    # cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

    # Set default value for Max HSV trackbars
    # cv2.setTrackbarPos('HMax', 'image', 179)
    # cv2.setTrackbarPos('SMax', 'image', 255)
    # cv2.setTrackbarPos('VMax', 'image', 255)

    # Initialize HSV min/max values
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0

    # while(1):
    # Get current positions of all trackbars
    hMin= 0 #= cv2.getTrackbarPos('HMin', 'image')
    sMin= 0 #= cv2.getTrackbarPos('SMin', 'image')
    vMin= 196 #= cv2.getTrackbarPos('VMin', 'image')
    hMax= 72 #= cv2.getTrackbarPos('HMax', 'image')
    sMax= 153 #= cv2.getTrackbarPos('SMax', 'image')
    vMax= 255 #= cv2.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display result image
    img_path="temp//dark_txt.png"
    cv2.imwrite(img_path, result)
    return img_path
