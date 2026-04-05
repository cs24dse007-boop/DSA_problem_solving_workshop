# print("prashantjha777".isalnum()) #combination of number and alphabets
# print("prashantjha".isalpha())
# print('777f'.isdigit())
# print("'sdsdsdsd".islower())
# print(' '.islower())
# print('PRASHANTj'.isupper())
# print("My Name Is Prashant".istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo")) 
#-----------------------------------------------------------------------------------------
# print("Prashant".find("r"))
# print("Prashant".index("r"))
# print("prashant jha".count("a"))
#-----------------------------------------------------------------------------------------
# dict={"name":"Alice","age":30}
# i=int(input("Enter the key:"))

#-----------------------------------------------------------------------------------------
# mydict={1,2,3,3,4,5}
# mydict1={}
# for i in mydict:
#     if i in mydict1:
#         mydict1[i]+=1
#     else:
#         mydict1[i]=1
# print(mydict1)
#-------------------------------------------------------------------------------------------------
# a=[5,7,8,3,7,8,9,2,3]
# b=[]
# for i in range(len(a)):
#     counter=0
#     key=a[i]
    
#     j=i+1
#     while j<len(a):
#         if key==a[j]:
#             b.append(key)
#         j=j+1
   
   
# print(len(b))
#-------------------------------------------------------------------------------------------------
#find the second largest element
# list=[7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])
#-------------------------------------------------------------------------------------------------
# i=1
# while i<=5:
#     print(i)
#     i=i+1

#-------------------------------------------------------------------------------------------------
# username=""
# password=""
# while username!="admin" or password!="admin":
#     username=input("enter username:")
#     password=input("enter password:")
#-------------------------------------------------------------------------------------------------
# name='programming'
# vowels=['a','e','i','o','u']
# cons=0
# vowel=0
# for i in name:
#     if i in vowels:
#         vowel+=1
#     else:
#         cons+=1
# print("consonent:",cons)
# print("vovels:",vowel)
#-------------------------------------------------------------------------------------------------
# list=[1,2,2,3,4,2]
# list1=[]
# a=int(input("Enter the value"))
# for i in a:
#     if i!=a:
#         list1+=a
# print(list1)
    
#-------------------------------------------------------------------------------------------------
# list=[2,3,4,5]
# product=1
# for i in list:
#     product*=i
# print(product)
#-------------------------------------------------------------------------------------------------
# f1=open("DFD0.jpeg","rb")
# f2=open("Rossom.jpeg","wb")
# data=f1.read()
# f2.write(data)
# print("New image is available with the name:")
#-------------------------------------------------------------------------------------------------
# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# # a.writerow(["StudentID","rollno","name","mobileno"])
# studentid=int(input("Enter the student id:"))
# rollno=int(input("Enter the roll no:"))
# name=input("Enter the student name")
# mobileno=int(input("enter the mobile number:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("Student record has save")
#-------------------------------------------------------------------------------------------------
# import csv
# f=open("student2.csv","a",newline="")
# a=csv.writer(f)
# #a.writerow(["rollno","name","nobileno","p1","p2","p3","total","percentage","email","result"])
# rollno=int(input("Enter the student roll no:"))
# name=input("Enter the student name")
# mobileno=int(input("enter the mobile number:"))
# p1=int(input("enter the subject 1:"))
# p2=int(input("enter the subject 2:"))
# p3=int(input("enter the subject 3:"))
# total=p1+p2+p3
# percentage=total/300*100
# email=input("enter the email:")
# result=[]
# if p1>=40 and p2>=40 and p3>=40:
#     result="pass"
# else:
#     result="fail"
# a.writerow([rollno,name,mobileno,p1,p2,p3,total,percentage,email,result])
# print("Student record has save")
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------