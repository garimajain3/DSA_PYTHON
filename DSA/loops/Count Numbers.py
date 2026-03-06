n = int(input())
l = list(map(int,input().split()))
# print(len(l))
# -2 0 3 7 -5
# output = 2
# 2
# 2
# 3
countPositiveNumber = 0
countNegativeNumber = 0
countEvenNumber = 0
countOddNumber = 0
for i in range(len(l)):
    if(l[i]>0):
        countPositiveNumber+=1
    if(l[i]<0):
        countNegativeNumber+=1
    if(l[i]%2==0):
        countEvenNumber+=1
    if(l[i]%2!=0):
        countOddNumber+=1
print(countPositiveNumber)
print(countNegativeNumber)
print(countEvenNumber)
print(countOddNumber)
        
        
        
        


    
    