n = int(input())
for i in range(1, n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        if( k==0 or k==i-1):
            print("*",end=" ")
            
        else:
            print(" ",end=" ")
    print()
for l in range(n):
    print("*",end=" ")