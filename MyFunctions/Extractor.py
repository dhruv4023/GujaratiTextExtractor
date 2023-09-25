from PIL import Image
import pytesseract
# Specify the Tesseract executable path (update this with your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Apps\\Tesseract-OCR\\tesseract.exe'


def extract_text(img_file:str):
    # Open the image
    image = Image.open(img_file)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(image, lang='eng', output_type=pytesseract.Output.STRING)

    # Print or use the extracted Gujarati text
    return (extracted_text)

