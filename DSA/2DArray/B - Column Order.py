row , col = map(int,input().split())

matrics = []

for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)
# print("before",matrics)

for i in range(len(matrics[0])):
    for j in range(len(matrics)):
        print(matrics[j][i],end=" ")
    # print()
# print("after",*matrics)
    
        
        