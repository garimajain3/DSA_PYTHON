def stringDistribute(s):
    
    # ans = []
    # size = 1
    # index = 0
    
    
    # while index<len(s): # 0 ,1 || 1,2 || 3,3 || 6,4
    #     ans.append(s[index:index+size]) # [0:1]=>a || [1:3] => bc || [3:6]=>def || [6,10]
    #     index+=size # 1 || 3 || 6 ||10 -> fail loop
    #     size+=1  # 2 || 3 || 4
    # return ans
    
    
    # two pointer
    
    ans = []
    size = 1
    start = 0
    while start<len(s):
        end = start + size
        ans.append(s[start:end])
        
        start+=size
        size+=1
    
    return ans
    
    
s = "abcdefghij"
print(stringDistribute(s))

