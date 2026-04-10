# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
        
#     def addChild(self,child):
#         self.children.append(child)
        
#     def __str__(self,level=0):
#         ret="  "*level+str(self.data)+"\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)#recursion
#         return ret
    
# #object creation:
# rootNode=Tree("N1")
# n2=Tree("N2")
# n3=Tree("N3")
# n4=Tree("N4")
# n5=Tree("N5")
# n6=Tree("N6")
# n7=Tree("N7")
# n9=Tree("N9")
# n10=Tree("N10")

# rootNode.addChild(n2)
# rootNode.addChild(n3)
# n2.addChild(n4)
# n2.addChild(n5)
# n3.addChild(n6)
# n3.addChild(n7)
# n4.addChild(n9)
# n4.addChild(n10)
# print(rootNode)
        

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Binarytree:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        pass
        if self.root is None:
            self.root=Node(value)
        else:
            self.insertNode(self.root,value)
    
    def insertNode(self,rootNode,value):
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left=Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right=Node(value)
            else:
                self.insertNode(rootNode.left,value)
                
    
    def __str__(self,level=0):
        ret="  "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)#recursion
        return ret
    
btobj=Binarytree()
btobj.insert(50)
btobj.insert(30)   
btobj.insert(70)     

print(btobj)