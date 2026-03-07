n = int(input())
marks = list(map(int,input().split()))

output = {}
for i in range(len(marks)):
    if(marks[i] not in output):
        output[marks[i]] = 1
    else:
        output[marks[i]] += 1
result = []
for key,value in output.items():
    if(value<=1):
        result.append(key)
print(*result)