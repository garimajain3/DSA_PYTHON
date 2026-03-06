n = int(input())
 
for i in range(1,n+1):
    print("*"*(n-i+1)+" "*(2*i-1)+"*"*(n-i+1), end=" ")
    print()
for j in range(2,n+1):
    print("*"*(j)+" "*(2*n-2*j+1)+"*"*(j),end=" ")
    print()