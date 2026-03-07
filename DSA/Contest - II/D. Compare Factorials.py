# fact1 , fact2 = map(int,input().split())

# result1 = 1
# result2 = 1

# for i in range(1,fact1+1):
#     if(fact1 == 0 or fact1 ==1):
#         result1 = 1
#         break
#     result1 = result1*i

# for i in range(1,fact2+1):
#     if(fact2 == 0 or fact2 ==1):
#         result2= 1
#         break
#     result2 = result2*i
    
# if(result1==result2):
#     print("Yes")
# else:
#     print("No")




fact1 , fact2 = map(int,input().split())

if(fact1==fact2):
    print("yes")
elif(fact1 == 0 and fact2 ==1):
    print("Yes")
elif(fact1==1 and fact2==0 ):
    print("Yes")
else:
    print("No")