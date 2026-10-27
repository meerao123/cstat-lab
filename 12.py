#Create Pivot Tables and Cross Tabulations. 
import pandas as pd 


department=list(input("enter dept values").split())
salary=list(map(int,input("enter salary values").split()))
gender=list(input("enter gender values").split())

df=pd.DataFrame({
    'Department':department,
    'Salary':salary,
    'Gender':gender
})

print("pivot table: ")
print(pd.pivot_table(df,values="Salary",index="Department",columns="Gender",aggfunc="mean"))

print("cross tabulation")
print(pd.crosstab(df['Department'],df['Gender']))


