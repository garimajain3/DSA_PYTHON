# n,m = map(int,input().split())
n = int(input())
 
 
for i in range(n):
    if(i==0 or i==n-1):
        print(n*"*",end="")
        
    else:
        print("*"+(n-1)*" "+"*",end="")
    # for j in range(i):
    #     if(j==1):
    #         print("*",end="")
    # else:
    #     for j in range(i):
    #         if(j==0 or j==n-1):
    #             print("*")
    #         else:
    #             print(" ")
        # pass
    print()