import numpy as np

# PERFORMING BASIC OPERATIONS ON NUMPY

a = np.array([1,2,3,4])
print("ONE DIMENSIONAL ARRAY :")
print("ARRAY : ", a)
print("PERFORMING BASICS OPERATIONS ON THE ARRAY:")
print("ADDING 2 TO THE ARRAY : ", a+2)
print("SUBTRACTING 2 FROM THE ARRAY : ", a-2)
print("MULTIPLYING 8 TO THE ARRAY : ", a*2)
print("DIVIDING 2 FROM THE ARRAY : ", a/2)
print("SQUARING THE ARRAY : ", a**2)
print("TWO DIMENSIONAL ARRAY :")
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("ARRAY : ", b)
print("TRANSPOSE OF THE TWO DIMENSIONAL ARRAY : ", b.T)

# FINDING THE COMMON ELEMENTS ON THE GIVEN 1d ARRAY

array_1 = np.array([1,2,3,4])
print("ARRAY 1 : ",array_1)
array_2 = np.array([5,2,4,8])
print("ARRAY 2 : ",array_2)
inter = np.intersect1d(array_1,array_2)
print("THE INTERSECTION OF THE TWO ARRAYS ARE : ", inter)