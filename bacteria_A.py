print ("hello Bacteria")

# from PIL import Image
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
sigma = 2
t = 0.4

# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(blur, sigma=2)

# perform inverse binary thresholding
mask = blur < t

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# save the result
img.save('sel.png')