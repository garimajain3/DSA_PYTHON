def search_insert_position(nums,target):
    left = 0
    right = len(nums)-1
    while left <=right:
        mid = (left+right)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            left = mid+1
        else:
            right = mid -1
    return left
    
    
# nums = [1,3,5,6]
# target = 5
# print(search_insert_position(nums,target))

nums = [1,3,5,6]
target = 4
print(search_insert_position(nums,target))


'''
dry run 
nums = [1,3,5,6] target = 4 ans= 2

l = 0
r = 4-1 = 3

---------1 round --------
0<=3
mid = 1 (3+0)//2
1) 3 == 4 ->no
2) 3<4 ->YES
l = 1+1 = 2


------ 2 round -------

2<=3
mid = 5//2 = 2
5==4 ->no
5<4 ->no l = 2
r = 3-1 = 2

-----------3 rounf -------

2<=2
mid = 2+2//2 = 2
5==4 ->no
5<4 ->no
r = 2-1 = 1

-------- 4 runf -----
2<=1 -> no
return left = 2








'''
