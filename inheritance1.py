#extending property from on eclass to another class is called inheritance
#Directly we are getting here reusability concept
#--------------------------------------------------------------------------------------------------
#single inheritance
# class College:
#     def college_name(self):
#         print("Modern college:")
# class Student(College):
#     def student_info(self):
#         print("Name:Omkar Bhalekar")
#         print("Branch :Computer")
    
# obj=Student()
# obj.college_name()
# obj.student_info()
#----------------------------------------------------------------------------------------------------
#multi-level
# class College:
#     def college_name(self):
#         print("Modern college:")
# class Student(College):
#     def student_info(self):
#         print("Name:Omkar Bhalekar")
#         print("Branch :Computer")
# class Exam(Student):
#     def subject(self):
#         print("Subject 1 :Designing Engineering")
#         print("Subject 2 : maths")
#         print("Subject 3: C-language")
        
    
# obj=Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()
#----------------------------------------------------------------------------------------------------
#miltiple inheritance
# class SubMarks:
#     math=int(input("enter the paper marks of math:"))
#     DE=int(input("Enter the marks of designing engineering:"))
#     c=int(input("Enter the paper marks of c language:"))
#     english=int(input("Enter the paper marksr of english:"))
    
# class PracMarks:
#     cpract=int(input("enter the practical marks of c:"))
    
# class Result(SubMarks,PracMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("Pass")
#         else:
#             print("fail")
# obj=Result()
# obj.total()
#----------------------------------------------------------------------------------------------------
#george hotz
#----------------------------------------------------------------------------------------------------
#polymorphism exapmle
# class Principal:
#     def role(self):
#         print("I am managing all activity of college:")
# class Dean:
#     def role(self):
#         print("Dean=I am decision taking person")
# class Hod:
#     def role(self):
#         print("Hod=I have responsibility of teachers and students:")
# class Faculty:
#     def role(self):
#         print("Faculty=I have to complete syllabus successfully:")

# def fun(obj):
#     obj.role()
# campus=[Principal(),Dean(),Hod(),Faculty()]
# for obj in campus:
#     fun(obj)
#----------------------------------------------------------------------------------------------------
#python does not method overloading and constructor overloading
# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=Arithmetic()
# obj.add(10)
# obj.add(20,30)
# obj.add(1,2,3)

#general solution
# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("Enter the atleast two arguments")
    
# obj=Arithmetic()
# obj.add(10)
# obj.add(20,30)
# obj.add(1,2,3)

#----------------------------------------------------------------------------------------------------
#constructor overloading
# class Arithmetic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self,a):
#         print("passing one argument")
#     def __init__(self,a,b):
#         print("passing two arguments")
# obj=Arithmetic()
# obj=Arithmetic(10)
# obj=Arithmetic(2,2)
#----------------------------------------------------------------------------------------------------
#python supports both constructor overriding and method overriding
# class Rbi:
#     def home_loan(self):
#         print("Home loan=7.5")
#     def car_loan(self):
#         print("car loan=8%")
# class Sbi:
#     def home_loan(self):
#         print("Sbi provide home loan=6.5")
#         super().home_loan() #using super() you can access the parent class method in the child class
        
# obj=Sbi()
# obj.home_loan() #child class method override the parent class
#----------------------------------------------------------------------------------------------------
#constructor overriding
# class Father:
#     def __init__(self):
#         print("Father= i am already at breakfast table:")
        
# class Child(Father):
#     def __init__(self):
#         print("child=i will be late for breakfast")
#         super().__init__()
        
        
# obj=Child()
    
    

