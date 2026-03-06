inp = input()
 
ans = ''
for i in range(len(inp)):
    if(inp[i].isupper()):
        ans+=inp[i].lower()
    else:
        ans+=inp[i].upper()
print(ans)