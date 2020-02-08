# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the
#  object is in ["Hockey","Football"].

# Hints:
# Use list[index] notation to get a element from a list.

# subject=["I","You"]
# verb=["Play", "Love"] 
# objects=["Hockey","Football"]

# for p in range(len(subject)):
#     for q in range(len(verb)):
#         for r in range(len(objects)):
#             print("%s %s %s."%(subject[p],verb[q],objects[r]))


# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

# li=[12,24,35,70,88,120,155]
# for i,m in enumerate(li):
#     if i%2=0:
#         print(m)

# li=[12,24,35,70,88,120,155]
# values=[x for (i,x) in enumerate(li) if i%2!=0]
# print(values)


# li=[12,24,35,70,88,120,155]
# values=[x for (i,x) in enumerate(li) if i not in(0,3,5)]
# print(values)


# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.

# Solution:

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
nothing=Person()
print (aMale.getGender())
print (aFemale.getGender())
print (nothing.getGender())