# This is Saleh

from PIL import Image
img = Image.open('results_L3.jpg').convert('LA')
# img.save('greyscale.png')


import sys
import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer

# get filename, sigma, and threshold value from command line

#sigma = float(sys.argv[2])
#t = float(sys.argv[3])

# read and display the original image
image = skimage.io.imread('results_L3.jpg')
viewer = skimage.viewer.ImageViewer(image)
#viewer.show()


