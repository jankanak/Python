class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self,name):
        # self.name is the instance parameter
        self.name = name

jeffrey =Person("kanak")
print ("%s name is %s" % (Person.name, jeffrey.name))
cse=Person("pust")
print("%s "%(Person.name))

