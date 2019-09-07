class binarytree:
    def __init__(self,key):
        self.value=key
        self.leftchild=None
        self.rightchild=None
    def setrootvalue(self,obj):
        self.value=obj
    def getrootvalue(self):
        return self.value

    def insertleft(self,new):
        if self.leftchild==None:
            self.leftchild=binarytree(new)
        else:
            t=binarytree(new)
            t.leftchild=self.leftchild
            self.leftchild=t

    def insertright(self,new):
        if self.rightchild==None:
            self.rightchild=binarytree(new)
        else:
            t=binarytree(new)
            t.rightchild=self.rightchild
            self.rightchild=t
    def getleftchild(self):
        return self.leftchild
    def getrightchild(self):
        return self.rightchild
tree=binarytree('a')
print(tree.getrootvalue())
tree.insertleft('b')
tree.insertright('c')
print(tree.getleftchild().getrootvalue())
print(tree.getrightchild().getrootvalue())



