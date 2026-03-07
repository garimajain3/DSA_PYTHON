n = int(input())
result = []
for i in range(2,n+1):
    if(n%i==0):
        result.append(i)
l = []
flag = False
for i in result:
    if(i%10==2 or i%10==7):
        l.append(i)
        flag= True
        
if(flag):
    print(*l)
else:
    print(-1)