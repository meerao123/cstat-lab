import matplotlib.pyplot as plt

heights = [150, 155, 160, 162, 165, 158, 170, 172, 160, 155,
           168, 175, 162, 158, 165, 170, 155, 160, 172, 168]

plt.hist(heights, bins=5, color='skyblue', edgecolor='black')

plt.title('Histogram of Classmates\' Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Number of Students')

plt.show()