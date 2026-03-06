n = int(input())
def prime_function(n):
    for i in range(2,int(n//2)+1):
        if(n%2==0):
            print("Not Prime")
            break
    else:
        print("Prime")
prime_function(n)