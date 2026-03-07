n = int(input())
marks = list(map(int,input().split()))

flag = True
for i in range(1,len(marks)):
    if(marks[i-1]!=marks[i]):
        flag = False
        break
if(flag==True):
    print("YES")
else:
    print("NO")