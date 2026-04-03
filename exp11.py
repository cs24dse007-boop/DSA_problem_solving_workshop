#nested if else:WAP to accept of A,B,C and find max

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if a>b:
    if a>c:
        print("a is max:",a)
    else:
        print("c is max",c)
else:
    if b>c:
        print("b is max:",b)
    else:
        print("c is grater",c)
        
