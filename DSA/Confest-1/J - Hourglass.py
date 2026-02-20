n = int(input())
# for i in range(n,0,-1):
    # for k in range(n-i): #
    #     print(" ",end="")
        
    #     # i = 5 , 10-5 = 5 | i=4 8-4 = 4 
    # for j in range(i): 
    #     print(".",end=" ")
    # print()
    
           
# for l in range(2,n+1):
#     for k in range(n-l): #
#         print(" ",end="")
        
#         # i = 5 , 10-5 = 5 | i=4 8-4 = 4 
#     for j in range(l): 
#         print(".",end=" ")
#     print()
    
    
# without trailing sace
for i in range(n, 0, -1):
    print(" " * (n - i) + " ".join(["."] * i))
    
for l in range(2, n + 1):
    print(" " * (n - l) + " ".join(["."] * l))