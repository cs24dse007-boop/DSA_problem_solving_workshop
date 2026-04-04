#user function
# def msg():
#     print("Hello World")

# msg() #calling function
# msg()
#-------------------------------------------------------------------------------------------------
# def arithmetic():
#     a=int(input("Enter the value of A:"))
#     b=int(input("Enter the value of B:"))
#     add=a+b
#     sub=a+b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div

# # print(arithmetic())#function call
# result=arithmetic()
# print("Arithmetic=",result)
#-------------------------------------------------------------------------------------------------
#how many types of arguments we can pass in function
#1.positional argument
#2.keyword argument
#3.default argument
#4.variable number of argument/variable length argument
#-------------------------------------------------------------------------------------------------
#1.positional argument
# def login(username,password):
#     if username==password:
#         print("login successfully")
#     else:
#         print("login unsuccessful")
# username=input("Enter the user name:")
# password=input("Enter the password:")
# login(username,password)
#-------------------------------------------------------------------------------------------------
# #2.keyword argument
# def login(username,password):
#     if username==password:
#         print("login successfully")
#     else:
#         print("login unsuccessful")
# username=input("Enter the user name:")
# password=input("Enter the password:")
# login(username="admin",password="admin")
#-------------------------------------------------------------------------------------------------
#3.default argument
# def cityName(city="Goa"):
#     print(city)
    
# cityName("Delhi")
# cityName("Nagpur")
# cityName()
#-------------------------------------------------------------------------------------------------
#4.variable number of argument/variable length argument
# def nameOfCitys(*city):
#     print("City Name's=",city)

# nameOfCitys("Goa","Nagpur","Mumbai","Pune","Nashik")
#-------------------------------------------------------------------------------------------------
#WAP for menu driven code
# import sys
# def add():
#     val1=int(input("Enter the value of val1:"))
#     val2=int(input("Enter the value of val2:"))
#     print("Addition:",val1+val2) 
      
# def sub():
#     val1=int(input("Enter the value of val1:"))
#     val2=int(input("Enter the value of val2:"))
#     print("Subtraction:",val1-val2)
    
# def mul():
#     val1=int(input("Enter the value of val1:"))
#     val2=int(input("Enter the value of val2:"))
#     print("Multiplication:",val1*val2)
# def div():
#     val1=int(input("Enter the value of val1:"))
#     val2=int(input("Enter the value of val2:"))
#     print("Division:",val1/val2)

# while True:
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5. exit")
#     choice=int(input("Enter the choice:"))
#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice==3:
#         mul()
#     elif choice==4:
#         div()
#     elif choice==5:
#         sys.exit()   
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------