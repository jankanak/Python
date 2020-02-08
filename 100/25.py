# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later

class Person:
    name="kanak"

    def __init__(self,name=None):
        self.name=name
        print(name)
    
pust=Person("cse")
print(Person.name)
print(pust.name)
nico=Person()
nico.name = "Nico"
print(nico.name)