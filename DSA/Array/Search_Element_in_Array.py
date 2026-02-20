n , x = map(int , input().split())
numbers = [int(num) for num in input().split()]
found = False
for i in numbers:
    if i==x:
        found = True
        print("YES")
        break
if(found==False):
    print("No")