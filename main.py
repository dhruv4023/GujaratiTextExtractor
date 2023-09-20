from MyFunctions.Thin_Text import thin_font
from MyFunctions.Extractor import extract_text
from MyFunctions.WriteToTXTfile import write_to_txt_file 
from MyFunctions.Rm_Noice import rm_noice

# for i in range(1,6):
# print(write_to_txt_file(extract_text(img_file="TestImgs\\Gujarati_Image_Test_"+str(5)+".jpg")))
# print(write_to_txt_file(extract_text(img_file="TestImgs\\test3.png")))

# img_path="TestImgs\\Gujarati_Image_Test_5.jpg"
img_path="temp//shadows_out_norm.jpg"
# img_path="cleaned_image.jpg"
# img_path="temp/image_with_border.jpg"
# img_path="temp/eroded_image.jpg"
# img_path="temp//contrast_adjusted_image.jpg"
# img_path="temp//contrast_adjusted_image.jpg"

# img_path='temp//enhanced_image.jpg'
# cleaned_img_path=clean_img(img_path=img_path)
# img_path="temp\\binary.jpg"

img_path=rm_noice(img_path) 
img_path=thin_font(img_path) 
print(write_to_txt_file(extract_text(img_file=img_path)))
