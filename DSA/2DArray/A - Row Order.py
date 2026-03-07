row , col = map(int,input().split())

matrics = []

for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)
# print("before",matrics)

for i in range(len(matrics)):
    for j in range(len(matrics[0])):
        print(matrics[i][j],end=" ")
    # print()
# print("after",*matrics)
    
        
        