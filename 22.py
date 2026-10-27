#Compute eigenvalues and eigenvectors of a square matrix. 

import numpy as np

n = int(input("Enter order of square matrix: "))

print("Enter matrix elements row by row:")
a = []

for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

arr = np.array(a)

values,vector=np.linalg.eig(arr)
print("values: ",values)
print("vectors: ",vector)