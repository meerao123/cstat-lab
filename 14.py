#Get all 2D diagonals of a 3D NumPy array. 
import numpy as np
n=int(input("Enter size of array: "))
print("Enter ", n**3 ,"elements separated by space")
a= list(map(int, input().split()))
arr=np.array(a).reshape(n,n,n)
for i in range(n):
    print(np.diag(arr[i]))
