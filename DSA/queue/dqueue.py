class DQueue:
    def __init__(self):
        self.dq = []
        
    def isEmpty(self):
        return len(self.dq)==0
    
    def insertAtEnd(self,val):
        self.dq.append(val)
        
    def insertAtFront(self,val):
        self.dq.insert(0,val)
        
    def deleteAtStart(self):
        if(self.isEmpty()):
            print("queue is empty")
            
        else:
            return self.dq.pop(0)
        
    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("queue is empty")
        else:
            return self.dq.pop()
    
q = DQueue()
q.insertAtFront(50)
q.insertAtEnd(10)
q.insertAtEnd(20)
print(q.deleteAtEnd())
print(q.deleteAtStart())
print(q.deleteAtStart())
print(q.deleteAtStart())
