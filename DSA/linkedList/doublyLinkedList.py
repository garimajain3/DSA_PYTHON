class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLL:
    
    
    def __init__(self):
        self.head = None
            
    def insertAtTheEnd(self,value):
        temp = Node(value)
        if(self.head is None):
            self.head = temp
            return
        t = self.head
        while(t.next is not None):
            t = t.next 
        t.next = temp
        temp.prev = t
        
    def insertAtbeg(self,value):
        temp = Node(value)
        while(self.head is None):
            self.head = temp
            
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        
    def insertAtmid(self,value,x):
        t = self.head
        while(t.next!=None):
            if(t.data==x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t
        
    
    def reverseDLL(self):
        current = self.head
        temp = None
        
        while(current is not None):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
            
        if temp is not None:
            self.head = temp.prev
        
    def deleteDll(self,value):
        
        if(self.head == None):
            print("linked list is empty")
            return
        t = self.head
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next is not None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if(t.data==value):
            t.prev.next = None
                
            
        
    
        
        
    def printDll(self):
        t1 = self.head
        while(t1.next!= None):
            print(t1.data)
            t1=t1.next 
        print(t1.data)
        
obj = DoublyLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.printDll()
print("----------")
obj.insertAtbeg(0)
obj.printDll()
print("----------")
obj.insertAtmid(15,10)
obj.printDll()
print("reverse ------")
obj.reverseDLL()
obj.printDll()
print("-----")
obj.deleteDll(15)
obj.printDll()
print("-----")
obj.deleteDll(20)
obj.printDll()