from Extractor import extract_text
from WriteToTXTfile import write_to_txt_file 


for i in range(1,6):
    print(write_to_txt_file(extract_text(img_file="TestImgs\\Gujarati_Image_Test_"+str(i)+".jpg")))