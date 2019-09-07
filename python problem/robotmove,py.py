l=[]
for i in range(100,200):
    if(i%2==0):
        l.append(str(i))

print(','.join(l))

x=int(input())
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

print(fact(x))

