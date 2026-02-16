import numpy as np
array_1D = np.array([1,2,3,4])
print(array_1D)          ## printing the array
print(type(array_1D))    ## printing the datatype
print(array_1D.ndim)     ## printing how many dimensions are there in the array whether it is 1D, 2D or 3D
print(array_1D.size)     ## printing no of elements in the array
print(array_1D.shape)    ## prints (row, )
print(array_1D.dtype)    ## prints the data type of the elements of thae array

print("\n\n")

array_2D = np.array([[1,2,3,4],[5,6,7,8]])
print(array_2D)
print(type(array_2D))
print(array_2D.ndim)
print(array_2D.size)
print(array_2D.shape)   ## prints (row,col)
print(array_2D.dtype)



