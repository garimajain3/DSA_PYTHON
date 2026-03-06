inp = input()
# inp = "aaaa"
removeCharacter = input()
output = []
for i in range(len(inp)):
    if(inp[i]!=removeCharacter):
        # print("hi",inp[i])
        output.append(inp[i])
        continue
    else:
        # print("hello")
        output+= ''
        
    
print(''.join(output))