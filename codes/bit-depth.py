#%% Imports

import numpy as np
from skimage import io

#%%

nBits = np.array([1, 2, 3, 4, 5, 6, 7, 8])

for bits in nBits:
    gScale = np.linspace(0, 1, num=2**bits)
    gScale = np.repeat(gScale, 2**nBits[-1]/len(gScale), axis=0)
    gScale = (gScale * ((2**nBits[-1])-1)).astype(int) 
    io.imsave(
        f'{bits}bit-depth.tif',
        gScale.astype('uint8'), 
        check_contrast=False
        )   

    
 