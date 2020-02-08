# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# 7
# Then, the output of the program should be:

0,1,1,2,3,5,8,13
def fn(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fn(n-1)+fn(n-2)
    
n=int(input())
values=[str(fn(x)) for x in range(0,n+1)]
print(values)

# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# 10
# 0,2,4,6,8,10
# Hints:
# Use yield to produce the next value in generator.

def Even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input())

values=[]
for i in Even(n):
    values.append(str(i))

print(",".join(values))


# Please write a program using generator to print the numbers 
# which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# 100

# 0,35,70

def numGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values=[]
for i in numGenerator(n):
    values.append(str(i))
print(",".join(values))

def divisible(num1):
    
    for i in range(0,num1):
        if i%5==0 and i%7==0:
            print(i)

num1=int(input())
divisible(num1)


####   assert in python 

li = [2,4,6,8]
for i in li:
    assert i%3==0

###random float generation

import random
print (random.random()*100)

# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# Use random.choice() to a random element from a list.

import random
print(random.choice([x for x in range(11) if x%2==0]))

print (([i for i in range(201) if i%5==0 and i%7==0]))

import random
print (random.sample(range(100), 2))


#Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
print(random.sample([x for x in range(100,200) if x%5==0 and x%7==0 ],2))