#Calculate the QR decomposition of a matrix. 
import numpy as np

r=int(input("enter number of rows "))
c=int(input("enter number of cols "))
print("enter matrix elemts row by row")
a=[]
for i in range(r):
    row=list(map(int,input().split()))
    a.append(row)
arr=np.array(a)
q,R=np.linalg.qr(arr)
print("q matrix: ",q)
print("r matrix: ",R)
    
