import PIL
from PIL import Image
from PIL import ImageOps
from matplotlib import pyplot as plt
import numpy as np

#%%
im = Image.open("results_L3.jpg")
grayIm = ImageOps.grayscale(im)

# grayIm.save('greyscale.png') #save greyscale image


im_thresh = grayIm
im_thresh[im_thresh<255] = 0

# Set all values at indices where the array equals 255 to 1.
im_thresh[im_thresh==255] = 1


# %matplotlib widget #onl makes sense for ipython

#%% make colour histogram 
w, h = im.size  
colors = im.getcolors(w*h)

def hexencode(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return '#%02x%02x%02x' % (r,g,b)

for idx, c in enumerate(colors):
    plt.bar(idx, c[0], color=hexencode(c[1]))

plt.show()