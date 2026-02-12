def selection_sort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i,n):
            if(a[min]>a[j]):
                min = j
        a[i],a[min] = a[min],a[i]
    return a
    
    
a = [2,5,6,2,5,8,3,0]
print(selection_sort(a))