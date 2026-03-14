import numpy as np
import random

print(np.random.random(1))
print(np.random.random((3,3)))
print(np.random.randint((1,4)))
print(np.random.randint(1,4,(4,4)))
print(np.random.randint(1,4,(2,4,4)))
np.random.seed(10)
print(np.random.randint(1,4,(2,4,4)))
print(np.random.rand(3,3))
print(np.random.randn(3,3))
x=[1,2,3,4,5,8,0,9]
print(np.random.choice(x))
print(np.random.choice(x))
for i in range(20):
    print(np.random.choice(x))
print(np.random.permutation(x))
print(np.random.permutation(x))
