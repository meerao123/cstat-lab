#Plot a line graph from a NumPy array. 
import numpy as np
import matplotlib.pyplot as plt

a = list(map(int, input("Enter array elements: ").split()))

arr = np.array(a)

plt.plot(arr)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("line graph")
plt.grid(True)
plt.show()