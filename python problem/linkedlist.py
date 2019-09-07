class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,item):
        self.data=item
    def setnext(self,newnext):
        self.next=newnext

class unorderlist:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,item):
        temp=Node(item)
        temp.setnext(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count=0
        while current !=None:
            current=current.getnext()
            count+=1
        return count
    def search(self,item):
        current=self.head
        found=False
        while current !=None and not found:
            if current.getdata()==item:
                found=True
            else:
                current=current.getnext()
        return found
        

mylist = unorderlist()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
print(mylist.size())
print(mylist.search(17))
