def max_min(arr,start,end):
    if(start==end):
        return arr[start] , arr[end]

    if(start+1==end):
        if(arr[start]<arr[end]):
            return arr[start],arr[end]
        else:
            return arr[end],arr[start]
        
    mid = (start+end)//2
    min1 , max1 = max_min(arr,start,mid)
    min2,max2 = max_min(arr,mid+1,end)
    return min(min1,min2) , max(max1,max2)

a = [2,5,6,45,-5,8,3,0]
print(max_min(a,0,len(a)-1))
    