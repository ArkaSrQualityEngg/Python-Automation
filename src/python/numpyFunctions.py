#Different Functions in Numpy:

import numpy as np

# 1. arange()
# np.arange(start,end,steps)
arr_1D = np.arange(1,13)
print(arr_1D)
print('\n')
even_arr = np.arange(2,13,2)
print(even_arr)

# 2. linspace()
print(np.linspace(1,21,6))

# 3. reshape()- used to change the dimension of arrays, for instance, 1Ds are converted into 2Ds,3Ds and 4Ds etc.
arr_1D = np.array([1,3,5,7,9,11,13,15,17,19,21,23])
arr_2D = arr_1D.reshape(3,4)
print(arr_2D)
arr_3D=arr_1D.reshape(3,2,2)
print(arr_3D)
arr_4D= np.arange(1,25,1).reshape(2,3,2,2)
print(arr_4D)

# 4. ravel() - converts multi dim arrays into 1D
print(arr_3D.ravel())

#5. flatten() - converts multi dim arrays into 1D
print(arr_4D.flatten())

#6. transpose() - converts rows into columns, basically transpose operation in matrices
print(arr_2D.transpose())


