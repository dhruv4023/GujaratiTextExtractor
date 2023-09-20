import cv2
import numpy as np



def clean_img(img_path):
    image = cv2.imread(img_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set a threshold value (adjust as needed)
    threshold_value = 180  # You can experiment with different threshold values

    # Apply binary thresholding (pixels below the threshold become black, above become white)
    # _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    thresholded_image = np.where(gray_image > threshold_value, 250, 0)
    result_image=thresholded_image
    # Apply the thresholded mask to the original image
    # result_image = cv2.bitwise_and(image, image, mask=thresholded_image)

    # Display the original and result images
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Result Image', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result image
    cv2.imwrite('TestImgs\\tmp_image.jpg', result_image)
    print("img cleaned")
    return "TestImgs\\tmp_image.jpg"
# img_path="TestImgs\\Gujarati_Image_Test_4.jpg"
# img_path="TestImgs\\test4.webp"
# img_path="TestImgs\\test3.png"

# print(use_np(img_path))
# print(removeblure(img_path))