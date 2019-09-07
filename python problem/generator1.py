def evengenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=input()
values=[]
for i in evengenerator(n):
    values.append(str(i))

print(",".join(values))

def gene(n):
    i=0
    for i in range(n+1):
        
        if i%5==0 and i%7==0:
            yield i
        i+=1

n=input()
value=[]
for i in gene(n):
    value.append(str(i))

print(",".join(value))

    
