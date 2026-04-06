# class Student:
    
#     roll_no=101 #data member

#     def studentData(self): #Method/member function
#         print("Student Information")
        
# obj=Student()
# print(obj.roll_no)
# obj.studentData()
#-------------------------------------------------------------------------------------------------------
# class Demo:
#     def __init__(self):
#         print("I am constructor")
        
#     def msg(self):
#         print("Hello class:")
# obj1=Demo()
# # print(obj1)
# obj2=Demo()
# obj1.msg()
#--------------------------------------------------------------------------------------------------------
# class HOD:
#     def __init__(self): #default constructor
#         self.name='omkar bhalekar'
#         self.age=3
#         self.empid=1001
#     def info(self):
#         print("My name is:",self.name)
#         print("My age is:",self.age)
#         print("My emp id:",self.empid)
# obj=HOD() #object create
# obj.info()
#--------------------------------------------------------------------------------------------------------    
# class HOD:
#     def __init__(self,name,age,rollno): #parameterise constructor constructor
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#     def info(self):
#         print("My name is:",self.name)
#         print("My age is:",self.age)
#         print("My roll no is:",self.rollno)
# obj=HOD('Arjun',45,101) #object create
# obj.info()   
#-------------------------------------------------------------------------------------------------------
# class New:
#     def __init__(self):
#         self.a=10
# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a=20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
#-------------------------------------------------------------------------------------------------------
#declaring instance variable outside a class by using object
# class Student:
#     def __init__(self):
#         self.s_name="omkar"
#         self.s_rollno=101 #declaring the instance var inside the a constructor
    
#     def getData(self):
#         self.s_mb=234567890
        
# obj=Student()
# obj.getData()
# del obj.s_mb      #delete the instance variable by using obj
# obj.s_branch="cs" #adding instance variable by using object
# print(obj.__dict__)
#-------------------------------------------------------------------------------------------------------
# class New:
#     a=10   #static var
#     def __init__(self):
#         self.name="Omkar" #instance var
# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)        
#-------------------------------------------------------------------------------------------------------
# import sys
# class Crud:
#     def __init__(self):
#         print("Student managemnt system")
#         self.studentID=[]
#         self.studentName=[]
#         self.studentRollNo=[]
#         self.studentCity=[]
        
#     def addStudent(self):
#         self.studentID.append(input("Enter the student id:"))
#         self.studentRollNo.append(input("Enter the student roll no:"))
#         self.studentName.append(input("Enter the student name:"))
#         self.studentCity.append(input("Enter the student city:"))
        
#     def showStudent(self):
#         print("Students Detais are:")
#         print("Student ID",self.studentID)
#         print("Student Roll no",self.studentRollNo)
#         print("Student Name",self.studentName)
#         print("Student City",self.studentCity)
        
#     def updateStudent(self):
#         print("Student ID",self.studentID)
#         print("Student Roll no",self.studentRollNo)
#         print("Student Name",self.studentName)
#         print("Student City",self.studentCity)
#         print("Really want to update")
#         self.studentID.append(input("Enter the student id:"))
#         self.studentRollNo.append(input("Enter the student roll no:"))
#         self.studentName.append(input("Enter the student name:"))
#         self.studentCity.append(input("Enter the student city:"))
#         print("Student ID",self.studentID)
#         print("Student Roll no",self.studentRollNo)
#         print("Student Name",self.studentName)
#         print("Student City",self.studentCity)
#     def deleteStudent(self):
#         print("Student ID",self.studentID)
#         print("Student Roll no",self.studentRollNo)
#         print("Student Name",self.studentName)
#         print("Student City",self.studentCity)

        
        
# obj1=Crud()
# obj1.addStudent
# obj1.showStudent
# obj1.updateStudent
# obj1.deleteStudent

# while True:
#     print("1.Add Student")
#     print("2.Show Student")
#     print("3.Update")
#     print("4.Delete")
#     print("5. exit")
#     choice=int(input("Enter the choice:"))
#     if choice==1:
#         obj1.addStudent()
#     elif choice==2:
#         obj1.showStudent()
#     elif choice==3:
#         obj1.updateStudent() 
#     elif choice==4:
#         obj1.deleteStudent()       
#     elif choice==5:
#         sys.exit()      
#-------------------------------------------------------------------------------------------------------
class Student:
    def __init__(self,name,rollno,mob):
        self.name=name
        self.rollno=rollno
        self.mob=mob
    def display(self):
        print(self.name,"",self.rollno,"",self.mob)
        
stud=Student("Omkar",1001,6464646464)
stud.display()       
#-------------------------------------------------------------------------------------------------------
#static method
# class Student:
#     #by using class name we can access static method
#     @staticmethod #decor
#     def get_personal_detail(firstname,lastname):
#         print("Your personal details:",firstname,lastname)
        
#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact details:",mobile_no,rollno)
# Student.get_personal_detail("Omkar","Bhalekar")
# Student.contact_detail(345678,4)
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
