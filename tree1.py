class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        
    def addChild(self,child):
        self.children.append(child)
        
    def __str__(self,level=0):
        ret="  "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)#recursion
        return ret
    
#object creation:
rootNode=Tree("Drinks")
hot=Tree("Hot")
cold=Tree("Cold")
tea=Tree("Tea")
coffe=Tree("coffe")
nonAlchoholic=Tree("nonAlchoholic")
alchoholic=Tree("Alchoholic")

rootNode.addChild(hot)
rootNode.addChild(cold)
hot.addChild(tea)
hot.addChild(coffe)
cold.addChild(nonAlchoholic)
cold.addChild(alchoholic)
print(rootNode)
        