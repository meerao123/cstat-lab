import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

df=pd.read_csv("company-sales.csv")
print(df.head())
df.info()

plt.plot(df["month_number"],df["total_profit"])
plt.xlabel("date")
plt.ylabel("total profit")
plt.tight_layout()
plt.annotate("highest profit",xy=(10.99,4.137e+05),xytext=(10.51,4.165e+05),arrowprops=dict(arrowstyle="->"))
plt.show()

plt.plot(df["month_number"],df["total_profit"],linestyle="--",marker="o",color="red")
plt.xlabel("date")
plt.ylabel("total profit")
plt.tight_layout()
plt.show()

plt.plot(df["month_number"],df["total_units"],label="sales")
plt.plot(df["month_number"],df["total_profit"],label="profit")
plt.legend()
plt.show()

plt.subplot(2,2,1)
plt.scatter(df['total_units'],df['total_profit'])
plt.xlabel("sales")
plt.ylabel("profit")
#plt.show()

plt.subplot(2,2,2)
bars=plt.bar(df["month_number"],df["total_units"],color=cm.tab20(range(len(df))))
plt.bar_label(bars)
plt.savefig("bar.png")
#plt.show()

plt.subplot(2,2,3)
plt.hist(df["total_units"],bins=5,edgecolor="black")
plt.xlabel("sales")
plt.ylabel("freq")
#plt.show()

plt.subplot(2,2,4)
sales_per_prdt=df[["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]].sum()
plt.pie(sales_per_prdt,labels=sales_per_prdt.index,autopct="%1.1f%%")

#plt.show()

plt.tight_layout()
plt.show()

plt.stackplot(df["month_number"],
        df["facecream"],
        df["facewash"],
        df["toothpaste"],
        df["bathingsoap"],
        df["shampoo"],
        df["moisturizer"],
        labels=["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]
)
plt.legend()
plt.show()