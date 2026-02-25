import numpy as np

arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(1,10).reshape(3,3)

print(arr1)
print(arr2)

arr3 = arr1 + arr2
print(arr3)

print(np.add(arr2,arr3))

print(np.subtract(arr3,arr1))

print(np.multiply(arr1,arr3))

print(np.divide(arr1,arr3))

print(arr1 @ arr2)

print(arr3.dot(arr1))

print(arr1.max())

print(arr1.argmax())

print(arr1.max(axis=0))

print(arr1.max(axis=1))

print(arr1.min())

print(arr1.argmin())

print(arr1.min(axis=0))

print(arr1.min(axis=1))

print(np.sum(arr1))

print(np.sum(arr1,axis=0))

print(np.sum(arr1,axis=1))

print(np.mean(arr1))

print(np.sqrt(arr1))

print(np.std(arr1))

print(np.exp(arr1))

print(np.log2(arr1))

print(np.log10(arr1))

print(np.log(arr1))