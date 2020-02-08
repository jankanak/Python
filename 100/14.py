# Write a program that accepts a sentence and calculate the number of upper case letters and 
# lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


words=input()
num={"upper case":0 ,"Lower case":0}
for c in words:
    if c.isupper():
        num["upper case"] +=1
    elif c.islower():
        num["Lower case"] +=1
    else:
        pass

print("upper case",num["upper case"])
print("lower case ",num["Lower case"])