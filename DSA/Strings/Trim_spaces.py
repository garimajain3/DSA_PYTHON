inp = input()
output = []

for i in range(len(inp)):
    if(inp[i]==" "):
        output.append('')
        
    else:
        output.append(inp[i])
print(''.join(output))
        
    
        
        