class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def InOrder(root):
    if(root!=None):
        
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(8)
InOrder(root)
        