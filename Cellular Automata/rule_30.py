import numpy as np
import matplotlib.pyplot as plt
from math import floor

#Matrix dimensions
rows = 200
cols = 200
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')

#Defining the matrix that will be used
lattice =  np.zeros((rows+2, cols+1), int) #Matrix is padded by one cell on all side
update_lattice = np.zeros((rows+2, cols+2), int) #Matrix is padded by one cell on all side
lattice[0][round(cols/2)] = 1

#Defining rule 30
def rule_30(matrix, cell_row, cell_col):
    if matrix[cell_row][cell_col] == 1 and matrix[cell_row][cell_col-1] == 1 and matrix[cell_row][cell_col+1] == 1:
        matrix[cell_row+1][cell_col] = 0
    elif matrix[cell_row][cell_col] == 1 and matrix[cell_row][cell_col -1] == 1 and matrix[cell_row][cell_col + 1] == 0:
        matrix[cell_row+1][cell_col] = 0
    elif matrix[cell_row+1][cell_col] == 0 and matrix[cell_row][cell_col -1] == 1 and matrix[cell_row][cell_col + 1] == 1:
        matrix[cell_row+1][cell_col] = 0
    elif matrix[cell_row][cell_col] == 0 and matrix[cell_row][cell_col -1] == 1 and matrix[cell_row][cell_col + 1] == 0:
        matrix[cell_row+1][cell_col] = 1
    elif matrix[cell_row][cell_col] == 1 and matrix[cell_row][cell_col -1] == 0 and matrix[cell_row][cell_col + 1] == 1:
        matrix[cell_row+1][cell_col] = 1
    elif matrix[cell_row][cell_col] == 1 and matrix[cell_row][cell_col -1] == 0 and matrix[cell_row][cell_col + 1] == 0:
        matrix[cell_row+1][cell_col] = 1
    elif matrix[cell_row][cell_col] == 0 and matrix[cell_row][cell_col -1] == 0 and matrix[cell_row][cell_col + 1] == 1:
        matrix[cell_row+1][cell_col] = 1
    if matrix[cell_row][cell_col] == 0 and matrix[cell_row][cell_col -1] == 0 and matrix[cell_row][cell_col + 1] == 0:
        matrix[cell_row+1][cell_col] = 0


for k in range (rows*cols): #updating the entire lattice
    rule_30(lattice, floor(k/rows), k % cols)

plt.imshow(lattice)
