from  sys import argv
script,filename=argv
print("this is your filename %r :"%(filename))
fil=open(filename)
print(fil.read())
print("please write the file name again ")
file_again=input('>')
text_again=open(file_again)
print(text_again. read())
