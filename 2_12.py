
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import dataset
df = pd.read_csv("BankChurners.csv")

print(df.head())
print(df.shape)
df.info()

# Handle missing values
print((df=='Unknown').sum())
df.replace(["unknown", "Unknown"], np.nan, inplace=True)
print(df.isnull().sum())
df.dropna(inplace=True)

# Attrition Flag ratio
print(df["Attrition_Flag"].value_counts(normalize=True) * 100)

df["Attrition_Flag"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Attrition Flag Ratio")
plt.ylabel("")
plt.show()

# Bar charts
sns.countplot(data=df, x="Gender")
plt.title("Customer Distribution by Gender")
plt.show()

sns.countplot(data=df, x="Card_Category")
plt.title("Customer Distribution by Card Category")
plt.show()

# Box plots
sns.boxplot(data=df, y="Credit_Limit")
plt.title("Distribution of Credit Limit")
plt.show()

sns.boxplot(data=df, y="Total_Trans_Amt")
plt.title("Distribution of Total Transaction Amount")
plt.show()

# Descriptive statistics
print(df.describe())

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

# Remove unnecessary columns
df = df.drop(columns=[
    "CLIENTNUM",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"
])

print(df.shape)
