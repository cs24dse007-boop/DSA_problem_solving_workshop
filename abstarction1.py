# from abc import ABC,abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def traning(self):
#         pass
#     @abstractmethod
#     def placement(self):
#         pass
# class Ashish(Help4code):
#     def traning(self):
#         print('C',"C++","Java")
#     def placement(self):
#         print("Java placement")
# class Ankush(Help4code):
#     def traning(self):
#         print("Python |D-jango")
#     def placement(self):
#         print("Python placement students")
# class Prashant(Help4code):
#     def traning(self):
#         print("Machine learning")
#     def placement(self):
#         print("Data science placement")
# obj1=Ashish()
# obj1.traning()
# obj1.placement()

# obj2=Ankush()
# obj2.traning()
# obj2.placement()

# obj3=Prashant()
# obj3.traning()
# obj3.placement()

#---------------------------------------------------------------------------------------------------------
from abc import ABC,abstractmethod
class Irctc(ABC):
    @abstractmethod
    def bookTicket(self):
        pass
class MakeMyTrip(Irctc):
    def bookTicket(self):
        print("===================================================")
        print(" Welcome to makemytrip.com")
        source=input("Enter the source station:")
        destination=input("Enter the destination name:")
        date=input("enter the date:")
        print("====================================================")
        
class GoIbibo(Irctc):
    def bookTicket(self):
        print("===================================================")
        print("Welcome to GoIbibo:")
        source=input("Enter the source station:")
        destination=input("Enter the destination name:")
        date=input("enter the date:")
        print("===================================================")
        
class Yatra(Irctc):
    def bookTicket(self):
        print("===================================================")
        print("Welcome to Yatar:")
        source=input("Enter the source station:")
        destination=input("Enter the destination name:")
        date=input("enter the date:")
        print("===================================================")
obj1=MakeMyTrip()
obj1.bookTicket()

obj2=GoIbibo()
obj2.bookTicket()

obj3=Yatra()
obj3.bookTicket()