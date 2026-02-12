def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1-i):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1] ,a[j]
    return a

a = [2,5,6,2,5,8,3,0]
print(bubble_sort(a))