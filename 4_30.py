import pandas as pd

# Read the dataset
data = pd.read_csv("data.csv")

# Population statistics
population_mean = data["Population"].mean()
population_median = data["Population"].median()
population_variance = data["Population"].var()

# Murder rate statistics
murder_mean = data["Murder_Rate"].mean()
murder_median = data["Murder_Rate"].median()
murder_variance = data["Murder_Rate"].var()

# Display results
print("Population")
print("Mean:", population_mean)
print("Median:", population_median)
print("Variance:", population_variance)

print("\nMurder Rate")
print("Mean:", murder_mean)
print("Median:", murder_median)
print("Variance:", murder_variance)
