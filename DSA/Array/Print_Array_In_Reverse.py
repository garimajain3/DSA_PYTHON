n = int(input())
numbers = [int(num) for num in input().split()]
print(*numbers[::-1])