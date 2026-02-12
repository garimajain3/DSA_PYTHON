class CQueue:
    def __init__(self,size): #here size we are mentioning because we want to create fixed size list
        self.size =  size
        self.items = [None]*size
        self.rear =self.front = -1
        
    def enqueue(self,value):
        if((self.rear+1)%self.size == self.front):
            print("queue is full")
        elif self.front== -1:
            self.rear = self.front = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear+1)%self.size
            self.items[self.rear] = value
            
    def dequeue(self):
        if(self.front== -1):
            print("queue is empty")
        elif self.rear == self.front:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front+1)%self.size 
            
            
dq = CQueue(5)
            
# dq.enqueue(10)
# dq.enqueue(20)
# dq.enqueue(20)
# dq.enqueue(20)
# dq.enqueue(20)
dq.dequeue()
# dq.enqueue(20)

# dq.enqueue(20)