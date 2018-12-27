# Python 3
# Dataset treatment: importing, filtering, transforming, image augmentation, saving the results.
# Original dataset needs to be prepared in order to be employed in models. 
# The images are converted into numpy arrays to facilitate the operations.

import os
from scipy import misc
import numpy as np

# Read and append image files in ndarray format
# X: original images; Y: segmented/mask images
X=[]   
Y=[]
for x in sorted(os.listdir('.')):
    if x.endswith('.png'):
        im = misc.imread(x)
        Y.append(im)
    else:
        im = misc.imread(x)
        X.append(im)

X = np.asarray(X)
Y = np.asarray(Y)


# There is 76/300 images with different size, in order to avoid problems with size input, these 
# images are removed from X and Y ndarrays
n=[]
for i in range(300):
  if (X[i].shape != (120,120,3)) == True:
    n.append(i)

x = np.delete(X,n)
x = np.stack(x)
x.shape  # shape control print requires

y = np.delete(Y,n)
y = np.stack(y)
y.shape  # shape control print requires

# Image augmentation, using flip and 90º rotation 

from scipy.ndimage.interpolation import rotate as rot

y = y.reshape(224,120,120,1)
# new variables are created for augmented images
X = [] 
Y = []

# flip and rotation on 90º
for i in range(224):
    X.append(np.fliplr(rot(x[i], angle=90)))
    Y.append(np.fliplr(rot(y[i], angle=90)))

X = np.asarray(X)
Y = np.asarray(Y)

# variables xx and yy are the addition of original and augmented images
xx = np.concatenate((x,X), axis=0)
yy = np.concatenate((y,Y), axis=0)

yy = yy.reshape(448, 120, 120)

# Save the data created and augmented as npy files
np.save('y.npy',yy)
np.save('x.npy',xx)
