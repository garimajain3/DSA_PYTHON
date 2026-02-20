n = int(input())
numbers = [int(num) for num in input().split()]
 
max_index = 1
max_number = numbers[0]
 
for i in range(len(numbers)):
    if(numbers[i]>max_number):
        max_number = numbers[i]
        max_index = i+1
print(max_number,max_index)