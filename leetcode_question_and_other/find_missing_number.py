def findMissingNumber(n,numberList):
    # first method  best Time: O(n) Space: O(1)
    sums = 0
    for i in numberList:
        sums+=i
    TotalNumber = (n*(n+1))//2
    missingNumber = TotalNumber-sums
    return missingNumber
    
    # ---------------------------------------------------------------------------#
    # second method worst Time: O(n log n) Space: O(1)
    # numberList.sort()
    # for i in range(len(numberList)):
    #     if(numberList[i]!=i+1):
    #         return i+1
            
    # return n
            
    

n = 5
numberList = [1,2,4,5] 
print(findMissingNumber(n,numberList))