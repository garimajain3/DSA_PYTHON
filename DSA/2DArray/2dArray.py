'''
1 00   2 01   3 02  91 03
4 10   5 11   6 12  92 04
7 20   8 21   9 22  93 05

print

1 4 7 
2 5 6
3 6 8
91 92 94
'''

nums = [[1,2,3],[4,5,6],[7,8,9]]
row = len(nums)
col = len(nums[0])
# print("row",row)
# print("column",col)

for i in range(row):
    for j in range(col):
        print(nums[i][j])
    print()
    
