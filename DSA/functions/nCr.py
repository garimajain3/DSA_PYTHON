n ,r = map(int,input().split())

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
    
def binomial_coefficient(n,r):
    if r>n:
        return 0
    if  r==0 or r==n:
        return 1
    if r==1:
        return n
    
    return factorial(n)//(factorial(r)*factorial(n-r))
    
print(binomial_coefficient(n,r))        
