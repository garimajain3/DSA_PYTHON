n = int(input())
res = []
def hello_function(n):
    for i in range(n,0,-1):
        if(n%i==0):
            res.append(i)
    print(*res)
hello_function(n)