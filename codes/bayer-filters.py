#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io 
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

# img_name = 'chameleon-01_crop_mod_256x256.tif'
# img = io.imread(Path('../_content/01a_chameleon-01', img_name))

img_name = 'chameleon-01_crop_mod_192x192_crop.tif'
img_path = Path('../_content/01a_chameleon-01', img_name)
img = io.imread(img_path)

# img_name = 'butterfly-wing-01_mod_256x256.tif'
# img_path = Path('../_content/01c_butterfly-wing-01', img_name)
# img = io.imread(img_path)

#%%

# Define Bayer filters array (R=0, G=1, B=2)
filtBayer = np.zeros_like(img[...,0])
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if y % 2 == 0:
            if x % 2 == 0:
                filtBayer[y,x] = 2 # Blue
            else:
                filtBayer[y,x] = 1 # Green
        else:
            if x % 2 == 0:
                filtBayer[y,x] = 1 # Green
            else:
                filtBayer[y,x] = 0 # Red
                
# Extract color array
filtR = img[...,0].copy()
filtG = img[...,1].copy()
filtB = img[...,2].copy()
filtR[filtBayer!=0] = 0
filtG[filtBayer!=1] = 0
filtB[filtBayer!=2] = 0
filtRGB = np.maximum(filtR, filtG)
filtRGB = np.maximum(filtRGB, filtB)

#%%

io.imsave(
    str(img_path).replace('.tif', '_filtR.tif'), 
    filtR, check_contrast=False,
    )

io.imsave(
    str(img_path).replace('.tif', '_filtG.tif'), 
    filtG, check_contrast=False,
    )

io.imsave(
    str(img_path).replace('.tif', '_filtB.tif'), 
    filtB, check_contrast=False,
    )

io.imsave(
    str(img_path).replace('.tif', '_filtRGB.tif'), 
    filtRGB, check_contrast=False,
    )