n = int(input())
res = []
s = "I am learning functions"
def hello_function(n):
    
    for _ in range(n):
        res.append(s)
    print(*res,sep='\n')
hello_function(n)