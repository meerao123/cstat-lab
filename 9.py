#Find the 	n-th Fibonacci number using recursion.  	
def fib(n):
    if n==0 or n==1:
        return n 
    else:
        return fib(n-1)+fib(n-2)

n=int(input("enter the term"))
print(n,"th term is",fib(n))
