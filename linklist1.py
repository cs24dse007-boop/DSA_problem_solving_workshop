# class Node:
#     def __init__(self,data):
#         self.data=data #instance var
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None

# Linkedlist=Linkedlist()
# Linkedlist.head=Node(5)
# second=Node(10)
# third=Node(15)

# print(Linkedlist.head.data)
# print(second.data)
# print(third.data)


# print(Linkedlist.head.next)
# print(second.next)
# print(third.next)


# #linking part
# Linkedlist.head.next=second
# second.next=third

# #display linkedlist
# while Linkedlist.head!=None:
#     print("|",Linkedlist.head.data,"|",Linkedlist.head.next,"|")
#     Linkedlist.head=Linkedlist.head.next
import sys    
class Node:
    def __init__(self,data):
       self.data=data #instance var
       self.next=None
       
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,value):
        node=Node(value)
        if self.head is None:
          self.head=node
          self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def displayNode(self):
        temp = self.head
        while temp is not None:
           print("---------------------------------------------------")
           print(temp.data, '|', temp.next, '|')
           print("---------------------------------------------------")
           temp = temp.next
    def addNodeBegining(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
    def addNodeBetween(self,index,value):
        node =Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        elif index==0:
            node.next=self.head
            self.head=node
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            node.next=temp.next
            temp.next=node
               
if __name__=='__main__':
    object=Linkedlist()
    
    while True:
        print("1.Add node linkedlist:")
        print("2.Show  linkedlist:")
        print("3.Add node at begining:")
        print("4.Add node at between:")
        print("6.delete linkedlist:")
        print("7.Exit")
        
        
        ch=int(input("Enter your choice:"))
        if ch==1:
            value=int(input("Enter the value:"))
            object.addNode(value)
        elif ch==2:
            object.displayNode()
        elif ch==3:
            value=int(input("Enter the value:"))
            object.addNodeBegining(value)
        elif ch==4:
            value=int(input("Enter the value and add node in between:"))
            index=int(input("Enter the position after that you have to insert:"))
            object.addNodeBetween(index,value)
            print('Node added successfully in between')
            
            
        else:
            sys.exit()
            