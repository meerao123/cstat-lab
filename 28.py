#Convert a NumPy array into a CSV file.
import numpy as np

r=int(input("enter number of rows: "))
c=int(input("number of cols: "))

a=[]
print("enter elemts:")
for i in range (r):
    row=list(map(int,input().split()))
    a.append(row)

arr=np.array(a)

np.savetxt("file.csv",arr,delimiter=",",fmt="%d")
print("file saved")