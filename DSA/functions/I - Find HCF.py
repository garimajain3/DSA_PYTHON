n,x = map(int,input().split())
res1 = []
res2 = []
def hcmf(n,x):
    for i in range(1,n+1):
        if(n%i==0):
            res1.append(i)
    for j in range(1,x+1):
        if(x%j==0):
            res2.append(j)
    # print(res1)
    # print(res2)
    res = list(set(res1) & set(res2))
    maximun = res[0]
    # print(maximun)
    # print(res)
    for i in range(1, len(res)):
       
        if(res[i]>maximun):
            maximun = res[i]
    print(maximun)
hcmf(n,x)

