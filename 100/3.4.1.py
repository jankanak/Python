## some very important notes about map and filter \
#map returns both value and true false .when we check condition it returns true false otherwise return value
##filter



#Write a program which can map() to make a list whose elements are square of elements in 

li=[1,2,3,4,5,6,7,8,9,10]
squareNumbers=filter(lambda x: x%2==0,range(1,11))
squareNumber=map(lambda x: x%2==0,range(1,11)) ####map is used to check the true false when we try to check a condition 
square=map(lambda x: x**2,range(1,11)) 
print(list(squareNumbers))
print(list(squareNumber))####print true false because we check the condition
print(list(square)) ## we are not checking the condition that is why a list is print otherwise a map printed a true false when we check a condition


#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
li1=[1,2,3,4,5,6,7,8,9,10]
evenSquare=filter(lambda x: x%2==0,(map(lambda x: x**2,li1)))
print(list(evenSquare))

li2=[1,2,3,4,5,6,7,8,9,10]
def square(num):
    return num**2

squared=map(square,li2)
print(list(squared))

#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)
evenNumber=map(lambda x: x%2==0,[x for x in range(1,21)])
oddNumber=(map(lambda x: x%2!=0, range(1,21)))
print(list(evenNumber))
values = ','.join(str(v) for v in oddNumber)
# print(values)
print(values)