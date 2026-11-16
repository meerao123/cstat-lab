import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv("BankChurners.csv")

print(df.head())
print(df.shape)
df.info()

print(df.isnull().sum())
print((df=="Unknown").sum())

df.replace(['Unknown','unknown'],np.nan,inplace=True)
df.dropna(inplace=True)
#df["Marital_Status"]=df["Marital_Status"].fillna(df["Marital_Status"].mode()[0])
print(df.shape)

print(df["Attrition_Flag"].value_counts(normalize=True)*100)

df["Attrition_Flag"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Attrition Flag Ratio")
plt.ylabel("")
plt.show()

df["Attrition_Flag"].value_counts().plot(kind="bar")
plt.title("Attrition flag")
plt.xticks(rotation=45)
plt.xlabel("customer status")
plt.ylabel("count")
plt.tight_layout()
plt.show()

sns.countplot(data=df,x="Gender")
plt.title("customer distribution over gender")
plt.xlabel("gender")
plt.ylabel("count")
plt.show()

sns.countplot(data=df,x="Card_Category")
plt.title("customer distribution over card catrgory")
plt.xlabel("category")
plt.ylabel("count")
plt.show()

sns.boxplot(data=df,y="Credit_Limit")
plt.title("Distribution of credit limit")
plt.show()

sns.boxplot(data=df,y="Total_Trans_Amt")
plt.title("Distribution of trans amt")
plt.show()

print(df.describe())

df=df.drop(columns=["CLIENTNUM","Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1","Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"])

print(df.shape)

plt.figure(figsize=(12,8))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    cmap='coolwarm',
    annot=True
    )

plt.tight_layout()
plt.show()
