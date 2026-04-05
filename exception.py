# n1=int(input("Enter first value:"))
# n2=int(input("Enter the second value:"))
# print(n1/n2)
#-------------------------------------------------------------------------------------------------
# n1=int(input("Enter first value:"))
# n2=int(input("Enter the second value:"))
# try:
#     print(n1/n2)
# except:
#     print("can't divide by zero")
    
# print("To bo continue")
#-------------------------------------------------------------------------------------------------
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value")
    
# print("To bo continue")
#-------------------------------------------------------------------------------------------------
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)
#-------------------------------------------------------------------------------------------------
#the concept of default except block,generally we used
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# except:
#     print("this is default part of except block") 
#-------------------------------------------------------------------------------------------------
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)
# else:
#     print("Everything is ok")

#-------------------------------------------------------------------------------------------------
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)
# finally:
#     print("I will always executed")
#-------------------------------------------------------------------------------------------------
#nested try except block
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     try:
#         print(n1/n2)
#     except ZeroDivisionError as message:
#         print(message)
        
# except ValueError as message:
#     print(message)
#-------------------------------------------------------------------------------------------------
# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except (ValueError,ZeroDivisionError) as message:
#    print(message)
# else:
#    print("Everything is ok")
        
# finally:
#     print("I will always executed")
#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------

