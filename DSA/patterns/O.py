def diamond(n):
    for i in range(1,2*n-1+1):
        if i<=n:
            space = n-i
            stars = i
        else:
            space = i-n
            stars = 2*n - i    
            
        print(" "*(space),end="")
        for j in range(stars):
            print("*",end=" ") 
        print()

diamond(3)