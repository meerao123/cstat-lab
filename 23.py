#Calculate the n-th order discrete difference. 
import numpy as np
num=int(input("Enter order of discrete diff"))

a=list(map(int,input("Enter vector: ").split()))
arr=np.array(a)
result=np.diff(arr, n=num)
print("Result: ",result)


