n = int(input())
marks = list(map(int,input().split()))
# pass_mark = int(input())
min_race = min(marks)
# print(min_race)
last_index = -1
for i in range(len(marks)):
    if(marks[i]==min_race):
        last_index = i+1
print(last_index)
    
    
    