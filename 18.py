#Calculate inner, outer, and cross products of vectors/matrices. 
#(here vector not array so..)
import numpy as np

a=list(map(int,input("enter elements of 1st vector").split()))
b=list(map(int,input("Enter elements of 2nd vector").split()))
vec1=np.array(a)
vec2=np.array(b)
print("inner product ",np.dot(vec1,vec2))
print("outer product ",np.outer(vec1,vec2))
print("cross product ",np.cross(vec1,vec2))