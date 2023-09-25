def cleanTxtVisible(img_path):
    import cv2
    # Load the image with text
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply adaptive thresholding
    thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    enhanced_text = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)
    img_path='temp//enhanced_image.jpg'
    cv2.imwrite(img_path, enhanced_text)
    return img_path