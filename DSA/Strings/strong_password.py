s = input()
counterDigit = 0
counterUpper = 0
counterLower = 0
counterSpecial = 0

if(len(s)==10):
    
    for i in range(len(s)):
        if(s[i].isupper()):
            # print("lower")
            counterUpper+=1
        elif(s[i].islower()):
            # print("upper")
            counterLower+=1
            
        elif(s[i].isdigit()):
            # print("no")
            
            counterDigit+=1
        else:
            # print("special")
            counterSpecial+=1
# print(counterUpper)
if(counterUpper>0 and counterLower>0 and counterDigit>0 and  counterSpecial>0):
    print("Strong")
else:
    print("Weak")