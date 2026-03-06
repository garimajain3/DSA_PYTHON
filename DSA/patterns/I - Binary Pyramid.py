# def bin_payramid(no):
#     n = str()
#     for i in range(1,no+1):
#         if(i%2!=0):
#             n = str(0) + n
#         else:
#             n = str(1) + n
#         print(n)
            
            
            
            
        
        
# bin_payramid(6)


n = int(input())
for i in range(n):
    for j in range(i+1):
        if((i+j)%2==0):
            print("0",end="")
            
        else:
            print("1",end="")
    
            
            
        
    print()