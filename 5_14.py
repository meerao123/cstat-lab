import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sales_data(1).csv')

print(df.head())

# a. Total Profit Line Plot
plt.plot(df['Date'], df['Profit'])
plt.title('Total Profit')
plt.xlabel('Date')
plt.ylabel('Profit')
plt.show()

# b. Styled Line Plot
plt.plot(df['Date'], df['Sales'], color='red',
         linestyle='--', marker='o')
plt.title('Styled Sales Plot')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# c. Multi-Line Plot
plt.plot(df['Date'], df['Sales'], label='Sales')
plt.plot(df['Date'], df['Profit'], label='Profit')
plt.title('Sales and Profit')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend()
plt.show()

# d. Scatter Plot
plt.scatter(df['Sales'], df['Profit'])
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

# e. Bar Chart
plt.bar(df['Region'], df['Sales'])
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# f. Bar Chart and Save the Figure
plt.bar(df['Region'], df['Profit'], color='green')
plt.title('Profit by Region')
plt.xlabel('Region')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

# g. Histogram
plt.hist(df['Sales'], bins=5, edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# h. Pie Chart
region_sales = df.groupby('Region')['Sales'].sum()

plt.pie(region_sales, labels=region_sales.index,
        autopct='%1.1f%%')
plt.title('Sales Percentage by Region')
plt.show()

# i. Subplots
plt.subplot(1, 2, 1)
plt.plot(df['Date'], df['Sales'])
plt.title('Sales')

plt.subplot(1, 2, 2)
plt.plot(df['Date'], df['Profit'])
plt.title('Profit')

plt.tight_layout()
plt.show()

# j. Stack Plot
region_data = df.groupby('Region')['Sales'].sum()

plt.stackplot(
    range(len(region_data)),
    region_data.values,
    labels=region_data.index
)
plt.title('Sales by Region - Stack Plot')
plt.xlabel('Region Index')
plt.ylabel('Sales')
plt.legend()
plt.show()