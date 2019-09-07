from  sys import argv
from os.path import exists
script,from_file,to_file=argv
print("copying from %s to %s file" %(from_file,to_file))
indata=open(from_file)
fl=indata.read()
print("The input file is %s bytes long" %len(fl))
print("does the file exists ? \n %s" %exists(to_file))
fk=open(to_file,'w')
fk.write(fl)
print("ok alright ")
