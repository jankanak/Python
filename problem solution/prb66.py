d=dict(weather="clima",earth="terra",rain="chuva")

def vocabulary(word1):
    return d[word1]

word1=input("enter a word:")
word2=vocabulary(word1)
print(word2)

word=input("enter a valid name :")
if word=='weather':
    print(d['weather'])
elif word=='earth':
    print(d['earth'])
else:
    print(d['rain'])


