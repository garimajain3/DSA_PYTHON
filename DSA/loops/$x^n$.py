x,n = map(int,input().split())
# print(x**n)
p = 1
for i in range(n):
    p = p*x
print(p)