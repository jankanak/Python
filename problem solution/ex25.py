def break_words(kanak):
    words=kanak.split(' ')
    return words
def sort_words(words):
    return sorted(words)
def print_first_word(words):
     """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)
