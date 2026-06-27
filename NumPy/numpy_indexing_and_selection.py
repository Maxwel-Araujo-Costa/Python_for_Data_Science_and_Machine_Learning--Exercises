#Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
# mat = np.arange(1,26).reshape(5,5)
#array([[ 1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10],
#       [11, 12, 13, 14, 15],
#       [16, 17, 18, 19, 20],
#       [21, 22, 23, 24, 25]])

#Desired Output 1:
#array([[12, 13, 14, 15],
#       [17, 18, 19, 20],
#       [22, 23, 24, 25]])

#Desired Output 2:
#20

#Desired Output 3:
#array([[ 2],
#       [ 7],
#       [12]])

#Desired Output 4:
#array([21, 22, 23, 24, 25])

#Desired Output 5:
#array([[16, 17, 18, 19, 20],
#       [21, 22, 23, 24, 25]])

import numpy as np

mat = np.arange(1,26).reshape(5,5)

output1 = mat[2][1:5], mat[3][1:5], mat[4][1:5]
output1 = np.array(output1)
print(output1)  # Desired Output 1

print(mat[2:,1:])  # Alternative solution to Desired Output 1

