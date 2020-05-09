import numpy as np
import matplotlib.pyplot as plt

#Matrix dimensions
rows = 60
cols = 60

#Defining the matrix that will be used
a =  np.zeros((rows, cols), int)
a[0][round(cols/2)] = 1

#Defining the function that will be used
#a = np.random.random((60, 60))
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(a)
