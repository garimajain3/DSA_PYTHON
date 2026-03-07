row , col = map(int,input().split())

matrics = []

for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)


res = []
for i in range(len(matrics)):
    minimum = matrics[i][0]
    for j in range(len(matrics[0])):
        if(matrics[i][j]<minimum):
            minimum = matrics[i][j]
            
    res.append(minimum)
print(*res)
        