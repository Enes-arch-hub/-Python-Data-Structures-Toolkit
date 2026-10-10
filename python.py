#creating a node class 
class Node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedate = val
        
#creating an instance of the Node class to construct the tree shown in the image above

root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5) 

def Incrd(root):
    if root:
        Incrd(root.childleft)
        print(root.nodedate,end=" ")
        Incrd(root.childright)