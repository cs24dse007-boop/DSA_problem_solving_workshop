#Stack implementation with size limit
import sys
class Stack:
    def __init__(self,stackSize):#parameterized constructor
        self.stackList=[] #stack created
        self.stackSize=stackSize
        
    def isFull(self):
        if len(self.stackList)== self.stackSize:
            return True
        else:
            return False      
    def push(self,value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.stackList.append(value)
        
    
    def displayStack(self):
        print("-----------------------------")
        print(self.stackList)
        print("-----------------------------")
        
    def isEmpty(self):
        if self.stackList==[]:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty" 
        else:
            return self.stackList.pop()
    def deleteStack(self):
        self.stackList=None
        return "Stack is deleted"
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stackList[-1]

size=int(input("Enter the stack size:"))        
StackObj=Stack(size)

while True:
   
    print("1.Push elements in the stack")
    print("2.Show elements in the stack")
    print("3.stack is empty")
    print("4.Pop the elemets from stack")
    print("5.delete the elements from stack")
    print("6. Peek element:")
    print("7.Exit......................")
    choice=int(input("enter your choice:"))
    if choice==1:
        val=int(input("enter the value in stack:"))
        StackObj.push(val)
    elif choice==2:
        StackObj.displayStack()
    elif choice==3:
        print(StackObj.isEmpty())
    elif choice==4:
        print(StackObj.pop())
    elif choice==5:
        print(StackObj.deleteStack())
    elif choice==6:
        print(StackObj.peek())
    else:
        sys.exit()
    