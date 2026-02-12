def hollow_rect(m,n):
    for i in range(m):  
        for j in range(n):
            if(j==0 and j==n-1):
                print("gari")
                print("*",end="\n")
        
            
hollow_rect(6,9)

