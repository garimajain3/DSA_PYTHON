# n,m = map(int,input().split())
n = int(input())
 
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()