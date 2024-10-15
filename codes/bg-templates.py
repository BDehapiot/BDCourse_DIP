#%% Imports

import napari
import numpy as np
from skimage import io
from pathlib import Path
import matplotlib.pyplot as plt

#%% Parameters

nY = 10           
nX = 60

#%% Execute

# set sigmoid parameters
a = 0.9; b = 0.1; x0 = nX*0.6; k = 2/nX
x = np.linspace(0, nX-1, nX)

# define sigmoid function
def sigmoid(x, x0, k, a, b):
    y = a + (b-a) / (1 + np.exp(-k*(x-x0)))
    return y

# create gradient from sigmoid
gradient = np.tile(sigmoid(x, x0, k, a, b), (nY, 1))

# add a specified noise to gradient
noise = np.random.normal(0, 0.05, (nY, nX))
gradient += noise

# select valid pixels
valid = gradient > 0.5

# create an uint8 image
img = (np.random.normal(0.5, 0.1, (nY, nX))*255).astype('uint8') 
img[valid==0] = 0 

plt.imshow(valid)
plt.show()

#%%

io.imsave(
    Path('valid_array.tif'),
    (valid*255).astype('uint8'),
    check_contrast=False,
    )

#%% Display

# viewer = napari.Viewer()
# viewer.add_image(valid)


