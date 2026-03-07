row , col , x = map(int,input().split())

matrics = []

for _ in range(row):
    row = [int(x) for x in input().split()]
    matrics.append(row)

counter = 0  
for i in range(len(matrics)):
    for j in range(len(matrics[0])):
        if(matrics[i][j]==x):
            counter = 1
            
if(counter>0):
    print("true")
else:
    print("false")