def Quick_sort(arr,l,r):
    if(l<r):
        p = partation(arr,l,r)
        Quick_sort(arr,l,p-1)
        Quick_sort(arr,p+1,r)
        
def partation(arr,l,r):
    pivot = arr[l]
    i = l+1
    j = r
    
    while True:
        while(i<=j and arr[i]<pivot):
            i+=1
        while(i<=j and arr[j]>pivot):
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[j] , arr[l] = arr[l] , arr[j]
    return j

a = [2,5,6,45,-5,8,3,0]
Quick_sort(a,0,len(a)-1)
print(a)