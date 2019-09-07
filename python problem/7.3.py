class circle(object):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
ab=circle(2)
de=ab.area()
print(de)
