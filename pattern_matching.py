# import re
# count=0
# pattern=re.compile("function")
# #print(pattern)
# matcher=pattern.finditer("The return statement is used to return a value from a function,function parameters and arguments are distinct concepts Parameters are the names listed in the function definition Arguments are the values received by the function")
# #print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:",count)
#------------------------------------------------------------------------------------------------------------------
# import re
# count=0
# matcher=re.finditer('hi',"hihihihi")
# #print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:",count)

#--------------------------------------------------------------------------------------
# import re
# obj=input("Enter the any character")
# objmatch=re.finditer(obj,"a7b @k9z")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())

#-------------------------------------------------------------------------------------------------
# import re
# a=input("Enter the any string to match operation:")
# mtch=re.match(a,"python is very important language")->match the beggining of the statements then returns if math found return match then return None 
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching at beggining level")
#---------------------------------------------------------------------------------------------------
#fullmatch()->match full statement  
# import re
# a=input("Enter the any string to match operation:")
# mtch=re.fullmatch(a,"pythonisvery")#->fullmatch the full statements then returns if math found return match then return None 
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching at beggining level") 
#-----------------------------------------------------------------------------------------------------
#Search()->if the match is found anywhere in the string then it returns object else it will return None
# import re
# a=input("Enter the string to perform match operation:")
# mtch=re.search(a,"python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching  anywhere") 

#-----------------------------------------------------------------------------------------------------
# import re
# a=input("Enter the string to perform match operation:")
# f=open('myfile.txt','r')
# c=f.read()
# mtch=re.search(a,c)
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching  anywhere") 
#----------------------------------------------------------------------------------------------------    
#findall()->returns list which containing all matches
# import re
# mtch=re.findall('[^a-zA-Z0-9]',"abch3hd$bk72QDF@HE&shd#@")
# print(mtch)
#----------------------------------------------------------------------------------------------------
#sub()->this function perform substitution or replacement 
# re.sub(expression,replacement,string)here every match pattern will be replaced by provided replacement
# import re
# obj=re.sub('[a-zA-Z]','X',"2345 ABCD Fbdc deff")
# print(obj)
#----------------------------------------------------------------------------------------------------
#subn()->it is as similar to sub() function only one thing is different that is also return number of 
#replacement this returns in tuple where the first element is string and second one is number of replacement
# import re
# obj=re.subn('[0-9]','X',"2abi3gdf k6fdg78")
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement is=",obj[1])
#----------------------------------------------------------------------------------------------------
# import re
# mo=input("Enter the mobile number")
# obj=re.fullmatch('[0-9]\d(9)',mo)
# if obj!=None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")
#----------------------------------------------------------------------------------------------------
# import re
# s=input("Enter the Mail id:")
# obj=re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com ',s)
# if obj!=None:
#     print("Valid Mail id")
# else:
#     print("Invalid Mail id")
#---------------------------------------------------------------------------------------------------
import os,sys
fname=input("Enter file name:")
if os.path.isfile(fname):
    print("FIle exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist",fname)
    sys.exit()
print("The content of the file is:")
data=f.read()
print(data)
#---------------------------------------------------------------------------------------------------
