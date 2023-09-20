



import cv2
import numpy as np

def cleanTxtVisible(img_path):
    # Load the image with text
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply adaptive thresholding
    thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    enhanced_text = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('tmp/enhanced_image.jpg', enhanced_text)
    return enhanced_text

# Display the enhanced image (optional)
cv2.imshow('Enhanced Image', cleanTxtVisible('TestImgs//test5.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
