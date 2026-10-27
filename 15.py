# Flatten a 2D NumPy array into a 1D array. 
import numpy as np 
r=int(input("enter no. of rows:"))
c=int(input("enter no. of cols: "))
print("enter values row by row")
a=[]
for i in range (r):
    row=list(map(int, input().split()))
    a.append(row)
arr=np.array(a)
print("2 d array:")
print(arr)
flat=arr.flatten()
print("flattened array: ")
print(flat)


