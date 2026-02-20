n = input()

def count_zero(n):
    count = 0
    for i in range(len(n)):
        if(int(n[i])==0):
            count+=1
    print(count)

count_zero(n)         
