import numpy as np

arr1 = np.arange(1,17).reshape(4,4)
print(arr1)

arr2 = np.arange(17,33).reshape(4,4)
print(arr2)

print(np.concatenate((arr1,arr2)))

print(np.concatenate((arr1,arr2),axis=1))

print(np.vstack((arr1,arr2)))

print(np.hstack((arr1,arr2)))

print(np.hstack((arr1,arr2,arr1)))

list1 = np.split(arr1,2)

print(list1)

print(type(list1[0]))

print(np.split(arr1,2,axis=1))

d1 = np.array([4,7,1,3,9])
d1 = np.split(d1,[1,3])
print(d1)