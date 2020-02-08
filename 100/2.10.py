# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

# Use int() to convert a string to integer.

def printsum(s1,s2):
    return int(s1)+int(s2)

print(printsum("4","7"))

#Define a function that can accept two strings as input and concatenate them and then print it in console.

def concatenate(s1,s2):
    print(s1+s2)
concatenate("5","7")

# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

# Use len() function to get the length of a string0

def length(number1,number2):
    l1=len(number1)
    l2=len(number2)
    if l1>l2:
        print(number1)
    elif l1<l2:
        print(number2)
    else:
        print(number1)
        print(number2)
length("kam","cse")

#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
def keyssquare():
    d=dict()
    d[1]=1**2
    d[2]=2**2
    d[3]=3**2
    print(d)
keyssquare()

#Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def dictSquare():
    d=dict()
    for i in range(1,21):
        d[i]=i**2

    print(d)
dictSquare()

#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
def dictSquare():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for key,value in d.items():
        print(value)
dictSquare()

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

def dictSquare():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for key,value in d.items():
        print(key)
dictSquare()

#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def listSquare():
    li=list()
    for i in range(0,21):
        li.append(i**2)
    print((li))
listSquare()

# ##list out of index problem
i = [1, 2, 3, 5, 8, 13]
# j = [None] * len(i)
#j == [None, None, None, None, None, None]
#j=i[:]
j=[l for l in i]

k = 0

for l in i:
   j[k] = l
   k += 1
print(j)

# #Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[:5])
printList()

# #Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[-5:])
printList()

#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))
printList()

# #Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

# tp=(1,2,3,4,5,6,7,8,9,10)
# li=list()
# for i in tp:
# 	if tp[i]%2==0:
# 		li.append(tp[i])

# tp2=tuple(li)
# print (tp2)
