def printValue(n):
	print (str(n))

printValue(35.89)
def sumvalue(s1,s2):
    print(int(s1)+int(s2))
sumvalue("3","8")
def length(n1,n2):
    l1=len(n1)
    l2=len(n2)
    if l1>l2:
        print(l1)
    elif(l1<l2):
        print(l2)
    else:
        print(l1)
        print(l2)

length("one","three")
def printdict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)

printdict()
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print (v)
		

printDict()
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[:5])
		

printList()
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (tuple(li))
		
printTuple()

tp=(1,2,3,4,5,6,7,8,9)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print (tp2)







