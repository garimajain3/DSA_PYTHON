n = int(input())
res = []
def hello_function(n):
    for i in range(1,n+1):
        if(n%i==0):
            res.append(i)
    print(*res)
hello_function(n)