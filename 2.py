








----------------------------------------------------------------------------------------------------------
math=50
chem=50
name="Omkar"
result=True
pi=3.14
print(id(math))
print(id(chem))
print(id(name))
print(id(result))
print(id(pi))

----------------------------------------------------------------------------------------------------------
math=50
chem=50
phy=50
hindi=40
print(id(math))
print(id(chem))
print(id(phy))
print(id(hindi))

----------------------------------------------------------------------------------------------------------
print(2+2)
print("2"+"2")
val1=int(input("enter value of val:"))#2
val2=int(input("enter the value of val2:"))#4
print(val1+val2)#input function bydefult accept only string value

----------------------------------------------------------------------------------------------------------

print(int(3.14))
#print(int(10+ij))#we cannot convert complex value into int
print(int(True))
print(int(False))
#print(int("4.22"))#we cannot convert floating point value string into int
print(int("4"))
print(int("Omkar"))#cannot convert into int
----------------------------------------------------------------------------------------------------------


print(float(3))
#print(float(50+2j))#we cannot convert complex value into float
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))
#print(float("Name"))#cannot convert string into float


print(complex(3))
print(complex(12,5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
#print(complex("Name"))#cannot convert string into float
print(complex(5,-3))
print(complex(True,False))


#bool()
print(bool(0))#Fales
print(bool(15))#True
print(bool(0+0j))#Fales
print(bool(3.14))#True
print(bool(0.0))#Fales
print(bool(1+2j))#True
print(bool(-1))#True
print(bool(False))
print(bool(True))#True
print(bool())#Fales
print(bool("Omkar"))#True


math=50
name="Omkar"
result=True
pi=3.14
print(type(math))
print(type(name))
print(type(result))
print(type(pi))


