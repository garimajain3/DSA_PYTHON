def qrown(n):
    for i in range(1,n):
        for j in range(i):
            print("*",end="")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()
        
    for k in range(2*n):
        print("*",end="")
    print()
    
qrown(4)