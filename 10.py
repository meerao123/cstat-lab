#Read and display a sparse matrix using a dictionary. 
d={}
r=int(input("Enter no. of rows"))
c=int(input("enter no. of cols"))
print("Enter sparse matrix elements")
for i in range (r):
    for j in range (c):
        x=int(input())
        if x!=0:
            d[(i,j)]=x

print("Sparse matrix\n",d)