row, col = map(int, input().split())
 
matrics = []
 
for _ in range(row):
    r = list(map(int, input().split()))
    matrics.append(r)
 
result = []
 
for i in range(col):
    if i % 2 == 0:
        for j in range(row):
            result.append(str(matrics[j][i]))
    else:
        for j in range(row - 1, -1, -1):
            result.append(str(matrics[j][i]))
 
print(" ".join(result))