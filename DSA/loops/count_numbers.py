

def count_no(n):
    
    t = {}
    for i in n:
        t[i] = 0
        if(i>0):
            t[i]+=1
        if(i<0):
            t[i]+=1
        if(i%2==0):
            t[i]+=1
        else:
            t[i]+=1
    print(t)

n = [-2,0,-3,7,5]
count_no(n)
            