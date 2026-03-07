row , col = map(int,input().split())
 
matrics = []
 
for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)
 
 
# res = []
for i in range(len(matrics)):
    if(i%2==0):
        for j in range(len(matrics[0])):
            print(matrics[i][j],end=" ")
    else:
        for j in range(len(matrics[0])-1,-1,-1):
            print(matrics[i][j],end=" ")