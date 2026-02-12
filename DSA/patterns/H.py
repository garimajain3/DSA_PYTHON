def numbered_tringle(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print("")
numbered_tringle(5)