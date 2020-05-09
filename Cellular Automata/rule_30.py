import numpy as np
import matplotlib.pyplot as plt

#Matrix dimensions
rows = 60
cols = 60

#Defining the matrix that will be used
a =  np.zeros((rows, cols), int)
a[0][round(cols/2)] = 1

#Defining rule 30
def rule_30(matrix, cell_row, cell_col):
    if matrix[cell_row, cell_col] == 1 and matrix[cell_row -1, cell_col] == 1 and matrix[cell_row + 1, cell_col] == 1:
        matrix[cell_row, cell_col] = 0
    elif matrix[cell_row, cell_col] == 1 and matrix[cell_row -1, cell_col] == 1 and matrix[cell_row + 1, cell_col] == 0:
        matrix[cell_row, cell_col] = 0
    elif matrix[cell_row, cell_col] == 0 and matrix[cell_row -1, cell_col] == 1 and matrix[cell_row + 1, cell_col] == 1:
        matrix[cell_row, cell_col] = 0
    elif matrix[cell_row, cell_col] == 0 and matrix[cell_row -1, cell_col] == 1 and matrix[cell_row + 1, cell_col] == 0:
        matrix[cell_row, cell_col] = 1
    elif matrix[cell_row, cell_col] == 1 and matrix[cell_row -1, cell_col] == 0 and matrix[cell_row + 1, cell_col] == 1:
        matrix[cell_row, cell_col] = 1
    elif matrix[cell_row, cell_col] == 1 and matrix[cell_row -1, cell_col] == 0 and matrix[cell_row + 1, cell_col] == 0:
        matrix[cell_row, cell_col] = 1
    elif matrix[cell_row, cell_col] == 0 and matrix[cell_row -1, cell_col] == 0 and matrix[cell_row + 1, cell_col] == 1:
        matrix[cell_row, cell_col] = 1
    if matrix[cell_row, cell_col] == 0 and matrix[cell_row -1, cell_col] == 0 and matrix[cell_row + 1, cell_col] == 0:
        matrix[cell_row, cell_col] = 0



#a = np.random.random((60, 60))
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(a)
