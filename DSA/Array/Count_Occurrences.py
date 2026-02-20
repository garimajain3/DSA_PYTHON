n , x = map(int , input().split())
numbers = [int(num) for num in input().split()]
# x = 3
# numbers = [1, 5, 2, 3, 7, 3]
count = 0
for i in numbers:
    if i==x:
        count+=1
print(count)