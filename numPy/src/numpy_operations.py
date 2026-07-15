import numpy as np

mat = np.arange(1,26).reshape(5,5)
mat

#Do the following:

#1) Get the sum of all the values in mat
#2) Get the standard deviation of the values in mat
#3) Get the sum of all the columns in mat


#1) Solution to get the sum of all the values in mat
sum = mat[0] + mat[1] + mat[2] + mat[3] + mat[4]
sum = sum[0] + sum[1] + sum[2] + sum[3] + sum[4]
print(sum)
#1) Alternative solution to get the sum of all the values in mat
sum = 0
total_sum = 0
for m in mat:
    sum += m
for s in sum:
    total_sum += s
print(total_sum)
#1) Another alternative solution to get the sum of all the values in mat
print(mat.sum())

#2) Solution to get the standard deviation of the values in mat
print(np.std(mat))

#3) Solution to get the sum of all the columns in mat
print(mat.sum(axis=0))
#3) Alternative solution to get the sum of all the columns in mat
sum = 0
for m in mat:
    sum += m
print(sum)