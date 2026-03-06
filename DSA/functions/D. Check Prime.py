n = int(input())
def prime_function(n):
    if n==0 or n==1:
        print("Not prime")
        return
    for i in range(2,n):
        if(n%i==0):
            print("Not Prime")
            break
    else:
        print("Prime")
prime_function(n)