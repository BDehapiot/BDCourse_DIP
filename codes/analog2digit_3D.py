#%% Imports

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.tri import Triangulation

#%% Parameters

# Define Gaussian parameters
mu = np.array([0, 0])
sigma = np.array([[2, 0], [0, 2]])

# Define Plot resolution
nc = 256 # continuous
nd = 16 # discrete
bar_width = 0.20 # bar width for discrete

# Define Plot view
elev = 25
azim = 202.5
roll = 0

# Define saving dpi
dpi = 1200

#%% Plots (continuous & discrete Gaussian distribution) 

''' continuous ------------------------------------------------------------ '''

# Create a mesh grids
xc = np.linspace(-5, 5, nc)
yc = np.linspace(-5, 5, nc)
Xc, Yc = np.meshgrid(xc, yc)

# Calculate Gaussian distribution 
posc = np.empty(Xc.shape + (2,))
posc[:, :, 0] = Xc; posc[:, :, 1] = Yc
Zc = np.exp(-0.5 * np.sum((posc - mu) @ np.linalg.inv(sigma) * (posc - mu), axis=2)) / (2 * np.pi * np.sqrt(np.linalg.det(sigma)))

# Reshape the X, Y, and Z arrays to be 1D
xc = Xc.flatten(); yc = Yc.flatten(); zc = Zc.flatten()

# Normalize Z
zc = (zc - np.min(zc)) / (np.max(zc) - np.min(zc))*255
zc = zc.astype('uint8')

# Triangulation of the X, Y coordinates
tri = Triangulation(xc, yc)

# Plot the 3D Gaussian distribution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', proj_type = 'ortho')
ax.view_init(elev, azim, roll) # view orientation
ax.plot_trisurf(tri, zc, cmap='gray', vmax=270, edgecolor='none', antialiased=False)
plt.axis('off')

# save as svg
plt.savefig("analog2digit_3D_continuous.png", dpi=dpi, transparent=True)

''' discrete -------------------------------------------------------------- '''

# Create a mesh grids
xd = np.linspace(-5, 5, nd)
yd = np.linspace(-5, 5, nd)
Xd, Yd = np.meshgrid(xd, yd)

# Calculate Gaussian distribution 
posd = np.empty(Xd.shape + (2,))
posd[:, :, 0] = Xd; posd[:, :, 1] = Yd
Zd = np.exp(-0.5 * np.sum((posd - mu) @ np.linalg.inv(sigma) * (posd - mu), axis=2)) / (2 * np.pi * np.sqrt(np.linalg.det(sigma)))

# Reshape the X, Y, and Z arrays to be 1D
xd = Xd.flatten(); yd = Yd.flatten(); zd = Zd.flatten()

# Normalize Z
zd = (zd - np.min(zd)) / (np.max(zd) - np.min(zd))*255
zd = zd.astype('uint8')

# Get histogram color
cmap = cm.get_cmap('gray')
rgba = [cmap(z) for z in zd]

# Plot the 3D Gaussian distribution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', proj_type = 'ortho')
ax.view_init(elev, azim, roll) # view orientation
ax.bar3d(xd, yd, np.zeros_like(zd), 
    bar_width, bar_width, zd, 
    color=rgba,
    shade=True,
    # edgecolor='black',
    # linewidth=0.33,
    )
plt.axis('off')

# save as svg
plt.savefig("analog2digit_3D_discrete.png", dpi=dpi, transparent=True)