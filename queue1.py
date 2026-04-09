# #Stack implementation with size limit
# import sys
# class Queue:
#     def __init__(self,queueSize):#parameterized constructor
#         self.queueList=[] #Queue created
#         self.queueSize=queueSize
        
#     def isFull(self):
#         if len(self.queueList)== self.queueSize:
#             return True
#         else:
#             return False      
#     def Enqueue(self,value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.queueList.append(value)
            
#     def displayQueue(self):
#         print("-----------------------------")
#         print(self.queueList)
#         print("-----------------------------")
        
#     def isEmpty(self):
#         if self.queueList==[]:
#             return True
#         else:
#             return False
        
#     def Dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty" 
#         else:
#             return self.queueList.pop(0)
        
#     def deleteQueue(self): #Delete the Queue
#         self.queueList=None
#         return "Queue is deleted"
        
    
#     def peek(self): #it returns first element of a queue
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.queueList[0] #slicing of list

# size=int(input("Enter the queue size:"))        
# queueObj=Queue(size)

# while True:
   
#     print("1.Enqueue elements in the Queue")
#     print("2.Show elements in the Queue")
#     print("3.Queue is empty")
#     print("4.Dequeue the elemets from Queue")
#     print("5.delete the elements from Queue")
#     print("6. Peek element:")
#     print("7.Exit......................")
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         val=int(input("enter the value in Queue:"))
#         queueObj.Enqueue(val)
#     elif choice==2:
#         queueObj.displayQueue()
#     elif choice==3:
#         print(queueObj.isEmpty())
#     elif choice==4:
#         print(queueObj.Dequeue())
#     elif choice==5:
#         print(queueObj.deleteQueue()) 
#     elif choice==6:
#         print(queueObj.peek())
#     else:
#         sys.exit()
# -----------------------------------------------------------------------
   