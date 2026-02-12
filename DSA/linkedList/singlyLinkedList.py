class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class SinglyLL:
    def __init__(self,head=None):
        self.head = head
    
    def insertAtTheEnd(self,val):
        temp = Node(val)
        
        if(self.head!=None):
            t1 = self.head
            while(t1.next!=None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtBegining(self,val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        
    
    def insertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next!=None):
            if(t1.data==x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
        
    def deleteSinglyLL(self, value):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        prev = self.head
        curr = self.head.next
        
        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def reverseSingleLL(self):
        t1 = self.head
        prev = None
        while(t1.next is not None):
            next_node = t1.next
            t1.next = prev
            prev = t1
            t1 = next_node
        self.head = prev

    def printSinglyLL(self):
        t1 = self.head
        while(t1.next is not None):
            print(t1.data)
            t1=t1.next
        print(t1.data)

obj = SinglyLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20) 
obj.insertAtTheEnd(30)
obj.printSinglyLL()
print("--------------------")
obj.insertAtBegining(0)
obj.printSinglyLL()
print("-------------")
obj.insertAtMid(20.5,20)
obj.printSinglyLL()
print("--------------")
obj.reverseSingleLL()
obj.printSinglyLL()
print("garima--------")
obj.deleteSinglyLL(0)
obj.printSinglyLL()
print("----------")
obj.deleteSinglyLL(20.5)
obj.printSinglyLL()
print("----------")
obj.deleteSinglyLL(30)
obj.printSinglyLL()
print("----------")
     