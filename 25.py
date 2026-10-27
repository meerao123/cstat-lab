#Compute Pearson correlation coefficients. 


import numpy as np

x = list(map(int, input("Enter first set of values: ").split()))
y = list(map(int, input("Enter second set of values: ").split()))

result = np.corrcoef(x, y)

print("Pearson correlation coefficient:")
print(result[0, 1])