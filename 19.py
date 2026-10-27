#Compute the Kronecker product of two multidimensional arrays. 
import numpy as np

r1=int(input("enter number of rows in matrix 1"))
c1=int(input("enter no of cols in matrix 1"))
print("Enter matrix 1 elements row by row: ")
a=[]
for i in range (r1):
    row1=list(map(int,input().split()))
    a.append(row1)

r2=int(input("enter number of rows in matrix 2"))
c2=int(input("enter no of cols in matrix 2"))
print("Enter matrix 2 elements row by row: ")
b=[]
for i in range (r2):
    row2=list(map(int,input().split()))
    b.append(row2)

print("Kronecker product")
print(np.kron(a,b))

