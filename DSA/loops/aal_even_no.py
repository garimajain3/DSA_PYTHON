def even(no):
    e = []
    for i in range(1,no+1):
        if(i%2==0):
            e.append(i)
    print(e,end=" ")
    
even(10)