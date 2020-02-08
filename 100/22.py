#####set version of count the frequency of words 
def frequency(name):
    name=name.split(" ")
    duplicate=set(name)
    for words in duplicate:
        print('frequency of ',words,'is',name.count(words))


if __name__ == "__main__":
    name=input()
    frequency(name)

#list version of counting the frequency of words in a line 

def frequency(words):
    line=words.split(" ")
    line1=[]
    for i in line:
        if i not in line1:
            line1.append(i)
    for j in range (0,len(line1)):
        print ('the frequency of ',line1[j],'is:',line.count(line1[j]))
def main():
    words=input()
    frequency(words)

if __name__ == "__main__":
    main()