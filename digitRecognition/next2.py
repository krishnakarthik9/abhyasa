
from skimage import img_as_ubyte
from skimage.io import imread
from skimage.filters import gaussian, threshold_minimum
from skimage.morphology import square, erosion, thin
from PIL import Image

import numpy as np
import cv2

import matplotlib.pyplot as plt
from skimage.morphology import skeletonize, skeletonize_3d
from skimage.data import binary_blobs

def binarize(image_abs_path):

    # Convert color image (3-channel deep) into grayscale (1-channel deep)
    # We reduce image dimensionality in order to remove unrelevant features like color.
    grayscale_img = imread(image_abs_path, as_grey=True)
    # Apply Gaussian Blur effect - this removes image noise
    gaussian_blur = gaussian(grayscale_img, sigma=1)

    # Apply minimum threshold
    thresh_sauvola = threshold_minimum(gaussian_blur)

    # Convert thresh_sauvola array values to either 1 or 0 (white or black)
    binary_img = gaussian_blur < thresh_sauvola
    # plt.imshow(binary_img,cmap=plt.cm.gray, interpolation='nearest')
    # plt.savefig('bg.jpg')

    return binary_img

# data = binary_blobs(200, blob_size_fraction=.2, volume_fraction=.35, seed=1)

data = binarize('cropped1.jpg')
#plt.imshow(data)
# = Image.fromarray(im1)
skeleton = skeletonize(data)
#skeleton3d = skeletonize_3d(data)

# fig, axes = plt.subplots(1, 3, figsize=(8, 4), sharex=True, sharey=True,
#                          subplot_kw={'adjustable': 'box-forced'})
# ax = axes.ravel()

# ax[0].imshow(data, cmap=plt.cm.gray, interpolation='nearest')
# ax[0].set_title('original')
# ax[0].axis('off')

# ax[1].imshow(skeleton, cmap=plt.cm.gray, interpolation='nearest')
# ax[1].set_title('skeletonize')
# ax[1].axis('off')

data = skeleton == 0 
#plt.figure(figsize = (2,2))
#plt.imshow(data, cmap=plt.cm.gray, interpolation=None)
#plt.imshow(data, cmap=plt.cm.binary, interpolation=None)
#plt.axis('off')
#extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
plt.imsave('final.jpg',data, format="jpg", cmap="hot")

# ax[2].imshow(skeleton3d, cmap=plt.cm.gray, interpolation='nearest')
# ax[2].set_title('skeletonize_3d')
# ax[2].axis('off')



#fig.tight_layout()
#plt.show()
