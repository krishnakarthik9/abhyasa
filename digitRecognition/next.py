# image.py

from skimage import img_as_ubyte
from skimage.io import imread
from skimage.filters import gaussian, threshold_minimum
from skimage.morphology import square, erosion, thin
from PIL import Image

import numpy as np
import cv2

# ...
def binarize(image_abs_path):

    # Convert color image (3-channel deep) into grayscale (1-channel deep)
    # We reduce image dimensionality in order to remove unrelevant features like color.
    grayscale_img = imread(image_abs_path, as_grey=True)

    # Apply Gaussian Blur effect - this removes image noise
    gaussian_blur = gaussian(grayscale_img, sigma=1)

    # Apply minimum threshold
    thresh_sauvola = threshold_minimum(gaussian_blur)

    # Convert thresh_sauvola array values to either 1 or 0 (white or black)
    binary_img = gaussian_blur > thresh_sauvola

    return binary_img
 
im1 = binarize('cropped1.jpg')
a = Image.fromarray(im1)
a.save('cropped_1.jpg')