char_no = input()
if(48<=ord(char_no)<=57):
    print("Digit")
elif(65<=ord(char_no)<=90):
    print("Uppercase")
elif(97<=ord(char_no)<=122):
    print("Lowercase")
elif(32<=ord(char_no)<=47 or 58<=ord(char_no)<=64 or 91<=ord(char_no)<=96 or 123<=ord(char_no)<=126):
    print("Special")
    
    

