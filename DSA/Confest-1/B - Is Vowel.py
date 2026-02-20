a = input().lower()
l = ['a','e','i','o','u']
for i in range(len(l)):
    if a==l[i]:
        print("YES")
        break
else:
    print("NO")
    