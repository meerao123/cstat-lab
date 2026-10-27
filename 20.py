#Convert a NumPy matrix into a list. 
import numpy as np 
r=int(input("enter number of rows in matrix: "))
c=int(input("Enter no. of col in matrix"))
print("enter elements row by row: ")
a=[]
for i in range(r):
    row=list(map(int,input().split()))
    a.append(row)
arr=np.array(a)
print("array: ",arr)
print("converted to list",arr.tolist())    
