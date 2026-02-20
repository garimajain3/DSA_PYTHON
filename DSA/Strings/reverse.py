s = input()
n = len(s)
rev = ''
# print(s[n::-1])
# print(n)
for i in range(n-1,-1,-1):
    rev+=s[i]
print(rev)