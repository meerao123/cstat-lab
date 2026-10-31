import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("river_temp.csv")

# Filter Swale at Catterick Bridge
swale_data = data[data["SITE_NAME"] == "Swale at Catterick Bridge"]

# Mean temperature
mean_temperature = swale_data["Temperature"].mean()

# Median dissolved oxygen
median_oxygen = swale_data["Oxygen"].median()

print("Mean Temperature:", mean_temperature)
print("Median Dissolved Oxygen:", median_oxygen)

# Histogram
plt.hist(swale_data["Temperature"], bins=5,
         color="skyblue", edgecolor="black")

plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Temperature Distribution - Swale at Catterick Bridge")
plt.show()
