# mylist=["omkar","Anish","komal","Ashish",77,"sandip",60.52,"omkar"]
# print(mylist)#['omkar', 'Anish', 'komal', 'Ashish', 77, 'sandip', 60.52, 'omkar']
# print(type(mylist))#<class 'list'>
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-2])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:3])
# print(mylist[:])
# print(mylist[::-1])

# mylist[2]="Akshay"
# print(mylist)#change index value

# if "Anish" in mylist:
#     print("yes anish is available")
# else:
#     print("Not available")

# mylist.append("harsh") #add element at the end
# mylist.append("laxman")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)

# mylist=[['omkar',"bhalekar"],[85.56],[444444,"yyy"]]
# print("example of multidimensional list:")
# print(mylist)
# #print(mylist[row0][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

#       0         1
# 0 =['omkar',"bhalekar"]
# 1 =[85.56],
# 2 =[444444,"yyy"]

# list1=["omkar","bhalekar"]
# print(list1*2)  #it will print 2 times

# list2=[50,60,70]
# print(list1+list2)  #combine list1 and list2 data

# list2=[50,60,70,'omkar']
# del list2
# print(list2)#Get error

# list2=[50,60,70,'omkar']
# del list2[2]
# print(list2)

# list2=[50,60,70,'omkar']
# list2.clear()#print empty list
# print(list2)

# name="Omkar"
# print(name)
# myname=list(name) #typecasting
# print(myname)

# list2=[50,60,70,'omkar']
# list2.reverse()
# print(list2)

#sorting example
# mylist=[50,60,70,39,89,54]
# mylist.sort()#reverse=true #39, 50, 54, 60, 70, 89 ascending order
# print(mylist)

#list alising
# mylist=[50,60,70,39,89,54]
# newlist=mylist #assigning the address
# print(id(mylist))
# print(id(newlist))

# mylist[0]="Omkar"
# print(mylist)
# print(newlist)

# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())


# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i],end="")

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)#ValueError: attempt to assign sequence of size 6 to extended slice of size 5

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# names=[4,2,5,6,8,2]
# for i in names:
#     print(i)
    

#A=[4,0,2,5,0,1] i/p
#B=[4,2,5,1,0,0] o/p
#moves zeros in last
# A=[4,0,2,5,0,1]
# for i in A:
#     if i==0:
#         A.remove(i)
#         A.append(i)
# print(A)
    

# A=[1,2,2,3,4,4,5]
# B=[]
# for i in A:
#     if i not in B:
#         B.append(i)
# print(B)

# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)

# n=int(input("Enter the size of array:"))
# arr=[]
# for i in range(n):
#     val=int(input("Enter the value of array:"))
#     arr.append(val)
# sum=0
# print(arr)
# for i in range(n):
#     if i+1 in range(n):
#         sum+=abs(arr[i] - arr[i+1])
# print(sum)
 
# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

# for i in range(1,5):
#      if i==3:
#          continue
#      print(i)


#zip()inside we can take multiple range()
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,"",j)

#WAP to move 
#input=prashant*is*good*programmer
#output=****prashantisgoodprogrammer

# name="prashant*is*good*programmer"
# name1=""
# val=''
# for i in name:
#     if i !='*':
#         name1 +=i
#     else:
#         val+=i

# print(name1)
# print(val)
# print(str(val+name1)) #***prashantisgoodprogrammer


# #BOADMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)
# print(id(x==y))
# print(id(x==z))
# print(id(x != z))

# val1="listen"
# val2="silent"
# if sorted(val1) == sorted(val2):
#     print("anagram")
# else:
#     print("not")

#counts words in string
# val="This is the my sentence"
# count=1
# for i in val:
#     if i==" ":
#         count+=1
# print(count)


    