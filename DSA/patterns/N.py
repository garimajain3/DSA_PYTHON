def inverted_hollow(n):
    for i in range(n,0,-1):
        print(" "*(n-i),end="")
        
        for j in range(1,i+1):
            if(j==i or j==1 or i==n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
                
        print()
        
inverted_hollow(6)