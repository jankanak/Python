alphabet=['a','c','d','o','p','u']
def filtervowels(alphabet):
    vowels=['a','e','i','o','u']
    if (alphabet in vowels):
        return True
    else:
        return False
    
    
filteredvowels=filter(filtervowels,alphabet)

print('The filtered vowels are:')
for vowel in filteredvowels:
    print(vowel)
