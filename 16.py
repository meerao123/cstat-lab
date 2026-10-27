#Generate the Fibonacci series using the Binet Formula. 
import math
n=int(input("enter number of terms: "))
phi=(1+math.sqrt(5))/2
psi=(1-math.sqrt(5))/2

for i in range (n):
    t=int((phi**i - psi**i)/math.sqrt(5))
    print(t,end=" ")
