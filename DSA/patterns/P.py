def hollow_diamond(n):
    for i in range(1,2*n-1+1):
        if i<=n:
            space = n-i
            stars = i
        else:
            space = i-n
            stars = 2*n-i
            
        print(" "*space,end=" ")
        for k in range(1,stars+1):
            if(k==1 or k==i or k==2*n-i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

hollow_diamond(5)