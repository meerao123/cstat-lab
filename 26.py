#Calculate mean, variance, and standard deviation using NumPy. 
import numpy as np
a=list(map(int,input("enter elements").split()))
arr=np.array(a)
print("mean=",np.mean(arr))
print("var=",np.var(arr))
print("std=",np.std(arr))