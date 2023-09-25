import cv2

# img_path="TestImgs\\Gujarati_Image_Test_5.jpg"
def rm_noice(img_path):
    image = cv2.imread(img_path)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
    bg=cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
    out_gray=cv2.divide(image, bg, scale=255)
    out_binary=cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU )[1] 
    out_path="temp//rm_noise.jpg"
    cv2.imwrite(out_path,out_binary)
    return out_path
    # cv2.imshow('binary', out_binary)  

    # cv2.imshow('gray', out_gray)  
    # # cv2.imwrite('gray.png',out_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()