from MyFunctions.Thin_Text import thin_font
from MyFunctions.Extractor import extract_text
from MyFunctions.WriteToTXTfile import write_to_txt_file 
from MyFunctions.Gary_scale import gray_Image 
from MyFunctions.Rm_Noice import rm_noice
from MyFunctions.CleanTxtVisible import cleanTxtVisible 
# for i in range(1,6):
# print(write_to_txt_file(extract_text(img_file="TestImgs\\Gujarati_Image_Test_"+str(5)+".jpg")))
# print(write_to_txt_file(extract_text(img_file="TestImgs\\test3.png")))

# img_path="TestImgs\\en_tst_2.png"
img_path="TestImgs\\tst_dev.jpeg"
# img_path="temp//shadows_out_norm.jpg"
# img_path="cleaned_image.jpg"
# img_path="temp/image_with_border.jpg"
# img_path="temp/eroded_image.jpg"
# img_path="temp//contrast_adjusted_image.jpg"
# img_path="temp//contrast_adjusted_image.jpg"

# img_path='temp//enhanced_image.jpg'
# cleaned_img_path=clean_img(img_path=img_path)
# img_path="temp\\binary.jpg"

img_path=gray_Image(img_path) 
# img_path=cleanTxtVisible(img_path) 
# img_path=thin_font(img_path) 
print(write_to_txt_file(extract_text(img_file=img_path)))
