class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return  self.items.pop(0)
    def peek(self):
        return self.items[0]
    def length(self):
        return len(self.items)
    
s=Stack()
s.push('kanak')
s.push('cse')
#s.push('pabna')
print(s.peek())
#print(s.pop())
print(s.pop())
print(s.length())
