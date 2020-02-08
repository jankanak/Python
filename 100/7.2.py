# class American(object):
#     @staticmethod
#     def printNationality():
#         print ("America")

# anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()

#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

# import math
# class Circle(object):
#     def __init__(self,radius):
#         self.r=radius
    
#     def area(self):
#         return self.r**2*3.14
    
# a=Circle(2)
# print(a.area())

#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

# class Rectangle:
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def area(self):
#         return self.length*self.width
    
# rec=Rectangle(4,5)
# print(rec.area())

#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
#  Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# class Shape(object):
    
#     def __init__(self):
#         pass
#     def area():
#         return 0

# class Square(Shape):

#     def __init__(self,l):
#         Shape.__init__(self)
#         self.length=l

#     def area(self):
#         return self.length*self.length

# a=Square(3)
# print(a.area())


class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        self.msg = msg
        

error = MyError("something wrong" )
print(error)