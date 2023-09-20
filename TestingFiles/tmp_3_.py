# %%
import cv2
from matplotlib import pyplot as plt
ip_folder="TestImgs\\"
tmp_folder="temp\\"

# %%
img_path=ip_folder+"Gujarati_Image_Test_5.jpg"
def rimg(path):
    return cv2.imread(path)
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

# %%
def gray_Image(img_path):
    import numpy as np
    import cv2
    gray = cv2.cvtColor(rimg(img_path), cv2.COLOR_BGR2GRAY)
    kernel_size = (2,2)
    psf = np.ones(kernel_size) / np.prod(kernel_size)
    deblurred = cv2.filter2D(gray, -1, psf)
    img_path=tmp_folder+'deblurred_image.jpg'
    cv2.imwrite(img_path, deblurred)
    return img_path
display(gray_Image(img_path))

# %%
def grayscale(img_path):
    img=(rimg(img_path))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_path=tmp_folder+"gray.jpg"
    cv2.imwrite(img_path,img)
    return img_path

# %%
display(grayscale(img_path))

# %%
def contrast_image(img_path):
    image = cv2.imread(img_path)

    # Adjust the contrast using the cv2.convertScaleAbs function
    alpha = 1.5  # Adjust this value to control the contrast (1.0 is no change)
    beta = 0  # Bias value (typically 0)
    contrast_adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Save or display the adjusted image
    img_path='temp/contrast_adjusted_image.jpg'
    cv2.imwrite(img_path, contrast_adjusted)
    return img_path

display(contrast_image(img_path))

# %%
def bw_image(img_path):
    thresh, im_bw = cv2.threshold(rimg(img_path), 180, 220, cv2.THRESH_BINARY)
    img_path=tmp_folder+"bw_image.jpg"
    cv2.imwrite(img_path, im_bw)
    return img_path
display(bw_image(img_path))

# %%
def thin_font(img_path):
    import numpy as np
    image = (rimg(img_path))
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    img_path="temp/eroded_image.jpg"
    cv2.imwrite(img_path, image)
    return img_path

# %%
display(thin_font(img_path))

# %%

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

# %%
display(cleanTxtVisible(img_path))


