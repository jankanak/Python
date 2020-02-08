# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

# li=[1,2,3,4,5,6,7,8,9,10]
# even=filter(lambda x: x%2==0,li)
# print(even)

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = list(filter(lambda x: x%2==0, li))
print (evenNumbers)
# x=lambda a,b: a*b+5
# print(x(5,6))

def myfunc(n):
    
    return lambda a : a * n
mytripler = myfunc(3)

print(mytripler(2))