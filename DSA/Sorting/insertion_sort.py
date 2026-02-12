def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while(j>=0 and key<a[j]):
            a[j+1] = a[j]
            j-=1
            
        a[j+1] = key
    return a
    



a = [2,5,6,2,5,8,3,0]
print(insertion_sort(a))