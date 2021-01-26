print ("hello Bacteria")

from PIL import Image
# img = Image.open('results_L3.jpg').convert('LA')
# img.save('greyscale.png')

import sys
import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer

# get filename, sigma, and threshold value from command line
filename = 'results_L3.jpg'
sigma = 1
t = 0.8

image = skimage.io.imread(fname=filename)

# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(blur, sigma)

# perform inverse binary thresholding
t = skimage.filters.threshold_otsu(blur)
mask = blur > t

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# save binary image; first find beginning of file extension
dot = filename.index(".")
binary_file_name = filename[:dot] + "-binary" + filename[dot:]
skimage.io.imsave(fname=binary_file_name, arr=skimage.img_as_ubyte(sel))