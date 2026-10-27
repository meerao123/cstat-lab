#Create a program that asks the user for a number and prints all its divisors. 
x=int(input("enter a num"))
if x==0:
    print("0 had many divisors")
else:
    for i in range(1,x+1):
        if x%i==0:
            print(i)

