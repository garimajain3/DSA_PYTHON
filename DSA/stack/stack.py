class Stack:
    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    
    def push(self,value):
        # self.s.insert(0,value)
        self.s.append(value)
    
    def peek(self):
        if len(self.s)==0:
            raise Exception("stack is empty")
        else:
            return self.s[-1]
        
    def pop(self):
        if len(self.s)==0:
            raise Exception("stack is empty")
        else:
            # return self.s.pop(0)
            return self.s.pop()
        
obj = Stack()
obj.push(10)
obj.push(20)
print(obj.peek())
print(obj.pop())
# print(obj.peek())