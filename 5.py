#Search for a fruit in a tuple. 
fruits=list(input("enter list of fruits ").split())
fruit=input("enter a fruit to check: ")
if fruit in fruits:
    print("yes")
else:
    print("no")
    