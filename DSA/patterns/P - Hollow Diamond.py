n = int(input())
for i in range(1, 2*n):
    if i<=n:
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            if(k==0 or k==i-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    else:
        for l in range(i-n):  
            print(" ",end="")
        for m in range(2*n-i):
            if(m==0 or m==2*n-i-1): 
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()