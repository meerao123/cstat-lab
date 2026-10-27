#Find the inverse of a matrix using NumPy. 
import numpy as np
n=int(input("enter the order of matrix: "))
print("enter value row by row")
a=[]
for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)

arr=np.array(a)
print("og array: ")
print(arr)
try:
    inv=np.linalg.inv(arr)
    print("inverse ")
    print(inv)
except np.linalg.LinAlgError:
    print("no inverse")
