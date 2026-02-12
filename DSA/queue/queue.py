class Queue:
    def __init__(self):
        self.q = []
        
    def isEmpty(self):
        return len(self.q) == 0
    
    def insert(self,value):
        self.q.append(value)
    
    def delete(self):
        if(self.isEmpty()):
            raise Exception("queue is empty")
        else:
            return self.q.pop(0)
            
q = Queue()
q.insert(10)
q.insert(20)
print(q.delete())
print(q.delete())