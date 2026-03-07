row , col = map(int,input().split())
 
matrics = []
 
for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)
 
 
res = []
for i in range(len(matrics[0])):
    sums = 0
    for j in range(len(matrics)):
        sums+=matrics[j][i]
            
    res.append(sums)
print(*res)