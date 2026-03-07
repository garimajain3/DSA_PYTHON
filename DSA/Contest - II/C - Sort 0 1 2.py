# n = int(input())
# marks = list(map(int,input().split()))

# result = sorted(marks,reverse=True)
# print(*result)


# second method
n = int(input())
marks = list(map(int,input().split()))


for i in range(len(marks)):
    for j in range(len(marks)-i-1):
        if(marks[j]<marks[j+1]):
            marks[j],marks[j+1] = marks[j+1] , marks[j]
            
print(*marks)