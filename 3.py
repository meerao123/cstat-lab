#Check whether a string containing brackets (), {}, [] is valid. 
s=input("enter a bracket string")
stack=[]
for ch in s:
    if ch=="(" or ch=="[" or ch=="{":
        stack.append(ch)
    else:
        if len(stack)==0:
            print("invalid")
            break
        else:
            top=stack.pop()
            if ch==')' and top!='(':
                print("invalid")
                break
            elif ch=='}' and top!='{':
                print("invalid")
                break
            elif ch==']' and top!='[':
                print("invalid")
                break
else:
    if len(stack)==0:
        print("valid")
    else:
        print("invalid")