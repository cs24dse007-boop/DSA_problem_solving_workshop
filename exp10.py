#WAP to accept phy,che,and maths subject marks calculate total percentage and if
#percentage is greater then equal to 60 and gender is equal to make so he is elligible for placement else
#elligible for dataentry job

phy=int(input("Enter the marks of phy:"))
che=int(input("Enter the marks of che:"))
maths=int(input("Enter the marks of maths:"))
gender=input("enter the gender:")

total=phy+che+maths
per=total/300*100

print("Total:",total)
print("Percentage:",per)

if per>=60 and gender=="male":
    print("elligible for placement")
else:
    print("elligible for data entry job")
