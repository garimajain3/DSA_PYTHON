n = int(input())
for i in range(1, 2*n):
    if i<=n:
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            print("*",end=" ")
        print()
    else:
        for l in range(i-n): 
            print(" ",end="")
        for m in range(2*n-i):  
            print("*",end=" ")
        print()