n = int(input())
for i in range(1, 2*n):
    if i<=n:
        for j in range(i):
            if(j==0 or j==i-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    else:
        for k in range(2*n-i):
            if(k==0 or k==2*n-i-1):
                
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()