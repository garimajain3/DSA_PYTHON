n = int(input())
 
for l in range(n):
    print("*",end=" ")
print()
for i in range(n-1,-1,-1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        if(j==0 or j==i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print()