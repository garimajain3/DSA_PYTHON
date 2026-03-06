n,m = map(int,input().split())
# n = int(input())
 
 
for i in range(n):
    if(i==0 or i==n-1):
        print("*"*m,end="")
    else:
        print("*" + (m-2)*" " + "*",end="")
    print()
        