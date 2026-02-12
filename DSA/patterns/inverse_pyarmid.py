def inverse_pyarmid(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print("")
        
inverse_pyarmid(5)