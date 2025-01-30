import numpy as np
a = np.array([1, 2, 3, 6, 4, 5])
print(a[::-1])

x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
print(np.bincount(x).argmax(), np.where(x == np.bincount(x).argmax())[0])
print(np.bincount(y).argmax(), np.where(y == np.bincount(y).argmax())[0])
