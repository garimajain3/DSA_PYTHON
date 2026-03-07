row , col = map(int,input().split())

matrics = []

for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)
maximum = matrics[0][0]
for i in range(len(matrics)):
    for j in range(len(matrics[0])):
        if(matrics[i][j]>maximum):
            maximum = matrics[i][j]
print(maximum)