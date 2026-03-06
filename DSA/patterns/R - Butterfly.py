n = int(input())
 
for i in range(1,n+1):
    print(i*"*"+" "*(2*n-2*i)+ i*"*",end="")
    print()
for j in range(n-1,-1,-1):
    print(j*"*"+" "*(2*(n-j))+j*"*",end="")
    print()