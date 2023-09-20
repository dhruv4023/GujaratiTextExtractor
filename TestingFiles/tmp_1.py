import cv2
import pytesseract

# Load the image
image = cv2.imread("TestImgs\\Gujarati_Image_Test_5.jpg")
# image = cv2.imread("TestImgs\\test4.webp")

# Convert the image to grayscale

# Use Tesseract OCR to detect text and get bounding boxes
# custom_config = r'--oem 3 --psm 6 -l guj'  # You can adjust OCR settings
# text_boxes = pytesseract.image_to_boxes(gray, config=custom_config)

# Highlight text and paint background
# for box in text_boxes.splitlines():
#     box = box.split()
#     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(image, (x, y), (w, h), (0, 0, 0), -1)  # Highlight text in black

# Paint the background white
# image[gray < 200] = [255, 255, 255]

# Save the cleaned image

gaussian_blur = cv2.GaussianBlur(image,(7,7),2)

sharpend_img = cv2.addWeighted(image,3.5,gaussian_blur,-2.5,0)
gray = cv2.cvtColor(sharpend_img, cv2.COLOR_BGR2GRAY)
# from ImageCleaner import clean_img
# clean_img('cleaned_image.jpg')
# cv2.imshow('sharpended img',sharpend_img)
cv2.imwrite('cleaned_image.jpg',gray)
# cv2.imwrite('cleaned_image.jpg',sharpend_img)
