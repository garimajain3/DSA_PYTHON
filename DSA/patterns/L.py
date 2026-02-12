def star_print(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        
        for k in range(i):
            print("*",end=" ")
            
        print("\n")
            
star_print(5)