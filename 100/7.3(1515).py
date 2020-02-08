# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# 5
# Then, the output of the program should be:
# 500

# def fn(n):
#     if n==0:
#         return 0
#     else:
#         return fn(n-1)+100

# n=int(input())
# print(fn(n))

#####Fibonacci numbers 

# def fn(num):
#     if num ==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fn(num-1)+fn(num-2)

# n=int(input())
# print(fn(n))

# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13


def f(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return f(num-1)+f(num-2)
n=int(input())
value=[str(f(x)) for x in range(0,n+1)]
print(",".join(value))