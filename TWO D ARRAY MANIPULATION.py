import numpy as np

# EXTRACTING SOME COLUMNS OR ROWS OF THE 2D ARRAY

arr1 = np.arange(36).reshape(6,6)
print("THE 2D ARRAY : ",arr1)
ex = np.array(arr1)
print("EXTRACTION OF THE 4 ROW AND 5 ROW : ", ex[3:5])

# FINDING THE SUM OF THE COLUMNS

arr2 = np.array([[1,3,5,6],[3,6,7,3],[2,3,6,6],[4,5,8,5]])
print("THE 2D ARRAY : ", arr2)
print("THE SUM OF THE COLUMNS OF THE ARRAY : ", arr2.sum(axis =0))