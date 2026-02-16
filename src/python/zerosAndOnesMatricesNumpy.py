import numpy as np

mx_1s = np.ones(5)
print(mx_1s)
print(mx_1s.dtype)
mx_1s = np.ones((3,4))
print(mx_1s)
mx_1s = np.ones((3,4),dtype=int)
print(mx_1s)
mx_0s = np.zeros((4,6),dtype=str)
print(mx_0s)
mx_0s = np.zeros((4,6),dtype=bool)
print(mx_0s)
mx_0s = np.zeros((4,6),dtype=float)
print(mx_0s)
em_str = ''
print(bool(em_str))
em_mx = np.empty((3,3))
print(em_mx)
