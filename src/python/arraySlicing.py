import numpy as np

mx = np.arange(1,101).reshape(10,10)
print(mx)

print(mx[0,0])

print(mx[0,0].ndim)

print(mx[0,])

print(mx[0,].ndim)

print(mx[:,0:1])

print(mx[:,0:1].ndim)

print(mx[1:4,1:4])

print(mx[1:4,1:4].ndim)

print(mx[:])

print(mx[::])

print(mx.dtype)

print(mx.itemsize)

