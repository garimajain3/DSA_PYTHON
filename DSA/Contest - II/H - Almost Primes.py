n = int(input())

result = []
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
        if(count>4):
            break
    
    if count <= 4:   # important condition
        result.append(i)
print(*result)