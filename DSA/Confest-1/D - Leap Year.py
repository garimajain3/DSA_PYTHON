leap_year = int(input())
if(leap_year%400==0):
    print("Yes")
elif(leap_year%4==0):
    if(leap_year%100!=0):
        print("Yes")
    else:
        print("No")
else:
    print("No")