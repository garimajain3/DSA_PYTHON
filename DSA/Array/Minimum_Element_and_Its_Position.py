n = int(input())
numbers = [int(num) for num in input().split()]

min_index = 1
min_number = numbers[0]

for i in range(n):
    if(numbers[i]<min_number):
        min_number = numbers[i]
        min_index = i+1
print(min_number,min_index)