ch=ord(input("Enter the character:"))

#ord()-used to convert in ASCII code
if ch>=65 and ch<=91:
    print("Your entered character is in upper case")
elif ch>=97 and ch<=122:
    print("Your entered character is in lower case")
elif ch>=48 and ch>=57:
    print("Your entered character is in Numbers")
else:
    print("Your entered character is in special symbol")
