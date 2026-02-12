def hollow_sqaure(n):
    for i in range(n):
        if(i==0 or i==n-1):
            print("*"*n,end= "\n")
        
        else:
            print('*' + " "*(n-2) + "*")
hollow_sqaure(5)
        