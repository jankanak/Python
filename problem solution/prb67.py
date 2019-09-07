d=dict(weather="clima",earth="terra",rain="chuva")
def vocabulary(word):
    try:
        return d[word]
    except:
        return "there is keyerror"

word=input("enter a word:").lower()
print(vocabulary(word))