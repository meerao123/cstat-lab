#Get all 2D diagonals of a 3D NumPy array. 
import numpy as np 
import matplotlib.pyplot as plt 
start= float(input("enter starting value of x: "))
end=float(input("enter ending vlaue: "))
if (start==end):
    print("Starting and ending same")
else:
    x=np.linspace(start,end,100)
    y=x**2 
    plt.plot(x,y)
    plt.xlabel("x axis")
    plt.ylabel("yaxis")
    plt.title("graph of y=f(x)")
    plt.grid(True)
    plt.show()

    
