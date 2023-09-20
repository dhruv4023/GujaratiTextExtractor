from rembg import remove
from PIL import Image

# Specify the path to your input image and output image
# input_image_path = 'TestImgs/test2.png'
input_image_path = 'cleaned_image.jpg'

output_image_path = 'output_ima=ge.png'

# Open the input image file and read its data
with open(input_image_path, 'rb') as img_file:
    input_image_data = img_file.read()

# Remove the background from the input image data
output_image_data = remove(input_image_data)

# Save the result as the output image
with open(output_image_path, 'wb') as out_file:
    out_file.write(output_image_data)
