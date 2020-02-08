# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
# and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
#1010
value=[]
items=input().split(",")
for p in items:
    item=int(p,2)
    if item %5 ==0:
        value.append(p)

print(",".join(value))


############ hexadecimal number input 
# value1=[]
# items1=input().split(",")
# for h in items1:
#     con=int(h,16)
#     if con %5 ==0:
#         value1.append(h)

# print(",".join(value1))
