class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def preOrder(root):
    if(root!=None):
        print(root.data,end=" ")
        preOrder(root.left)
        
        preOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(8)
preOrder(root)
        