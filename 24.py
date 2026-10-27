#Evaluate Einstein's summation convention (einsum). 
import numpy as np

r1 = int(input("Enter rows of A: "))
c1 = int(input("Enter columns of A: "))
print("enter a row by row: ")
a=[]
for i in range(r1):
    row1=list(map(int,input().split()))
    a.append(row1)

arr1=np.array(a)

r2 = int(input("Enter rows of B: "))
c2 = int(input("Enter columns of B: "))
print("enter b row by row: ")
b=[]
for i in range(r2):
    row2=list(map(int,input().split()))
    b.append(row2)

arr2=np.array(b)

result1=np.einsum('ik,kj->ij',arr1,arr2)
print(result1)

result2=np.einsum('ij,ij->',arr1,arr2)
print(result2)
