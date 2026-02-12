def bin_payramid(no):
    n = str()
    for i in range(1,no+1):
        if(i%2!=0):
            n = str(0) + n
        else:
            n = str(1) + n
        print(n)
            
            
            
            
        
        
bin_payramid(6)