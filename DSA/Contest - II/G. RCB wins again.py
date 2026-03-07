n = int(input())
marks = list(map(int,input().split()))

result = []
left = n//2-1
right = n//2

while left>=0 and right<n:
    result.append(marks[left])
    result.append(marks[right])
    left -=1
    right +=1
print(*result)