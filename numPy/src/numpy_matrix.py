import numpy as np

#Create a 3x3 matrix with values ranging from 0 to 8
arr = np.arange(0,9)
arr = arr.reshape(3,3)
print(arr)

#Create a 3x3 identity matrix
idmtx = np.eye(3)
print(idmtx)