#Create a student grade dictionary and calculate the average grade. 
n=int(input("enter no. of students"))
d={}
for i in range(n):
    x=input("student name")
    y=int(input("grade"))
    d[x]=y

total=sum(d.values())
print("Avg=",total/n)
