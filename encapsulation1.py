# class Base:#parent class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a="prashant"#public data member
#         self.__c="Ashish"#private member

# #creating a derived class/child class        
# class Derived(Base):#child class
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         #print("Calling private number of base class:")
#         #print(self.a)
#         #print(self.__c)
# obj1=Derived()
# print(obj1.a)
# print(obj1.__c)
# # obj2=Base() #
# # print(obj2.a) #Accessible
# # print(obj2.__c) #not accesible

# class Rbi:
#     #declaring public method
#     def publicPolicy(self):
#         print("Check the public policy of RBI:")
        
#     #Declaring private method
#     def __privatePolicy(self):
#         print("There is some private policy which is not accessible:")
# class Sbi(Rbi):
#     def __init__(self):#first sbi class const called
#         Rbi.__init__(self)#second parent class constr called
        
#     def callingPublicMethode(self):#child class public method
#         print("\n inside the child class:")
#         self.publicPolicy()#calling 
#     def callingPrivateMethod(self):
#         self.__privatePolicy()
# obj1=Sbi()
# obj1.callingPublicMethode()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()

# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__Rbi__privatePolicy()

  