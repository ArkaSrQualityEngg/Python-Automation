import numpy as np
import matplotlib.pyplot as plt

print(np.sin(90))
print(np.sin(180))
print(np.cos(90))
print(np.cos(180))
print(np.tan(90))
print(np.tan(180))

x = np.arange(0,np.pi,0.1)
y_sin = np.sin(x)
print(x)
print(y_sin)
plt.plot(x,y_sin)
plt.show()
y_cos = np.cos(np.cos(x))
plt.plot(x,y_cos)
plt.show()
y_tan = np.tan(x)
plt.plot(x,y_tan)
plt.show()