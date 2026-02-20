inp = input()
c1 , c2 = input().split()
# print(c1)
# print(c2)
output = []

for i in range(len(inp)):
    if(inp[i]==c1):
        output.append(c2)
    else:
        output.append(inp[i])
print(''.join(output))