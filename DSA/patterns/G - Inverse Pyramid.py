# n,m = map(int,input().split())
n = int(input())
 
 
for i in range(n,-1,-1):
    for j in range(i):
        print("*",end="")
    print()